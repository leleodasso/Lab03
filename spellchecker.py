import time
import multiDictionary
import spellchecker as sc

md = multiDictionary.MultiDictionary()

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn):
        """
        prende la frase in ingresso, rimuove i caratteri speciali e la rende tutta minuscola
        e mette ciascuna parola in una stringa
        :param txtIn: il testo digitato da correggere
        :return: la lista di parole digitate minuscole e senza caratteri speciali
        """
        # rimuovo caratteri speciali
        sc.replaceChars(txtIn)
        lista_input=txtIn.lower().split(" ")
        return lista_input

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    '''
    prende il testo in ingresso e rimuove tutti i caratteri intrusi
    :param text: il testo da correggere
    :return: il testo senza caratteri speciali
    '''
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text