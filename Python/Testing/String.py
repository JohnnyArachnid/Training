tekst = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s 
with the release of Letraset sheets containing Lorem Ipsum passages, a
nd more recently with desktop publishing software like Aldus Pag
eMaker including versions of Lorem Ipsum.'''
# tekst to string z ktory uwzlgednia entery i wciecia nie usuwa ich, dodatkowo zawarcie tekstu w ''' ''' sprawia ze mozemy wewnatrz uzywac "" oraz '' bez zadnych problemow z kodem, najbezpieczniejsza forma deklaracji stringow
zdanie = '''Dzisiaj jest ladna pogoda'''
#print(zdanie[4].upper()) - Wypisanie zwiekszonej literki
#print('disa' in zdanie) - Wypisze True, bo slowo disa znajduje sie w stringu zdanie, w przypadku bledu wypisze false np. print('Disa' in zdanie)
#print(zdanie.replace('a', 'ABC')) - Podmiana wszystkich literek a w stringu na KYS i wypisanie zamienionego tekstu
#print(zdanie.replace('jest', 'Kochac')) - Wypisanie zamienionego tekstu z podanego slowa na podane po przecinku, w przypadku nie napotkania slowa/literki do zamienienia wypisze oryginalny tekst
#print(zdanie.find('d')) - Wypisanie pierwszego napotkanego indeksu litery w stringu od lewej, w przypadku bledu -1
#print(zdanie.find("disa")) - Wypisanie pierwszego napotkanego indeksu slowa w stringu od lewej, w przypadku bledu -1
#zdanie.upper() - Zmiana wszystkich lister na duze
#zdanie.lower() - Zmiana wszystkich lister na male
#print(len(zdanie)) - Wypisaine dlugosci stringa
#print(zdanie[::-1]) - Wypisanie stringa zdanie od tylu
#print(zdanie[1:5]) - Wypisanie stringa od pierwszej literki do piatej literki bez niej
#printf(zdanie[:])- Wypisanie calego tekstu
#print(zdanie[-2] - Wypisanie literki n, drugiej od końca
#zdanie.split(SEPARATOR) - Podzieli tekst na tablice wzgledem separatora
imie = 'Jan'
nazwisko = 'Kowalski'
wiadomosc1 = imie + ' ['+nazwisko+'] jest programista' #konkatenacja stringow w celu otrzymania porzadanego rezultatu
wiadomosc2 = f'{imie} [{nazwisko} jest programista' #formating string, taki sam rezultat co pyzej f'', taka konstrukcja

