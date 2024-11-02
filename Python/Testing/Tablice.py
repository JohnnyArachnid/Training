tablica = [1,2,2,3,4,5,5,6,7,7,7,8]
#tablica.append() - Dodanie elementu do tablicy
#tablica.insert() - Dodanie elementu do tablicy po wskazanym indeksie
#tablica.pop() - Usuniecie elementu wskazanego
#tablica.clear() - Usuniecie wszystkich elementow z tablicy
#tablica.remove() - Usuniecie wskazanego elementu z tablicy o danym stringu
#tablica.index() - Wskazanie indeksu elementu w tablicy
#tablica.sort() - Sortowanie tablicy
#tablica.reverse() - Sortowanie odwrotne tablicy
#tablica_skopiona = tablica.copy() - Skopiowanie tablicy
#50 in tablica - Zmienna bool sprawdzajaca czy 50 nalezy do tablicy
tablica1 = []
for i in range(len(tablica)):
    if tablica.count(tablica[i]) == 1:
        tablica1.append(tablica[i])
print("Tablica przed operacja: ", tablica)
print("Tablica po operacji: ", tablica1)