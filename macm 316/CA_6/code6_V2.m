g = @(x) x.^(-1).*sin(x.^(-1).*log(x));
x = linspace(0,1,1000);
figure(4)
plot(x,g(x))
xlabel("X values")
ylabel("Y values")
title("Function 1")
legend("x^(-1)*sin(x^(-1)*log(x))")
A = 100:100:1000;
for i = 1:10
I(i) = simp(g,0.1,1,A(i));  % simpsons approximation of the function
end
figure(3)
plot(A,I)
xlabel("N values")
ylabel('Area approximation')
title("Simpson's Approximation")
%% 


length = 1000;
step = 100;
Q = zeros(1,length/step);
nArr = 100:step:length;

j = 1;
for n = 100:step:length
    b = zeros(1,n);
    a = zeros(1,n); 
    I2 = zeros(1,n);
    a(1) = 1;
    for i = 1:n
        b(i)=fzero(@(x) x*exp(x)-i*pi,0);
        a(i+1)=exp(-(b(i)));
    end
    
    for i = 1:(n-1)
        I2(i) = integral(g,a(i+1),a(i));
    end
    
    Q(j) = sum(I2);
    j= j+1;
end


size = length/step;
nArr2 = 100:step:length-2*step;
Qhat = zeros(1,size-2);
for i = 1: size-2
    Qhat(i) = (Q(i) * Q(i+2) - (Q(i+1))^2)/(Q(i+2) -2*Q(i+1) + Q(i));
   
end
figure(1)
plot(nArr2,Qhat)
hold on;
plot(nArr,Q)
hold off;
xlabel("X values")
ylabel("Area underneath the curve")
title("Difference in convergence")
legend("Aitken's approximation","Summation method")



%% 
format long
disp(Qhat)
disp(Q)
