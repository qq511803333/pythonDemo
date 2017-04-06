from collections import defaultdict
def letter(self):
   fre = defaultdict(int)
   for f in self:
       fre[f] += 1
       print(fre)

aaa = ['a','a','b']
letter(aaa)