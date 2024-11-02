tekst = "ZDANIE SLOWO NPYTANIE"
tekst_nowy = ""
flaga = True
for literka in range(len(tekst)):
    if tekst[literka].upper() != "N" or flaga == False:
        tekst_nowy += tekst[literka]
    else:
        flaga = False
print(tekst_nowy)





