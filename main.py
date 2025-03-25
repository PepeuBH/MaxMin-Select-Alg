def maxMin(array, menor, maior):
    class Pair:
        def __init__(self):
            self.max = 0 # declara máximo do vetor
            self.min = 0 # declara mínimo do vetor
    result = Pair()

    if menor == maior: # significa que o array só tem 1 número
        result.max = array[menor]
        result.min = array[menor]
        return result
    
    if maior == menor + 1:
        if array[menor] < array[maior]:
            result.min = array[menor]
            result.max = array[maior]
        else:
            result.min = array[maior]
            result.max = array[menor]
        return result

    meio = (menor + maior) // 2 # acha o meio do vetor

    left = maxMin(array, menor, meio) # a recursão aqui ó céloko

    right = maxMin(array, meio + 1, maior) # a recursão aqui ó céloko

    result.max = max(left.max, right.max)

    result.min = min(left.min, right.min)
    return result

array = [17, 14, 26, 89, 13, 10, 4] # array de teste, pode mudar eu deixo

result = maxMin(array, 0, len(array) - 1)

print(f"Maior: {result.max}\nMenor: {result.min}")
