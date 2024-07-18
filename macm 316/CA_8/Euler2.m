% MACM 316 - Week 12
% Euler's method demo
% Description: Applies Euler's method to a system of two equations
% describing a pendulum
% File name: Euler1.m

clear

a=0; % Start time
b=5; % End time
g=9.8; % Gravitational constant
ll=0.5; % Pendulum length

% Initial conditions
w10=0.5*pi; 
w20=0;

% Stepsize and mesh
h=0.0001;

tt=a:h:b; % Mesh
N=length(tt);
w1=zeros(N,1); % Values for w1
w2=zeros(N,1); % Values for w2

w1(1)=w10; % Initial values
w2(1)=w20; % Initial values

% Euler steps
for i=1:N-1
    w1n=w1(i)+h*w2(i);
    w2n=w2(i)-h*g*sin(w1(i))/ll;
    w1(i+1)=w1n;
    w2(i+1)=w2n;
end

plot(tt,w1,tt,w2)
title('Euler''s method','fontsize',14)
xlabel('t-axis','fontsize',12)
legend({'theta(t)','theta''(t)'},'fontsize',14,'Location','southeast')

