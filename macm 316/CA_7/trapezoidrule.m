% Trap. rule

function [trap,h] = trapezoidrule(fun,a,b,N);
format long

h=(b-a)/N;
trap = (fun(a)+fun(b))/2;
x = a + h.*(1:N-1);
trap = trap + sum(fun(x));
trap = h*trap;

%for n = 1:N-1
%    trap = trap + fun(a+h*n);
%end

%trap = h*trap;


%format short
