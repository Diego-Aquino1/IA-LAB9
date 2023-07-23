import random

# Lista de números proporcionados
numbers = [5, 7, 2, 13, 4, 15, 9, 4, 6, 1, 3, 10, 4, 10, 8, 20, 18, 15, 20, 12, 6, 12, 13, 14, 10, 6, 21, 25]

# Función para generar un número aleatorio entre -0.5 y 0.5
def random_value():
    # return round(random.uniform(-0.5, 0.5), 3)
    return random.uniform(-0.5, 0.5)

# Aplicar la suma o resta aleatoria a cada número
# result_numbers = [round(num + random_value(), 3) for num in numbers]
result_numbers = [num + random_value() for num in numbers]

# Mostrar los resultados
print("Números originales:", numbers)
print("Números con sumas o restas aleatorias:", result_numbers)