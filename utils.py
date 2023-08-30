import string
class utils:

    wordsToCount = []

    s = [0,0,0]

    positiveWords = []
    neutralWords = []
    negativeWords = []

    def __init__(self, words, positive, neutral, negative): #Constructor donde se le pasa las palabras que queremos buscar su ocurrencia dentro de los tweets, tambien las positivas, negatiivas y neutras.
        self.wordsToCount = words
        self.positiveWords = positive
        self.neutralWords = neutral
        self.negativeWords = negative

    def clearTweet(self, tweet): #Eliminar signos de puntuación
            tweet = tweet.lower()
            clearedTweet = tweet.translate(str.maketrans('', '', string.punctuation))

            # Dividir el texto en palabras
            words = clearedTweet.split()

            return words

    def initializeW(self): #Inicializa el vector w en 0
        w = []
        counter = 0
        for word in self.wordsToCount:
            w.insert(counter, 0)
            counter = counter + 1
        return w

    def stringsCounter(self, phrase): #Devuelve el vector w siendo 1 si la palabra esta contenida en el tweet, 0 sino.
        w = self.initializeW()
        counter = 0

        words = self.clearTweet(phrase)

        for word in self.wordsToCount:
            for actualWord in words:
                if word == actualWord:
                    if w[counter] == 0:
                        w[counter] = 1
                        counter = counter + 1
        return w


    def classifyTweet(self, phrase):
        words = self.clearTweet(phrase)
        for w in words:
            if w in self.positiveWords:
                self.s[0] = self.s[0] + 1
            if w in self.neutralWords:
                self.s[1] = self.s[1] + 1
            if w in self.negativeWords:
                self.s[2] = self.s[2] + 1
        return self.s