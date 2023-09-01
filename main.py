from utils import utils

words = ['mas', 'feliz', 'gusto', 'session', 'odio', 'problema', 'peores', 'peor', 'temazo', 'adictivo']
positives_words = ['mas','temazo',  'feliz', 'gusto', 'adictivo']
neutral_words = ['session']
negative_words = ['odio', 'problema', 'peores', 'peor']



feelings_calculator = utils(words, positives_words, neutral_words, negative_words)

tw1= "Probablemente de las peores canciones serias que he escuchado y la peor bzrp session de la historia, Peso Pluma en una bzrp session no iba a acabar bien"
w1 = feelings_calculator.stringsCounter(tw1)
s1 = feelings_calculator.classifyTweet(tw1)
avg_w1 = feelings_calculator.avg(w1)
avg_s1 = feelings_calculator.avg(s1)
score_s1 = feelings_calculator.score(s1)

spliter = "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------"

print("\n", spliter , "\n", "Tweet 1:" , tw1, "\n" , "Vector w: ", w1, "\n" , "Vector s: ", s1, "\n" , "avg(w): ", feelings_calculator.getAvgTweet(avg_w1),avg_w1  , "\n" , "avg(s)", feelings_calculator.getAvgTweet(avg_s1), avg_s1, "\n" , "Score sentimental: ", score_s1 , "\n", spliter )

tw2= "Es una pena que no sea la 17472937462929372929 vez que sea una session de regetón o trap. Cómo se atreve a " \
     "hacer algo diferente? Cómo se atreve a poner instrumentos de verdad y no puro auto tune?"
w2 = feelings_calculator.stringsCounter(tw2)
s2 = feelings_calculator.classifyTweet(tw2)
avg_w2 = feelings_calculator.avg(w2)
avg_s2 = feelings_calculator.avg(s2)
score_s2 = feelings_calculator.score(s2)

print("Tweet 2:" , tw2, "\n" , "Vector w: ", w2, "\n" , "Vector s: ", s2, "\n" , "avg(w): ", feelings_calculator.getAvgTweet(avg_w2), avg_w2 , "\n" , "avg(s)", feelings_calculator.getAvgTweet(avg_s2), avg_s2, "\n" , "Score sentimental: ", score_s2 , "\n", spliter)

tw3= "A mi si me gusto la bzrp session de peso pluma, por que tanto hate?"
w3 = feelings_calculator.stringsCounter(tw3)
s3 = feelings_calculator.classifyTweet(tw3)
avg_w3 = feelings_calculator.avg(w3)
avg_s3 = feelings_calculator.avg(s3)
score_s3 = feelings_calculator.score(s3)

print("Tweet 3:" , tw3, "\n" , "Vector w: ", w3, "\n" , "Vector s: ", s3, "\n" , "avg(w): ", feelings_calculator.getAvgTweet(avg_w3), avg_w3 , "\n" , "avg(s)", feelings_calculator.getAvgTweet(avg_s3), avg_s3, "\n" , "Score sentimental: ", score_s3 , "\n", spliter)

tw4= "Es un temazo y entre más lo escuchas más adictivo es"
w4 = feelings_calculator.stringsCounter(tw4)
s4 = feelings_calculator.classifyTweet(tw4)
avg_w4 = feelings_calculator.avg(w4)
avg_s4 = feelings_calculator.avg(s4)
score_s4 = feelings_calculator.score(s4)

print("Tweet 4:" , tw4, "\n" , "Vector w: ", w4, "\n" , "Vector s: ", s4, "\n" , "avg(w): ", feelings_calculator.getAvgTweet(avg_w4), avg_w4 , "\n" , "avg(s)", feelings_calculator.getAvgTweet(avg_s4), avg_s4, "\n" , "Score sentimental: ", score_s4 , "\n", spliter)


tw5= "¿entonces la bzrp session de peso pluma es una canción normal de peso pluma con un par de arreglos? porque la " \
     "música está grabada con instrumentos reales por la banda y la letra también es de ellos."
w5 = feelings_calculator.stringsCounter(tw5)
s5 = feelings_calculator.classifyTweet(tw5)
avg_w5 = feelings_calculator.avg(w5)
avg_s5 = feelings_calculator.avg(s5)
score_s5 = feelings_calculator.score(s5)

print("Tweet 5:" , tw5, "\n" , "Vector w: ", w5, "\n" , "Vector s: ", s5, "\n" , "avg(w): ", feelings_calculator.getAvgTweet(avg_w5), avg_w5 , "\n" , "avg(s)", feelings_calculator.getAvgTweet(avg_s5), avg_s5, "\n" , "Score sentimental: ", score_s5 , "\n", spliter)


tw6= "Hablan de mi Peso Pluma como si Quevedo tuviera otro tema que no sea su Session de BZRP"
w6 = feelings_calculator.stringsCounter(tw6)
s6 = feelings_calculator.classifyTweet(tw6)
avg_w6 = feelings_calculator.avg(w6)
avg_s6 = feelings_calculator.avg(s6)
score_s6 = feelings_calculator.score(s6)

print("Tweet 6:" , tw6, "\n" , "Vector w: ", w6, "\n" , "Vector s: ", s6, "\n" , "avg(w): ", feelings_calculator.getAvgTweet(avg_w6), avg_w6 , "\n" , "avg(s)", feelings_calculator.getAvgTweet(avg_s6), avg_s6, "\n" , "Score sentimental: ", score_s6 , "\n", spliter)


tw7= "La BZRP Session de Peso Pluma llega a 100M en YouTube en menos de un mes A este paso, la polémica canción se va " \
     "a convertir en una de las más vistas de la historia"
w7 = feelings_calculator.stringsCounter(tw7)
s7 = feelings_calculator.classifyTweet(tw7)
avg_w7 = feelings_calculator.avg(w7)
avg_s7 = feelings_calculator.avg(s7)
score_s7 = feelings_calculator.score(s7)

print("Tweet 7:" , tw7, "\n" , "Vector w: ", w7, "\n" , "Vector s: ", s7, "\n" , "avg(w): ", feelings_calculator.getAvgTweet(avg_w7), avg_w7 , "\n" , "avg(s)", feelings_calculator.getAvgTweet(avg_s7), avg_s7, "\n" , "Score sentimental: ", score_s7 , "\n", spliter)

tw8 = "Bro es que si es famosa en México es seguro que será famosa si somos demasiados, a los que nos gusta nuestra música nacional la apoyamos y ya esta. Independientemente del hete del exterior"
w8 = feelings_calculator.stringsCounter(tw8)
s8 = feelings_calculator.classifyTweet(tw8)
avg_w8 = feelings_calculator.avg(w8)
avg_s8 = feelings_calculator.avg(s8)
score_s8 = feelings_calculator.score(s8)

print("Tweet 8:" , tw8, "\n" , "Vector w: ", w8, "\n" , "Vector s: ", s8, "\n" , "avg(w): ", feelings_calculator.getAvgTweet(avg_w8), avg_w8 , "\n" , "avg(s)", feelings_calculator.getAvgTweet(avg_s8), avg_s8, "\n" , "Score sentimental: ", score_s8 , "\n", spliter)

tw9 = "La bzrp session de Peso Pluma no ha gustado porque es un género muy particular de México al que no estamos acostumbrados. Pero con la sesión de Arcángel dijimos que Biza estaba empezando a ser repetitivo y aquí ha traído algo diferente, no podemos quejarnos en ese sentido."
w9 = feelings_calculator.stringsCounter(tw9)
s9 = feelings_calculator.classifyTweet(tw9)
avg_w9 = feelings_calculator.avg(w9)
avg_s9 = feelings_calculator.avg(s9)
score_s9 = feelings_calculator.score(s9)

print("Tweet 9:" , tw9, "\n" , "Vector w: ", w9, "\n" , "Vector s: ", s9, "\n" , "avg(w): ", feelings_calculator.getAvgTweet(avg_w9), avg_w9 , "\n" , "avg(s)", feelings_calculator.getAvgTweet(avg_s9), avg_s9, "\n" , "Score sentimental: ", score_s9 , "\n", spliter)

tw10 = "Soy española, me encantan los corridos tumbados y me hace muy feliz ver todo lo que está consiguiendo Peso Pluma. Un cantante de 10 que transmite unas vibras increíbles PD: lo llevaba escuchando desde mucho antes de la bzrp session "
w10 = feelings_calculator.stringsCounter(tw10)
s10 = feelings_calculator.classifyTweet(tw10)
avg_w10 = feelings_calculator.avg(w10)
avg_s10 = feelings_calculator.avg(s10)
score_s10 = feelings_calculator.score(s10)

print("Tweet 10:" , tw10, "\n" , "Vector w: ", w10, "\n" , "Vector s: ", s10, "\n" , "avg(w): ", feelings_calculator.getAvgTweet(avg_w10), avg_w10 , "\n" , "avg(s)", feelings_calculator.getAvgTweet(avg_s10), avg_s10, "\n" , "Score sentimental: ", score_s10 , "\n", spliter)

green = "\x1b[32m"
reset = "\x1b[0m"
red = "\x1b[31m"
cian = "\033[;36m"



score_tweets = [score_s1, score_s2,  score_s3, score_s4, score_s5, score_s6, score_s7, score_s8, score_s9, score_s10]
best_score = max(score_tweets)

print(green + "El tweet más positivo es: ", tw4, "\n" "Score: " ,best_score + reset)

worst_score = min(score_tweets)


print(red + "El tweet más negativo es: ", tw1, "\n" "Score: " ,worst_score + reset)


average_tweets = [avg_w1, avg_w2, avg_w3, avg_w4, avg_w5, avg_w6, avg_w7, avg_w8 , avg_w9, avg_w10]
total = 0
for avg_tweet in average_tweets:
     total = total + avg_tweet
total = total / 10

print(cian + "El promedio de calidad de los tweets es de:  ", total)

