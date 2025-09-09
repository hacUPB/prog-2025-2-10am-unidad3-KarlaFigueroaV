## Límite de ángulo de ataque
Este problema consiste en simular lo que pasa cuando el avión aumenta su ángulo de ataque. El usuario empieza con un valor inicial y decide si quiere aumentarlo o mantenerlo. A medida que sube, el coeficiente de sustentación crece, pero si se pasa del ángulo límite (por ejemplo 15°), el avión entra en pérdida y se muestra una alerta. De esta forma se entiende cómo el ángulo de ataque tiene un límite seguro que no se puede superar.


## Peso y balance
Aquí el usuario va agregando peso al avión: pasajeros, carga o combustible. Con cada carga se recalcula el peso total y la posición del centro de gravedad (CG). Si el CG está dentro del rango permitido, el avión está balanceado y puede volar estable. Pero si queda fuera, se muestra una advertencia de que el avión es inestable y existe riesgo de pérdida de control. 

## Plan de vuelo con reserva de combustible
En este caso se simula un vuelo considerando el consumo de combustible. El usuario ingresa la cantidad inicial y el tiempo que durará el vuelo. Luego, minuto a minuto, el programa descuenta combustible según la fase de vuelo (ascenso, crucero o descenso). Al final se revisa si, además de llegar al destino, quedó la reserva mínima (por ejemplo 30 minutos extra). Si la reserva no alcanza, aparece una alerta de emergencia. 


| **Problema**                                    | **Variable**          | **Tipo**             | **Descripción**                                                     |
| ----------------------------------------------- | --------------------- | -------------------- | ------------------------------------------------------------------- |
| **1. Límite de ángulo de ataque**               | Angulo              | Entrada / Intermedia | Ángulo inicial dado por el usuario y luego va cambiando en el bucle |
|                                                 | limite              | Constante            | Ángulo máximo antes de la pérdida (ej. 15°)                         |
|                                                 | cl                  | Intermedia           | Coeficiente de sustentación calculado en cada ciclo                 |
|                                                 | estado              | Salida               | Muestra si el avión está en vuelo seguro o en pérdida               |
|                                                 | t                   | Contador             | Número de iteración (segundos de simulación)                        |
| **2. Peso y balance**                           | peso_total          | Intermedia           | Suma del peso del avión con pasajeros, carga y combustible          |
|                                                 | cg                 | Intermedia           | Centro de gravedad calculado en cada iteración                      |
|                                                 | limite_inferior     | Constante            | Límite mínimo permitido del centro de gravedad                      |
|                                                 | limite_superior     | Constante            | Límite máximo permitido del centro de gravedad                      |
|                                                 | estado              | Salida               | Indica si el avión está balanceado o inestable                      |
|                                                 | opcion              | Entrada              | Elección del usuario (agregar pasajeros, carga, combustible)        |
| **3. Plan de vuelo con reserva de combustible** | combustible_inicial | Entrada              | Combustible que el usuario ingresa al inicio                        |
|                                                 | combustible         | Intermedia           | Combustible restante que se va recalculando en el bucle             |
|                                                 | tiempo_vuelo        | Entrada              | Duración estimada del vuelo en minutos                              |
|                                                 | reserva             | Constante            | Combustible de reserva (ej. 30 minutos)                             |
|                                                 | fase                | Entrada              | Fase de vuelo elegida por el usuario (ascenso, crucero, descenso)   |
|                                                 | consumo             | Intermedia           | Combustible gastado según la fase                                   |
|                                                 | minuto              | Contador             | Marca el tiempo transcurrido en la simulación                       |
|                                                 | estado              | Salida               | Indica si el vuelo terminó seguro o en emergencia                  |