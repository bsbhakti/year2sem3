
format long;
clear;
close("all");

grid = (-1:0.0001:1)';

n_max = 100;
n_arr = 1:n_max;

err_eq_f1 = zeros(n_max,1);
err_eq_f2 = zeros(n_max,1);
err_ch_f1 = zeros(n_max,1);
err_ch_f2 = zeros(n_max,1);

for n = n_arr    
    err_eq_f1(n) = get_eq_space_interp_error(n, @f1, grid);
    err_eq_f2(n) = get_eq_space_interp_error(n, @f2, grid);

    err_ch_f1(n) = get_chebyshev_interp_error(n, @f1, grid);
    err_ch_f2(n) = get_chebyshev_interp_error(n, @f2, grid);
end

figure("Name","F1")
plot(n_arr,log10(err_eq_f1));
hold on;
plot(n_arr,log10(err_ch_f1));
hold off;
xlabel("N");
ylabel("Error");
title("Function 1");
legend('Barycentric','Chebyshev nodes');

figure("Name","F2")
plot(n_arr,log10(err_eq_f2));
hold on;
plot(n_arr,log10(err_ch_f2));
hold off;
xlabel("N");
ylabel("Error");
title("Function 2");
legend('Barycentric','Chebyshev nodes');

err_f3 = zeros(100,1);

n_tol = 0;
n=10;
% while err_f3 > 10^-5
for i = 1:1200
    err_f3(i) = get_chebyshev_interp_error(n, @f3, grid);

    if err_f3(i) < 10^-5 && n_tol == 0
        n_tol = n;
    end

    n = n + 10;
end

figure1("Name","F3")
plot(10:10:100,log10(err_f3),"DisplayName","Chebyshev Nodes");
xlabel("N")
ylabel("Log(error)")
title("cos((10^4)*(x))")


sprintf("Smallest value of N with err < 10^-5 : %d",(n_tol));

function err = get_chebyshev_interp_error(n, f, grid)

    x_arr = cal_chebyshev_x((0:n),n)';
    
    w = chebyshev_weights(n+1);
    
    y_arr = f(x_arr);
    u = baryinterp(x_arr, w, y_arr, grid);
    y_f1 = f(grid);
    
    diff = u - y_f1;
    err = max(abs(diff'));
end

function err = get_eq_space_interp_error(n, f, grid)

    x_arr = cal_x((0:n),n)';
    
    w = baryweights(x_arr);
    
    y_arr = f(x_arr);
    u = baryinterp(x_arr, w, y_arr, grid);
    y_f1 = f(grid);
    
    diff = u - y_f1;
    err = max(abs(diff'));
end

function w = chebyshev_weights(n)
    w = zeros(n,1);

    w(1) = 1/2;
    w(2:n-1) = -(-1).^(2:n-1);
    w(n) = -(1/2)*((-1)^n);
end

function x = cal_chebyshev_x(i,n)
    x = cos((i.*pi)./n);
end

function x = cal_x(i, n)
    x = -1 + ((2*i)/n);
end

function y = f1(x)
    y = 1 ./ (5-4.*x);
end

function y = f2(x)
    y = 1 ./ (1 + 16.*(x.^2));
end

function y = f3(x)
    y = cos((10^4).*(x));
end
