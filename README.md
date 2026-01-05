# Posición de una partícula en Movimiento Armónico Simple (MAS)

Este repositorio contiene una función simple escrita en Python que calcula las posiciones de una partícula que realiza Movimiento Armónico Simple a lo largo del tiempo, utilizando una discretización temporal.

La idea principal es mostrar cómo modelar un sistema físico continuo usando pasos de tiempo discretos.

---

## Idea física

En el Movimiento Armónico Simple, la posición de la partícula está dada por:

$$
x(t) = A \cos(\omega t + \phi)
$$

El intervalo temporal se discretiza en pasos de tamaño $\Delta t$. La simulación evalúa la posición de la partícula en cada uno de esos instantes.

---

## Que hace la función

* Parte desde un tiempo inicial $t = 0$
* Avanza en pasos regulares de tamaño $\Delta t$
* Calcula la posición de la partícula en cada instante
* Devuelve una lista con las posiciones de la partícula evaluadas desde $t=0$ hasta un tiempo final $t_{final}$.

---

## Parámetros

La función recibe:

* `t_final`: tiempo físico máximo de la simulación
* `a`: amplitud del movimiento
* `w`: frecuencia angular $\omega$
* `phi`: fase inicial $\phi$
* `delta_t`: paso temporal $\Delta t$

---

## Salida

* Una lista de números reales que representan la posición de la partícula en los distintos instantes:

$$
t_i = i \cdot \Delta t \quad \text{con } i = 0, 1, 2, ...
$$

Cada elemento de la lista corresponde a la posición en uno de esos tiempos.

Es importante remarcar que:

* El bucle no recorre el tiempo directamente
* El bucle recorre índices enteros
* El tiempo físico se construye a partir del índice y del paso temporal

---
## Ejemplo:
* input:

`print(posicion_mas(t_final=10 , a=5 , w=math.pi , phi=0, delta_t=3/2))`

* output:

`[5.0, 0, -5.0, 0, 5.0, 0, -5.0]`
