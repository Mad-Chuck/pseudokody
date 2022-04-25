slowa = [
  't' 'r' 'a' 'p' 'e' 'z';
  'p' 'l' 'a' 'm' 'a';
  's' 'z' 'a' 'f' 'k' 'a';
  's' 'e' 'k' 'u' 'n' 'd' 'a';
  'm' 'o' 'n' 'e' 't' 'a';
  't' 'a' 'b' 'l' 'i' 'c' 'a';
  'p' 'r' 'o' 's' 'z' 'e' 'k';
  'f' 'a' 'k' 's';
  'l' 'a' 's' 'k' 'a';
  's' 'e' 'g' 'r' 'e' 'g' 'a' 't' 'o' 'r';
  'p' 'a' 's' 'j' 'a';
  'g' 'i' 't' 'a' 'r' 'a';
  'g' 'r' 'z' 'y' 'b';
  'r' 'o' 'd' 'z' 'i' 'n' 'a';
  'p' 'i' 'c' 'i' 'e';
  't' 'r' 'a' 'm' 'w' 'a' 'j';
  't' 'o' 'n' 'i' 'k';
  'f' 'a' 's' 'o' 'l' 'k' 'a';
  'i' 'd' 'i' 'o' 't' 'a';
  's' 'u' 'k' 'n' 'i' 'a';
  'k' 'u' 'c' 'h' 'a' 'r' 'z';
  'b' 'e' 't' 'o' 'n';
  'm' 'a' 'p' 'a';
  'l' 'a' 't' 'a' 'w' 'i' 'e' 'c';
  'r' 'e' 'k' 'i' 'n';
  'r' 'z' 'e' 'c' 'z' 'o' 'w' 'n' 'i' 'k';
  'b' 'a' 'n' 'd' 'y' 't' 'a';
  'd' 'z' 'b' 'a' 'n' 'e' 'k';
  'o' 'b' 'r' 'a' 'z';
  'm' 'a' 'g' 'a' 'z' 'y' 'n'
]

aktualnyZnak = ''
innyIndeks = 0

for i in 1:length(slowa):
  slowo = slowa[i]
  for j in 2:length(slowo)
    aktualnyZnak = slowo[j]
    innyIndeks = j

    while innyIndeks > 0 && aktualnyZnak > slowa[[i, innyIndeks - 1]]
      slowo[innyIndeks] = slowo[innyIndeks - 1]
      innyIndeks = innyIndeks - 1
    end

    slowo[innyIndeks] = aktualnyZnak
  end
        
  print(slowo)
end
