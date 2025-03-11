class Dictionary:
    def __init__(self, dizionario = []):
        self.dizionario = dizionario


    def loadDictionary(self,path):
        '''
        apre il file del dizionario di quella lingua e crea una lista
        di nomi presenti nel dizionario. Mette tutto minuscolo
        :param path: il nome del file di dizionario
        :return: la lista con ciascuna parola per ogni elemento
        '''
        with open(path,'r') as file:
            for line in file:
                self.dizionario.append(line.strip().lower())
        return self.dizionario


    def printAll(self):
        print(self.dizionario)


    @property
    def dict(self):
        return self._dict

