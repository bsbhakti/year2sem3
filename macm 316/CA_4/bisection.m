% MACM 316 - Week 4
% Bisection method demo
% Description: applies the bisection method to f(x) and plots the error
% Name: bisection.m

% Define f(x)
f=@(x) sin(x);
rr=pi;

% Parameters
a=1; % Left endpoint a
b=5; % Right endpoint b
N=100; % Maximum number of iterations
tol=1e-15; % Tolerance

% Call the function bisfn.m
[r,data]=bisfn(f,a,b,N,tol);

% Print the data in long format
format 'long' 
data

% Plot f(x) and the computed root
figure(1); clf;
plot([a b],[0 0],'k')
hold 'on'
st=0.0001;
x=a:st:b;
plot(x,f(x));
plot(r,0,'r*');
xlabel('x-axis','fontsize',12)
ylabel('y-axis','fontsize',12)
title('Bisection method output','fontsize',14)

% Plot the error versus iteration number
figure(2);
semilogy(abs(data(:,3)-rr*ones(length(data),1)))
xlabel('Iteration number','fontsize',12)
ylabel('Absolute error','fontsize',12)
title('Bisection method error','fontsize',14)