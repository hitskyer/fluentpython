symbols = '$徐兴军'
#t = tuple(ord(symbol) for symbol in symbols)
t = (ord(symbol) for symbol in symbols)
print(t)
import array
a = array.array('I', (ord(symbol) for symbol in symbols))
print(a)
