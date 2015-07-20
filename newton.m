function y = newton(f,x0)

for i = 1:500
  y = newtonstep(f,x0);
  x0 = y;
  if abs(f(y)) < 10^(-10)
    disp(["One root of the function is " num2str(y)])
    disp(["    f(" num2str(y) ") = " num2str(f(y))])
    return
end

end

%derivatives


