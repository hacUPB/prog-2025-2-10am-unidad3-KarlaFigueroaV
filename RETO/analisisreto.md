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

### Pseudocódigo
```
Inicio
   Leer angulo
   limite = 15
   t = 0
   Mientras Verdadero
       cl = Cl0 + a_deg * angulo
       Si angulo > limite Entonces
           Escribir "¡Pérdida! Ángulo supera el límite"
           Salir
       Si no
           Escribir "Vuelo seguro. cl =", cl
       Fin si
       Escribir "1. Aumentar ángulo, 2. Mantener, 3. Salir"
       Leer opcion
       Si opcion = 1 Entonces
           angulo = angulo + 1
       Si opcion = 3 Entonces
           Salir
       Fin si
       t = t + 1
       Escribir "Tiempo de simulación:", t, "segundos"
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

### Pseudocódigo
```
Inicio
   consumo_ascenso = 5
   consumo_crucero = 3
   consumo_descenso = 2
   reserva_min = 30
   consumo_conservador = 3
   reserva_kg = reserva_min * consumo_conservador
   Leer combustible_inicial
   Leer tiempo_vuelo
   combustible = combustible_inicial
   minuto = 0
   Mientras minuto < tiempo_vuelo
       Escribir "Ingrese fase (1. Ascenso  2. Crucero  3. Descenso)"
       Leer fase
       Si fase = 1 Entonces
           consumo = consumo_ascenso
       Si fase = 2 Entonces
           consumo = consumo_crucero
       Si fase = 3 Entonces
           consumo = consumo_descenso
       Fin si
       combustible = combustible - consumo
       minuto = minuto + 1
       Escribir "Minuto:", minuto, "Combustible restante:", combustible
       Si combustible <= 0 Entonces
           Escribir "Emergencia: combustible agotado"
           Salir
       Fin si
   Fin mientras
   Si combustible >= reserva_kg Entonces
       Escribir "Vuelo completado con reserva"
   Si no
       Escribir "Vuelo completado sin reserva suficiente"
   Fin si
Fin

```


## DECLARACIÓN USO DE IA
Se utilizó la inteligencia artificial únicamente como apoyo para la idealización y selección de las situaciones problemas a realizar en el reto..