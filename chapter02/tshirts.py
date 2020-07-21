colors = ['black', 'white']
sizes  = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
print("-------------------------------")
tshirts = []
for color in colors:
	for size in sizes:
		tshirts.append((color, size))
print(tshirts)
print("-------------------------------")
tshirts = ((color, size) for size in sizes 
						 for color in colors)
print(type(tshirts))
print(list(tshirts))
