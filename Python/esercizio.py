#inizializza una stringa, stampa i primi 3 caratteri, seguiti da tre punti il resto della stringa

s= input(("Inserisci una stringa: "))
risultato= s[:3] + "..." + s[3:]        #per estrarre in python i caratteri da una stringa si usa la notazione s[da:a] dove da e a sono gli indici di inizio e fine
print(risultato)
