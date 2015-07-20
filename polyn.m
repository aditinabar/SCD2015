function y = polyn(A, x);

for i = 1:length(A)
  y = sum(A(i)*x^(i-1));
end

