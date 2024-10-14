numerolibri=float(input("Inserisci il numero di libri: "))
costototale=float(input("Inserisci il costo totale: "))

calcolotasse=costototale*7.5/100
calcolospedizione=2*numerolibri
importototale=costototale+calcolotasse+calcolospedizione

print("L'importo totale e ", importototale)