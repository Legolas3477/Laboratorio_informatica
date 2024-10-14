s=input("immetti stringa: ")
pos=s.find(" ")  #cerca la posizione dello spazio che separa le parole nella stringa
parola=s[0:pos] #estrae la prima parola e la mette in una variabile
parola2=s[pos+1:]   #estrae la seconda parola e la mette in una variabile
print(parola2 + " " + parola) #concateno le variabili al contrario