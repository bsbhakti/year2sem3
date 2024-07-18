g = @(x) x.^(-1).*sin(x.^(-1).*log(x));

I = simp(g,0.1,1,10); % simpsons approximation of the function

Q = zeros(1,10);
nArr = 100:100:1000;

length = 1000;
j = 1;
for n = 100:100:length
    b = zeros(1,n);
    a = zeros(1,n); 
    I2 = zeros(1,n);
    a(1) = 1;
    for i = 2:n-1
        b =fzero(@(x) x*exp(x)-i*pi,0);
        a(i)=exp(-b); 
        I2(i) = integral(g,a(i),a(i-1));
    end
    
    Q(j) = sum(I2);
    j= j+1;
end

figure(1)
plot(nArr,Q)
xlabel("X values")
ylabel("Area underneath the curve")

n2 = 1:8;
l2 = 1000-2;
size = length(Q);
Qhat = zeros(1,size-2);
for i = 1: size-2
    Qhat(i) = (Q(i) * Q(i+2) - (Q(i+1))^2)/(Q(i+2) -2*Q(i+1) + Q(i));
   
end
figure(2)
plot(n2,Qhat)
xlabel("X values")
ylabel("Area underneath the curve")

