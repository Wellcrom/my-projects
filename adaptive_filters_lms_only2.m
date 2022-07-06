%MatLab/Octave

clear all; close all; clc 
%% Initialization

% channel parameters
sigmaS = 1; %signal power
sigmaN = 0.01; %noise power
% CSI (channel state information):
channel = [0.722-1j*0.779; -0.257-1j*0.722; -0.789-1j*1.862]; 

M = 5; % filter order

% step sizes
mu_LMS = [0.01,0.07];

NS = 1000; %number of symbols
NEnsembles = 1000; %number of ensembles

%% Compute Rxx and p

%the maximum index of channel taps (l=0,1...L):
L = length(channel) - 1;  
H = convmtx(channel, M-L); %channel matrix (Toeplitz structure)
Rnn = sigmaN*eye(M); %the noise covariance matrix

%the received signal covariance matrix:
Rxx = sigmaS*(H*H')+sigmaN*eye(M);
%the cross-correlation vector 
%between the tap-input vector and the desired response: 
p = sigmaS*H(:,1); 

% An inline function to calculate MSE(w) for a weight vector w
calc_MSE = @(w) real(w'*Rxx*w - w'*p - p'*w + sigmaS);

%% Adaptive Equalization
N_test = 2;
MSE_LMS = zeros(NEnsembles, NS, N_test);

for nEnsemble = 1:NEnsembles
	%initial symbols:
	symbols = sigmaS*sign(randn(1,NS));
	%received noisy symbols:
	X = H*hankel(symbols(1:M-L),[symbols(M-L:end),zeros(1,M-L-1)]) + sqrt(sigmaN)*(randn(M,NS)+1j*randn(M,NS))/sqrt(2); 
	for n_mu = 1:N_test
		w_LMS = zeros(M,1);
		for n = 1:NS
			%% LMS - Least Mean Square
			e = symbols(n) - w_LMS'*X(:,n);
			w_LMS = w_LMS + mu_LMS(n_mu)*X(:,n)*conj(e);
			MSE_LMS(nEnsemble,n,n_mu)= calc_MSE(w_LMS);
		end
	end
end

MSE_LMS_1 = mean(MSE_LMS(:,:,1));
MSE_LMS_2 = mean(MSE_LMS(:,:,2));

n = 1:NS;
m = [1 3 6 10 30 60 100 300 600 1000];

figure(1)
loglog(m, MSE_LMS_1(m),'x','linewidth',2, 'color','green');
hold all;
loglog(m, MSE_LMS_2(m),'o','linewidth',2, 'color','blue');

wopt = Rxx\p;
MSEopt = calc_MSE(wopt);

loglog(n, MSEopt*ones(size(n)),'linewidth',2,'color','black');
loglog(n, MSE_LMS_1(n),'linewidth',2, 'color','green');
loglog(n, MSE_LMS_2(n),'linewidth',2, 'color','blue');


grid on
xlabel('Ns');
ylabel('Mean-Squares Error');
title('LMS')
legend(['LMS, \mu=' num2str(mu_LMS(1))],['LMS, \mu=' num2str(mu_LMS(2))],'Wiener solution')