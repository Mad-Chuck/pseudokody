function paczki(dzien_tygodnia)
  a = dzien_tygodnia mod 3
  b = dzien_tygodnia div 2
  liczba_paczek = 0
  for i in 1:dzien_tygodnia
    if a > b
      liczba_paczek = liczba_paczek + (a * i + b)
    else
      liczba_paczek = liczba_paczek + (b * i + a)
    end
    a = liczba_paczek ÷ 3
    b = liczba_paczek % 2
  end
  return liczba_paczek
end
