function y = newtonstep(f,x0);

if my_diff(f, x0) != 0
  y = x0 - (f(x0)/my_diff(f, x0));

end
end

%derivatives


