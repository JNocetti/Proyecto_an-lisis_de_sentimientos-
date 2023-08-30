from utils import utils

util = utils(['muerte', 'pérdida', 'luto', 'excelente','gran', 'positivo'], ['excelente','gran', 'positivo'] , ['pérdida'], ['muerte', 'luto'])

w = util.stringsCounter('Excelente en su área, su muerte es una enorme pérdida y debería ser luto nacional!!!')

print("Vector w: ")
for e in w:
    print(e)

s = util.classifyTweet('Excelente en su área, su muerte es una enorme pérdida y debería ser luto nacional!!!')

print("Vector s: ")
for e in s:
    print(e)

print("avg de w: ")
print(util.avg(w))
print("avg de s: ")
print(util.avg(s))
print("Score sentimental:")
print(util.score(s))
      

