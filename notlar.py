#  0 ile 5 arası p olasılığına göre 3 tane sayı. 
np.random.choice(0, 5, 3, p=[0.1, 0, 0.3, 0.6, 0])

#dizi içinden olasilikla, olasilik toplaminin 1 olduguna dikkat et. 
dizi1 = ['a','b','c','d']
olasilik = [0.2,0.4,0.4,0]
print(np.random.choice(dizi1,4,p=olasilik))

#Constructer ile İç içe sözlük
child = dict(child1=dict(name='hasan',yas=21),child2=dict(name='ebru',yas=25))
print(child, child.keys(), child.get('child1'))

#Decoratorleri özellikle loglama, error yakalama ve süre hesabı için kullanmak mantıklı.

#Einstein-Summation
#numpy.einsum(subscripts, *operands, out=None, dtype=None, order='K', casting='safe', optimize=False)
