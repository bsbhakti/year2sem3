clear;
close all;

format long;

nArr = 1:1:100;

b = length(nArr);
mainError1 = zeros(b,1);
mainError2 = zeros(b,1);
mainError3 = zeros(b,1);
mainError4 = zeros(b,1);
% size(mainError1)

f3 = @(x) cos((10^4)*x);
for l = nArr
    
    n_vec = (0:l)';
    
    A = -1 + ((2*n_vec)/l);
    B = cos((n_vec.*pi)/l);

    y1 = 1./(5-(4.*A));
    y2 = 1./(1+(16.*(A.^2)));
    
    grid_size = 10000;
    grid = (linspace(-1,1,grid_size))'; %test values
    
    w = baryweights(A);
    w2 = weights(l);
    
    u1 =  baryinterp(A,w,y1,grid);
    u2 =  baryinterp(A,w,y2,grid);
%     size(A)
%     size(B)
%     size(w2)
%     size(y1)

%     size(u1)
   
%     size(w2)
%     size(y1)
    u3 =  baryinterp(B,w2,y1,grid);
    u4 =  baryinterp(B,w2,y2,grid);
    size(w2)
    size(B)
    size(y1)

    
    interp_y1 = (1./(5-(4.*grid)))';
    interp_y2 = (1./(1+(16.*(grid.^2))))';
   size(interp_y1)
    mainError1(l) = max(abs((u1 - interp_y1)'));
    mainError2(l) = max(abs((u2 - interp_y2)'));
    mainError3(l) = max(abs((u3 - interp_y1)'));
    mainError4(l) = max(abs((u4 - interp_y2)'));
end
%   
% figure(2)
% plot(grid,u2)
% hold on
% plot(grid,interp_y2)
% hold off

figure(1)
plot(nArr,log10(mainError1))
hold on
plot(nArr,log10(mainError3))
hold off
xlabel("N")
ylabel("Max error")

figure(2)
plot(nArr,log10(mainError2))
hold on
plot(nArr,log10(mainError4))
hold off
xlabel("N")
ylabel("Max error")


figure(3)
plot(nArr,log10(mainError1))
hold on
plot(nArr,log10(mainError2))
hold off
xlabel("N")
ylabel("Max error")
legend('1/5-4x','1/1+16x^2')



plot(n_values, log10(max_error), '*');
title('Max Error vs. N: F(x) = cos(10^4*x)', 'fontsize',14);
xlabel('Degree of interpolating polynomial N','fontsize',12);
ylabel('log10(Max Error)','fontsize',12);
legend('F(x) = cos(10^4*x)');

function weight_arr = weights(n)

weight_arr = zeros(n+1,1);
weight_arr(1) = (1/2);
for i = 2:n
    weight_arr(i) = -((-1)^i);
end
weight_arr(n+1) = - ((1/2) * ((-1)^n));

end