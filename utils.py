import string
import numpy as np
class utils:

    wordsToCount = []
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
        w = np.zeros(len(self.wordsToCount))
        return w

    def initializeS(self): #Inicializa el vector w en 0
        s = np.zeros(3)
        return s

    def stringsCounter(self, phrase): #Devuelve el vector w donde en cada posicion esta la cantidad de veces que aparece la palabra en el tweet.
        w = self.initializeW()
        words = self.clearTweet(phrase)
        for actualWord in words:
            for i, word in enumerate(self.wordsToCount):
                if word == actualWord:
                    w[i] += 1

        return w
 

    def classifyTweet(self, phrase):
        words = self.clearTweet(phrase)
        s = self.initializeS()
        for w in words:
            if w in self.positiveWords:
                s[0] = s[0] + 1
            elif w in self.neutralWords:
                s[1] = s[1] + 1
            elif w in self.negativeWords:
                s[2] = s[2] + 1
        return s

    def getAvgTweet(self, r):
        if 0.5 < r <= 1:
            return  "El tweet tiene una calidad media -->"
        elif r > 1:
            return "El tweet tiene una calidad buena -->"
        else: # r < (0.5)
            return "El tweet tiene una calidad mala -->"

    def avg(self, w):
        n =  len(w)
        alpha = (1 / n)
        r =  alpha * sum(w)

        if 0.5 < r <= 1:
            return r
        elif r > 1:
            return r
        else: # r < (0.5)
            return r

    def score(self, s):
        v = np.array([1,0,-1]) 
        score = s@v
        if score > 0:
            return f"El tweet es positivo --> {score}"
        elif score == 0:
            return f"El tweet es neutral --> {score}"
        else:
            return f"El tweet es negativo --> {score}"

    
