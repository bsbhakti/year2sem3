clear 
a=0; 
b=10000; 

h=0.0005; 
e=0.6; 
tt=a:h:b; 


N=length(tt); 
q=zeros(N+1,2); 
p=zeros(N+1,2); 
symp_q=zeros(N+1,2); 
symp_p=zeros(N+1,2); 

q(1,1)=1-e; 
q(1,2)=0;
p(1,1)=0; 
p(1,2)=sqrt((1+e)/(1-e)); 

symp_q(1,1)=1-e;
symp_q(1,2)=0;
symp_p(1,1)=0; 
symp_p(1,2)=sqrt((1+e)/(1-e)); 


for i=1:N 
q(i+1,1)=q(i,1)+h*p(i,1); 
q(i+1,2)=q(i,2)+h*p(i,2); 
p(i+1,1) = (-h*q(i,1))/(q(i,1)^2 + q(i,2)^2)^(3/2) + p(i,1); 
p(i+1,2) = (-h*q(i,2))/(q(i,1)^2 + q(i,2)^2)^(3/2) + p(i,2); 
symp_q(i+1,1)=symp_q(i,1)+h*symp_p(i,1); 
symp_q(i+1,2)=symp_q(i,2)+h*symp_p(i,2); 
symp_p(i+1,1) = (-h*symp_q(i+1,1))/(symp_q(i+1,1)^2 + symp_q(i+1,2)^2)^(3/2) + symp_p(i,1); 
symp_p(i+1,2) = (-h*symp_q(i+1,2))/(symp_q(i+1,1)^2 + symp_q(i+1,2)^2)^(3/2) + symp_p(i,2); 
end 

figure(1)
plot(q(:,1),q(:,2)); 
title('Kepler laws for planetary motion(Euler method)','fontsize',14) 
xlabel('q1','fontsize',12) 
ylabel('q2','fontsize',12) 


figure(2); 
plot(symp_q(:,1),symp_q(:,2)); 
title('Kepler laws for planetary motion(Symplectic Euler method)','fontsize',14) 
xlabel('q1','fontsize',12) 
ylabel('q2','fontsize',12)
A = zeros(N+1,1); 
H = zeros(N+1,1); 
sA = zeros(N+1,1); 
sH = zeros(N+1,1); 

for i=1:N+1 
A(i) = q(i,1)*p(i,2) - q(i,2)*p(i,1); 
H(i) = 0.5*(p(i,1)^2 + p(i,2)^2) - (1/sqrt(q(i,1)^2 + q(i,2)^2)); 
sA(i) = symp_q(i,1)*symp_p(i,2) - symp_q(i,2)*symp_p(i,1); 
sH(i) = 0.5*(symp_p(i,1)^2 + symp_p(i,2)^2) - (1/sqrt(symp_q(i,1)^2 + symp_q(i,2)^2)); 
end 

 
figure(3); 
plot(1:N+1, A,'r',1:N+1,H,'b'); 
title('Angular momentum and Hamiltonian(Euler method)') 
xlabel('t'); 
ylabel('Angular and Hamiltonian momentum'); 
legend('Angular Momentum at t','Hamiltonian Momentum at t'); 

figure(4); 
plot(1:N+1, sA,'r',1:N+1,sH,'b'); 
title('Angular and Hamiltonian momentum(Symplectic Euler method)') 
xlabel('t'); 
ylabel('Angular and Hamiltonian'); 
legend('Angular Momentum at t','Hamiltonian Momentum at t'); 