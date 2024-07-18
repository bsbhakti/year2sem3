% MACM 316 - Week 12
% Euler's method demo
% Description: Applies Euler's method
% File name: Euler1.m

clear;clf;

% IVP parameters
a=0.0;
b=2.0;
y0=1.0;
f = @(t,y) (1+t)./(1+y);

% Exact solution
Y=@(t) sqrt(4+2.*t+t.^2)-1; 

% Euler's method parameters
N=40;
h=(b-a)/N;
tt=a:h:b;
w=zeros(N+1,1);
w(1)=y0;

% Euler steps
for i=1:N
    w(i+1)=w(i)+h*f(tt(i),w(i));
end

% Plot approximation and error
figure(1);
subplot(2,1,1);
hold on
plot(tt,w)
t_int=a:0.001:b;
plot(t_int,Y(t_int),'r')

title('Euler''s method','fontsize',14)
xlabel('t-axis','fontsize',12)
ylabel('y-axis','fontsize',12)
legend({'y(t)','Euler'},'fontsize',14,'Location','southeast')

subplot(2,1,2);
Err=abs(w'-Y(tt));
plot(tt,Err)
title('Error of Euler''s method','fontsize',14)
xlabel('t-axis','fontsize',12)
ylabel('y-axis','fontsize',12)

disp(['N=' num2str(N) '  ' 'Global error=' num2str(max(Err))]);
