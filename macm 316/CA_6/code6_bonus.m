g = @(x) x.^(-1).*cos(x.^(-2).*log(x));
x = linspace(0,0.005,1);
I = simp(g,0.1,1,10); % simpsons approximation of the function

%% 

length = 2000;
step = 1;
Q = zeros(1,length/step);
nArr = 1:1:length;

j = 1;
for n = 1:step:length
    b = zeros(1,n);
    a = zeros(1,n); 
    I2 = zeros(1,n);
    a(1) = 1;
    for i = 1:n
%         b(i)=fzero(@(x) x*exp(x)-i*pi,0);
%         b(i)=fzero(@(x)x*exp(2x)-i*pi+pi/2,0);
        b(i) = fzero(@(x) x* exp(2*x) -i*pi+(pi/2),0);

        a(i+1)=exp(-(b(i)));
    end
    
    for i = 1:(n-1)
        I2(i) = integral(g,a(i+1),a(i));
    end
    
    Q(j) = sum(I2);
    j= j+1;
end

figure(1)
plot(nArr,Q)
xlabel("X values")
ylabel("Area underneath the curve")


size = length/step;
nArr2 = 1:step:length-2*step;
Qhat = zeros(1,size-2);
for i = 1: size-2
    Qhat(i) = (Q(i) * Q(i+2) - (Q(i+1))^2)/(Q(i+2) -2*Q(i+1) + Q(i));
   
end
figure(2)
plot(nArr2,Qhat)
xlabel("X values")
ylabel("Area underneath the curve")



%% 
format long
disp(Qhat)
disp(Q)
