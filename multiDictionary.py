from operator import index

import dictionary
import richWord as rw

d = dictionary.Dictionary()

class MultiDictionary:

    def __init__(self):
       pass

    def printDic(self, language):
        pass

    def searchWord(self, words, nome_file):
        '''
        riceve la lista di parole digitate dall'utente
        riceve il nome del file da aprire
        a partire dalla lista di parole nel dizionario e dalla lista di parole digitate in input
        confronto le due liste e stabilisce:
        1: se una parola è contenuta nel significa che è sbagliata
        :param words: la lista di parole in input
        :param nome_file: la lingua del dizionario da cui ricavare il nome del file da aprire
        :return: una lista di parole che sono state digitate sbagliate
        '''
        diz=d.loadDictionary(nome_file)
        lista_sbagliate = []
        for word in words:
            if word not in diz:
                lista_sbagliate.append(word)
        return lista_sbagliate

    def searchWordLinear(self, words, nome_file):
        diz = d.loadDictionary(nome_file)
        lista_sbagliate = []
        for word in words:
            flag_trovata = False
            for i in range(0,len(diz)):
                if word==diz[i]:
                    flag_trovata = True
            if not flag_trovata:
                lista_sbagliate.append(word)
        return lista_sbagliate

    def searchWordDichotomic(self, words, nome_file):
        diz = d.loadDictionary(nome_file)
        lista_sbagliate=[]
        for word in words:
            flag_trovata = False
            estremo_inf=0
            estremo_sup=len(diz)-1
            posizione_centrale = estremo_inf + (estremo_sup-estremo_inf)//2
            while estremo_inf<=estremo_sup:
                posizione_centrale = estremo_inf + (estremo_sup - estremo_inf) // 2
                if word == diz[int(posizione_centrale)]:
                    flag_trovata = True
                    break
                elif word < diz[int(posizione_centrale)]:
                    estremo_sup = posizione_centrale - 1
                elif word > diz[int(posizione_centrale)]:
                    estremo_inf = posizione_centrale + 1
            if not flag_trovata:
                lista_sbagliate.append(word)
        return lista_sbagliate






