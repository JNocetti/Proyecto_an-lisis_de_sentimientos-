from utils import utils

util = utils(['muerte', 'pérdida', 'luto', 'excelente','gran', 'positivo'], ['excelente','gran', 'positivo'] , ['pérdida'], ['muerte', 'luto'])

w = util.stringsCounter('Excelente en su área, su muerte es una enorme pérdida y debería ser luto nacional!!!')

print("Vector w: ")
print(w)


s = util.classifyTweet('Excelente Excelente Excelente Excelente Excelente ExcelenteExcelente ExcelenteExcelente  Excelente Excelente Excelente l!!!')

print("Vector s: ")
print(s)

print("avg de w: ") 
print(util.avg(w))
print("avg de s: ") #Siempre debe ser mayor al avg de w, ya que el vector s tiene 3 elementos y el vector w tiene 6.
print(util.avg(s))
print("Score sentimental:") 
print(util.score(s))   
      

