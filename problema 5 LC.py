# =========================================
# PROBLEMA 5 - HORAS TRABAJADAS
# =========================================

# Función para calcular total y clasificación
def calcular_horas(horas):
    
    total = sum(horas)
    
    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"
    
    return total, clasificacion


# Matriz de recursos
matriz = [
    ["Juan", 8, 8, 8, 8, 8],
    ["Junior", 9, 9, 8, 8, 9],
    ["Nancy", 7, 8, 7, 8, 7],
    ["Alejandra", 10, 9, 8, 9, 10]
]

# Recorrer matriz
for recurso in matriz:
    
    nombre = recurso[0]
    
    horas = recurso[1:]
    
    total, clasificacion = calcular_horas(horas)
    
    print("--------------------------------")
    print("Nombre:", nombre)
    print("Horas trabajadas:", horas)
    print("Total semanal:", total)
    print("Clasificación:", clasificacion)