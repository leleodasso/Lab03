import time
import spellchecker
import multiDictionary

md = multiDictionary.MultiDictionary()
sc = spellchecker.SpellChecker()


while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()

        #creo una lista di elementi che contiene le parole digitate e creo una lista di elementi del dizionario
        lista_parole_input=sc.handleSentence(txtIn)
        inizio_timer = time.time()
        lista_parole_sbagliate=md.searchWord(lista_parole_input,"resources/Italian.txt")
        fine_timer = time.time()
        valore_timer = fine_timer - inizio_timer
        print("-----------------------------------------------")
        print("Using contains")
        for p in lista_parole_sbagliate:
            print(p)
        print("Time elapsed: " + str(valore_timer))


        #metodo con linear search
        inizio_timer = time.time()
        lista_parole_sbagliate = md.searchWordLinear(lista_parole_input, "resources/Italian.txt")
        fine_timer = time.time()
        valore_timer = fine_timer - inizio_timer
        print("-----------------------------------------------")
        print("Using Linear search")
        for p in lista_parole_sbagliate:
            print(p)
        print("Time elapsed: " + str(valore_timer))

        #metodo con dichotomic search
        inizio_timer = time.time()
        lista_parole_sbagliate = md.searchWordDichotomic(lista_parole_input, "resources/Italian.txt")
        fine_timer = time.time()
        valore_timer = fine_timer - inizio_timer
        print("-----------------------------------------------")
        print("Using Dichotomic search")
        for p in lista_parole_sbagliate:
            print(p)
        print("Time elapsed: " + str(valore_timer))
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        # creo una lista di elementi che contiene le parole digitate e creo una lista di elementi del dizionario
        lista_parole_input = sc.handleSentence(txtIn)

        #metodo con contains
        inizio_timer = time.time()
        lista_parole_sbagliate = md.searchWord(lista_parole_input, "resources/English.txt")
        fine_timer = time.time()
        valore_timer = fine_timer - inizio_timer
        print("-----------------------------------------------")
        print("Using contains")
        for p in lista_parole_sbagliate:
            print(p)
        print("Time elapsed: " + str(valore_timer))

        #metodo con linear search
        inizio_timer = time.time()
        lista_parole_sbagliate = md.searchWordLinear(lista_parole_input, "resources/English.txt")
        fine_timer = time.time()
        valore_timer = fine_timer - inizio_timer
        print("-----------------------------------------------")
        print("Using Linear search")
        for p in lista_parole_sbagliate:
            print(p)
        print("Time elapsed: " + str(valore_timer))

        # metodo con dichotomic search
        inizio_timer = time.time()
        lista_parole_sbagliate = md.searchWordDichotomic(lista_parole_input, "resources/English.txt")
        fine_timer = time.time()
        valore_timer = fine_timer - inizio_timer
        print("-----------------------------------------------")
        print("Using Dichotomic search")
        for p in lista_parole_sbagliate:
            print(p)
        print("Time elapsed: " + str(valore_timer))
        continue



    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        sc.handleSentence(txtIn,"Spanish")
        continue

    if int(txtIn) == 4:
        break


