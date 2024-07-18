format long
f1 = @(x) x.^3;
trapezoidrule(f1,0,1,100)

f2 = @(x) sin((1/2)*x);
f3 = @(x) abs(sin(2*x));
f4 = @(x) cos(x);


a1 = 0;
b1 = pi/3;
a2 = 0;
b2 = 2*pi;

resultMatrix = zeros(1,10);
actual1 = integral(f2,a1,b1);
actual2 = integral(f2,a2,b2);
actual3 = integral(f3,a1,b1);
actual4 = integral(f3,a2,b2);
actual5 = integral(f4,a1,b1);
actual6 = integral(f4,a2,b2);
N = 1000:100:100000;

error1 = zeros(1,10);
error2 = zeros(1,10);
error3 = zeros(1,10);
error4 = zeros(1,90);
error5 = zeros(1,90);
error6 = zeros(1,90);


j = 1;
for i = 1000:100:100000 %interval 1
    result = trapezoidrule(f2,a1,b1,i);
    result2 = trapezoidrule(f3,a1,b1,i);
    result3 = trapezoidrule(f4,a1,b1,i);
    error1(j) = abs((2-sqrt(3)) - result);
    error2(j) = abs((3/4) - result2);
    error3(j) = abs((sqrt(3)/2) - result3);
    j = j +1;
end
x = linspace(1,2*pi,50);
y1 = zeros(1,10);
y2 = zeros(1,10);
y3 = zeros(1,10);

p1 = polyfit(log(N),log(error1),1);
p2 = polyfit(log(N),log(error2),1);
p3 = polyfit(log(N),log(error3),1);

for i = 1:50
    y1(i) = p1(1) * x(i)+ p1(2);
    y2(i) = p2(1) * x(i)+ p2(2);
    y3(i) = p3(1) * x(i)+ p3(2);
end


% 
% figure(1)
% plot(x,y1)
% hold on;
% plot((x),(y2))
% hold on;
% plot((x),(y3))
%hold off;

figure(1)
loglog(N,error1)
hold on;
loglog(N,error2)
hold on;
loglog(N,error3)
hold off;
legend("sin(x/2)","abs(sin(2x)","cos(x)")
xlabel("N size")
ylabel("Log error")
title("Log error plot")

%% 

j = 1;
for i = 1000:100:100000 %interval 2
    result = trapezoidrule(f2,a2,b2,i);
    result2 = trapezoidrule(f3,a2,b2,i);
    result3 = trapezoidrule(f4,a2,b2,i);
    error4(j) = abs(4 - result);
    error5(j) = abs(4 - result2);
    error6(j) = abs(0 - result3);
    j = j +1;
end


p4 = polyfit(log(N),log(error4),1);
p5 = polyfit(log(N),log(error5),1);
p6 = polyfit(log(N),log(error6),1);

for i = 1:50
    y1(i) = p4(1) * x(i)+ p4(2);
    y2(i) = p5(1) * x(i)+ p5(2);
    y3(i) = p6(1) * x(i)+ p6(2);
end



figure(2)
loglog(N,error4)
hold on;
loglog(N,error5)
hold on;
loglog(N,error6)
hold off;
legend("sin(x/2)","abs(sin(2x)","cos(x)")
xlabel("N size")
ylabel("Log error")
title("Log error plot")
%% 

 eps







