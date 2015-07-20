function iteratesecant(f,s,t,h)
%h = 10^-6

d = t-s;
i = 0;

while((d > h) & (i <= 100))
  [s_1, t_1] = secantstep(f, s, t);
  i = i + 1;
  d = t_1 - s_1;
  s = s_1; t = t_1;

end
i
s
t
end
return