import re

mojiretu =  'How I want a drink, alcoholic of course, after the heavy chapters involving quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.'

cleaning_string = re.sub(r'[,.]', '' , mojiretu)
words = cleaning_string.split()
pi = ''
for i in list(map(len,words)):
  pi += str(i)
  print(pi)
