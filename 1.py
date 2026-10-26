def solution(A):
    # Convertimos a set para búsquedas O(1) y eliminamos duplicados
    s = set(A)
    
    # El resultado debe ser al menos 1. 
    # En el peor de los casos (array [1, 2, 3]), 
    # la respuesta sería N + 1 (4).
    for i in range(1, len(A) + 2):
        if i not in S:
            return i

X=[1,2,3]
print(solution(X))
print(set(X))