s = ["T","R","Z","E", "P", "A", "K"]  #szyfrowana wiadomość
n = length(s)

for i in n:-1:1
  if i % 2 == 0
    a = s[i]
    s[i] = s[i ÷ 2]
    s[i ÷ 2] = a
  else
    a = s[i]
    s[i] = s[i % 2]
    s[i % 2] = a
  end

  print(s)
  print("\n")
end

print(s)
exit(0)
