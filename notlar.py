#  0 ile 5 arası p olasılığına göre 3 tane sayı. 
np.random.choice(0, 5, 3, p=[0.1, 0, 0.3, 0.6, 0])

#dizi içinden olasilikla, olasilik toplaminin 1 olduguna dikkat et. 
dizi1 = ['a','b','c','d']
olasilik = [0.2,0.4,0.4,0]
print(np.random.choice(dizi1,4,p=olasilik))

#Constructer ile İç içe sözlük
child = dict(child1=dict(name='hasan',yas=21),child2=dict(name='ebru',yas=25))
print(child, child.keys(), child.get('child1'))

#Decoratorler
#Decoratorleri özellikle loglama, error yakalama ve süre hesabı için kullanmak mantıklı.

#Fonksiyonu parametre haline getirme
#Eğer parametre haline getirdikten sonra değiştirmek veya silmek istersek setter ve deleter kullanılabilir.
class metin():
    @property
    def yaz(self):
        return 'deneme'
kelime = metin()
print(kelime.yaz)

#Einstein-Summation
#numpy.einsum(subscripts, *operands, out=None, dtype=None, order='K', casting='safe', optimize=False)


import numpy as np
np.random.seed(69)

chain = 2*np.random.binomial(1,0.5,size=(2,10,10))-1
chain2= [a         for matrix in chain
                   for k in matrix
                   for a in k]
print(len(chain2))
#rastgele binomial dağılım üretip sonra onun içindeki elemanlara tek tek erişmek,
#ayrıca bu kodla liste içinde for döngüsü kullanımıda örneklendi.


x, y, z = 0, 1, 0

if any((x, y, z)):  #herhangi biri 1 yada true ise 
    print(any((x, y, z)))
    print('passed')
    
##################################################################
#Fonksiyonları liste içine koyup çağırabiliriz.
def l(a):
    print(a,'1')

def p(b):
    print(b,'2')
    
list1 = [l,p]

for i in list1:
    i(3)
    
list1[0](5) #list1 in 0.fonskiyoa bööle erişebiliriz.
###################################################################
def buyut(yazi):
    return (yazi.upper())
    
yeni_liste = list(map(buyut,['test1','test2']))

print(yeni_liste)
###################################################################
