function [s,t] = secantstep(f,a,b);

% f = @x.^2 - 3(x) + 2;

A = f(a);
B = f(b);

s = a;
t = b;

if A*B >= 0
   disp "No change of sign. Original interval is:";
   return
end

c = (a*B-b*A)/(B-A);
C = f(c);

if A*C > 0 
  s = c; t = b;
  
elseif A*C == 0 
  s = c; t = c;

else 
  s = a; t = c;
  
end
%disp "To iterate secant, define h, where" 
%disp "h is how close to 0 you want to approximate."
end

