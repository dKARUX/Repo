matrix = [
    ['Frutas', 'Verduras', 'Madera'],
    ['Uva', 'Limon', 'Cedro'],
    ['Fresa', 'Zanahoria', 'Roble'],
    ['Pera', 'Lechuga', 'Parota'],
]

output = []

for i in range(0, len(matrix)):
    for j in range(0,len(matrix[i])):
        print(matrix[i][j], f"[{matrix.index(matrix[i])}][{matrix.index(matrix[j])}]")

print(matrix.index(['Frutas', 'Verduras', 'Madera']))

print(matrix[1][1])

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i]):
        output.append(matrix[i][j])