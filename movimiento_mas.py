import math

def posicion_mas(t_final,a,w,phi,delta_t):
    lista = []
    n = int(t_final/delta_t) + 1
    for i in range(n):
        t_i = i*delta_t
        x = a * math.cos(w * t_i + phi)
        if abs(x) < 1e-10:
            x = 0
        lista.append(x)
    return lista