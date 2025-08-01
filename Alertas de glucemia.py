# Alertas de glucemia

lecturas = [110, 95, 85, 70, 190]  # ejemplo de N lecturas
N = len(lecturas)

suma = sum(lecturas)
promedio = suma / N

if promedio > 180:
    print("HIPERGLUCEMIA")
elif promedio < 70:
    print("HIPOGLUCEMIA")
else:
    print("NORMAL")
