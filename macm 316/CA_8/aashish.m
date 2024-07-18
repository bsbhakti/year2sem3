clear 
a=0; % Start time 
b=500; % End time 
% Stepsize and mesh 
h=0.0005; 
e=0.6; 
tt=a:h:b; % Mesh 


N=length(tt); 
q=zeros(N+1,2); % Values for w1 
p=zeros(N+1,2); % Values for v1 
sq=zeros(N+1,2); % Values for sw1 
sp=zeros(N+1,2); % Values for sv1 

q(1,1)=1-e; % Initial values 
q(1,2)=0;% Initial values 
p(1,1)=0; 
p(1,2)=sqrt((1+e)/(1-e)); 

sq(1,1)=1-e; % Initial values 
sq(1,2)=0;% Initial values 
sp(1,1)=0; 
sp(1,2)=sqrt((1+e)/(1-e)); 
% Euler steps 

for i=1:N 
q(i+1,1)=q(i,1)+h*p(i,1); 
q(i+1,2)=q(i,2)+h*p(i,2); 
p(i+1,1) = (-h*q(i,1))/(q(i,1)^2 + q(i,2)^2)^(3/2) + p(i,1); 
p(i+1,2) = (-h*q(i,2))/(q(i,1)^2 + q(i,2)^2)^(3/2) + p(i,2); 
sq(i+1,1)=sq(i,1)+h*sp(i,1); 
sq(i+1,2)=sq(i,2)+h*sp(i,2); 
sp(i+1,1) = (-h*sq(i+1,1))/(sq(i+1,1)^2 + sq(i+1,2)^2)^(3/2) + sp(i,1); 
sp(i+1,2) = (-h*sq(i+1,2))/(sq(i+1,1)^2 + sq(i+1,2)^2)^(3/2) + sp(i,2); 
end 
A = zeros(N+1,1); 
H = zeros(N+1,1); 
sA = zeros(N+1,1); 
sH = zeros(N+1,1); 

for i=1:N+1 
A(i) = q(i,1)*p(i,2) - q(i,2)*p(i,1); 
H(i) = 0.5*(p(i,1)^2 + p(i,2)^2) - (1/sqrt(q(i,1)^2 + q(i,2)^2)); 
sA(i) = sq(i,1)*sp(i,2) - sq(i,2)*sp(i,1); 
sH(i) = 0.5*(sp(i,1)^2 + sp(i,2)^2) - (1/sqrt(sq(i,1)^2 + sq(i,2)^2)); 
end 
plot(q(:,1),q(:,2),'r'); 
title('Kepler laws for planetary motion(Euler method)','fontsize',14) 
xlabel('q1','fontsize',12) 
ylabel('q2','fontsize',12) 
figure; 
plot(sq(:,1),sq(:,2),'r'); 
title('Kepler laws for planetary motion(Standard Euler method)','fontsize',14) 
xlabel('sq1','fontsize',12) 
ylabel('sq2','fontsize',12) 
figure; 
plot(1:N+1, A,'r',1:N+1,H,'b'); 
title('Graph of angular momentum and Hamiltonian(Euler method)') 
xlabel('t'); 
ylabel('Angular momentum and Hamiltonian'); 
legend('A(t)','H(t)'); 
figure; 
plot(1:N+1, sA,'r',1:N+1,sH,'b'); 
title('Graph of angular momentum and Hamiltonian(Standard Euler method)') 
xlabel('t'); 
ylabel('Angular momentum and Hamiltonian'); 
legend('A(t)','H(t)'); 