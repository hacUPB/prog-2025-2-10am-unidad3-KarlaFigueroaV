## Límite de ángulo de ataque 
Este problema consiste en simular lo que pasa cuando el avión aumenta su ángulo de ataque. El usuario empieza con un valor inicial y decide si quiere aumentarlo o mantenerlo. A medida que sube, el coeficiente de sustentación crece, pero si se pasa del ángulo límite (por ejemplo 15°), el avión entra en pérdida y se muestra una alerta. De esta forma se entiende cómo el ángulo de ataque tiene un límite seguro que no se puede superar.

| Variable | Tipo                 | Descripción                                     |
| -------- | -------------------- | ----------------------------------------------- |
| angulo | Entrada / Intermedia | Ángulo actual del avión (°), cambia en el bucle |
| limite | Constante  / control         | Ángulo máximo antes de la pérdida (ej. 15°)     |
| cl     | Intermedia           | Coeficiente de sustentación calculado           |
| estado | Salida               | Estado: “vuelo seguro” o “pérdida”              |
| t      | Contador             | Número de iteración de la simulación            |

Cálculo de coeficiente de sustentación:

cl = Cl0 + adeg * angulo

## Peso y balance
Aquí el usuario va agregando peso al avión: pasajeros, carga o combustible. Con cada carga se recalcula el peso total y la posición del centro de gravedad (CG). Si el CG está dentro del rango permitido, el avión está balanceado y puede volar estable. Pero si queda fuera, se muestra una advertencia de que el avión es inestable y existe riesgo de pérdida de control. 

| Variable          | Tipo       | Descripción                                          |
| ----------------- | ---------- | ---------------------------------------------------- |
| peso_total      | Intermedia | Masa total acumulada del avión                       |
|momento_total   | Intermedia | Suma de los momentos (masa × brazo)                  |
| cg              | Intermedia | Centro de gravedad calculado                         |
| limite_inferior | Constante  | Límite inferior del CG                               |
| limite_superior | Constante  | Límite superior del CG                               |
| estado          | Salida     | Estado: “balanceado” o “inestable”                   |
| opcion          | Entrada    | Tipo de carga añadida (pasajero, carga, combustible) |
| n | Contador | Cuenta la cantidad de elementos agregadpos al avion|

Se utilizara:

peso_total = peso_total + masa_nueva
momento_total = momento_total + (masa_nueva \ brazo_nuevo)
cg = momento_total / peso_total

### Pseudocódigo
```
Inicio
   peso_total = 0
   momento_total = 0
   limite_inferior = 10
   limite_superior = 20
   n = 0
   Mientras Verdadero
       Escribir "1. Pasajero  2. Carga  3. Combustible  4. Terminar"
       Leer opcion
       Si opcion = 4 Entonces
           Salir
       Fin si
       Leer masa_nueva
       Leer brazo_nuevo
       peso_total = peso_total + masa_nueva
       momento_total = momento_total + (masa_nueva * brazo_nuevo)
       cg = momento_total / peso_total
       n = n + 1
       Escribir "Elemento agregado número:", n
       Escribir "Peso total:", peso_total
       Escribir "Centro de gravedad:", cg
       Si cg >= limite_inferior Y cg <= limite_superior Entonces
           Escribir "Avión balanceado"
       Si no
           Escribir "Avión inestable"
       Fin si
   Fin mientras
Fin
```

## Plan de vuelo con reserva de combustible
En este caso se simula un vuelo considerando el consumo de combustible. El usuario ingresa la cantidad inicial y el tiempo que durará el vuelo. Luego, minuto a minuto, el programa descuenta combustible según la fase de vuelo (ascenso, crucero o descenso). Al final se revisa si, además de llegar al destino, quedó la reserva mínima (por ejemplo 30 minutos extra). Si la reserva no alcanza, aparece una alerta de emergencia. 

| Variable              | Tipo       | Descripción                                         |
| --------------------- | ---------- | --------------------------------------------------- |
| combustible_inicial | Entrada    | Combustible cargado al inicio                       |
| combustible         | Intermedia | Combustible restante en la simulación               |
| tiempo_vuelo        | Entrada    | Duración estimada del vuelo (min)                   |
| reserva_min         | Constante  | Reserva mínima en minutos (ej. 30 min)              |
| reserva_kg          | Intermedia | Reserva convertida a kg                             |
| fase                | Entrada    | Fase del vuelo (ascenso, crucero, descenso)         |
| consumo             | Intermedia | Consumo de combustible por minuto según la fase     |
| minuto              | Contador   | Minuto actual en la simulación                      |
| estado              | Salida     | Estado: “con reserva”, “sin reserva” o “emergencia” |

Se utilizará
combustible = combustible - consumo
reserva_kg = reserva_min * consumo_conservador



## DECLARACIÓN USO DE IA
Se utilizó la inteligencia artificial únicamente como apoyo para la idealización y selección de las situaciones problemas a realizar en el reto..