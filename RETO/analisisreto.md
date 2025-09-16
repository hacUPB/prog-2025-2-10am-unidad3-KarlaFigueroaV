## Límite de ángulo de ataque 
Este problema tiene como propósito simular cómo evoluciona el ángulo de ataque de un avión y cómo afecta directamente al coeficiente de sustentación. La idea es que el usuario pueda aumentar, mantener o ingresar un nuevo valor de ángulo en cada paso de la simulación, de modo que se observe la relación lineal entre el ángulo y el coeficiente de sustentación hasta que se supere el límite de 15°, momento en el cual se produce la pérdida y el Cl comienza a disminuir progresivamente. La relevancia de este ejercicio en el ámbito aeronáutico radica en que el ángulo de ataque es uno de los parámetros más importantes para garantizar la seguridad del vuelo, pues un ángulo excesivo provoca la pérdida de sustentación y puede desencadenar un accidente.

Para el desarrollo se asume que la relación entre el coeficiente de sustentación y el ángulo de ataque es estrictamente lineal hasta el límite, y que a partir de ese punto se da un descenso del 
Cl como aproximación al fenómeno de la pérdida. Cada iteración equivale a un segundo de simulación, y el usuario tiene control sobre la evolución del ángulo a través de un menú interactivo. Las variables que intervienen son el ángulo de ataque como entrada principal, el coeficiente de sustentación como variable intermedia y el tiempo como variable de control. Como constantes se definen el límite de 15°, el valor de sustentación inicial de 0.4 y la pendiente de la curva de 0.1 por cada grado.

El flujo del programa está guiado por un bucle infinito que repite el proceso hasta que se decida salir o se alcance la pérdida, y por condicionales que permiten decidir la acción del usuario, además de una validación que detecta el exceso de ángulo. Todo esto se desarrolla dentro de la función limite_angulo(), que integra los cálculos, las decisiones y la interacción con el usuario.

#### Tabla de variables y constantes
| Nombre | Tipo | Descripción |
|--------|------|-------------|
| angulo | Variable de entrada/control | Ángulo de ataque del avión | 
| limite | Constante | Ángulo máximo seguro antes de pérdida | 
| Cl0 | Constante | Coeficiente de sustentación inicial | 
| a_deg | Constante | Pendiente de la curva de sustentación | 
| cl | Variable de salida | Coeficiente de sustentación resultante |
| t | Variable de control | Tiempo de simulación en segundos |

#### Pseudocódigo
```
Inicio
   Leer angulo
   limite = 15
   Cl0 = 0.4
   a_deg = 0.1
   t = 0
   Mientras Verdadero
       cl = Cl0 + a_deg * angulo
       Escribir "Ángulo actual:", angulo, "Cl:", cl
       Si angulo > limite Entonces
           Escribir "¡Pérdida! Ángulo supera el límite"
           Salir
       Fin si
       Escribir "1. Aumentar, 2. Mantener, 3. Nuevo ángulo, 4. Salir"
       Leer opcion
       Si opcion = 1 Entonces
           angulo = angulo + 1
       Si opcion = 2 Entonces
           Escribir "Manteniendo ángulo"
       Si opcion = 3 Entonces
           Leer nuevo angulo
           angulo = nuevo angulo
       Si opcion = 4 Entonces
           Salir
       Fin si
       t = t + 1
       Escribir "Tiempo de simulación:", t, "segundos"
   Fin mientras
Fin
```

### Fórmula
Cl = Cl0 + a_deg \times angulo



## Peso y balance 
En este caso el propósito es simular cómo se distribuye el peso en una aeronave y cómo afecta al centro de gravedad. El usuario va agregando elementos como pasajeros, carga o combustible, y cada adición modifica tanto el peso total como el momento acumulado, lo que a su vez cambia la posición del centro de gravedad. La simulación es relevante porque mantener el centro de gravedad dentro de los límites establecidos es un requisito indispensable para la seguridad y estabilidad del vuelo.

Para resolver el problema se parte de ciertos supuestos. Se considera que todos los pesos se introducen en kilogramos y que los brazos se miden en metros respecto a un punto de referencia fijo. El modelo no contempla límites máximos de carga ni posiciones negativas de brazo, y la simulación finaliza únicamente cuando el usuario lo decide. Las variables principales son el peso y el brazo de cada elemento agregado, el centro de gravedad como variable intermedia, el número de elementos agregados como variable de control y los límites inferior y superior del rango permitido como constantes de referencia.

El programa se ejecuta dentro de un bucle que permite agregar sucesivos elementos de carga hasta que se decida terminar, mientras que mediante condicionales se evalúa si el centro de gravedad calculado está dentro del rango válido. La función que controla toda la lógica es peso_balance(), que se encarga de solicitar datos, acumular valores, calcular resultados y mostrar el estado de balance de la aeronave.

| Variable        | Clasificación | Descripción                                               |
| --------------- | ------------- | --------------------------------------------------------- |
| masa_nueva    | Entrada       | Peso del elemento agregado (pasajero, carga, combustible) |
| brazo_nuevo   | Entrada       | Brazo correspondiente al elemento agregado                |
| peso_total    | Intermedia    | Suma acumulada del peso total del avión                   |
| momento_total | Intermedia    | Suma acumulada de los momentos (masa × brazo)             |
| cg            | Salida        | Centro de gravedad calculado                              |
| rango_min     | Constante     | Límite inferior permitido para el centro de gravedad      |
| rango_max     | Constante     | Límite superior permitido para el centro de gravedad      |
| estado        | Salida        | Estado del avión: "Balanceado" o "Inestable"              |
| n             | Contador      | Número de elementos agregados                             |

### Fórmulas 
Peso total del avión:

peso_total=peso_total+masa_nueva

Momento total:

momento_total=momento_total+(masa_nueva×brazo_nuevo)

Centro de gravedad (CG):

cg=
peso_total/
momento_total
	​

### Pseudocódigo 
```
Inicio
   peso_total = 0
   momento_total = 0
   limite_inferior = 10
   limite_superior = 20
   n = 0
   Mientras Verdadero
       Escribir "1. Pasajero, 2. Carga, 3. Combustible, 4. Terminar"
       Leer opcion
       Si opcion = 4 Entonces
           Escribir "Simulación finalizada"
           Salir
       Fin si
       Leer masa_nueva
       Leer brazo_nuevo
       peso_total = peso_total + masa_nueva
       momento_total = momento_total + masa_nueva * brazo_nuevo
       cg = momento_total / peso_total
       n = n + 1
       Escribir "Elemento agregado:", n
       Escribir "Peso total:", peso_total
       Escribir "Centro de gravedad:", cg
       Si limite_inferior <= cg <= limite_superior Entonces
           Escribir "Avión balanceado"
       Si no
           Escribir "¡Avión inestable!"
       Fin si
   Fin mientras
Fin
```

## Plan de vuelo con reserva de combustible
El tercer problema consiste en simular el consumo de combustible a lo largo de un vuelo, teniendo en cuenta las fases de ascenso, crucero y descenso, cada una con un consumo característico por minuto. El usuario ingresa el combustible inicial y el tiempo total de vuelo, y luego va seleccionando la fase en cada minuto. El objetivo es verificar si al final del recorrido el combustible restante es suficiente para cubrir la reserva mínima de seguridad, que corresponde a 30 minutos de vuelo adicional a un ritmo de consumo conservador.

Este ejercicio es relevante porque la gestión del combustible es crítica en la planificación real de un vuelo. La simulación incluye ciertos supuestos: se considera que el consumo en cada fase es fijo (5 kg/min en ascenso, 3 en crucero y 2 en descenso), que cada iteración corresponde a un minuto de vuelo y que los datos ingresados siempre son válidos. Además, no se consideran situaciones externas como viento o esperas en el aire. Las variables son el combustible inicial, el tiempo de vuelo, la fase seleccionada y el combustible restante como salida principal, mientras que las constantes incluyen los consumos de cada fase y la cantidad de reserva mínima.

 El programa se apoya en un bucle que avanza minuto a minuto hasta completar el tiempo programado, acompañado de condicionales que seleccionan el consumo correcto según la fase indicada. Toda la lógica está contenida en la función plan_vuelo(), que administra las decisiones, los cálculos y la verificación de seguridad al finalizar la simulación.


#### Tabla de variables y constantes
| Nombre | Tipo | Descripción | Valor inicial |
|--------|------|-------------|---------------|
| combustible_inicial | Variable de entrada | Combustible al inicio | Usuario |
| tiempo_vuelo | Variable de entrada | Duración total del vuelo en minutos | Usuario |
| combustible | Variable de control/salida | Combustible restante | combustible_inicial |
| minuto | Variable de control | Tiempo transcurrido | 0 |
| consumo_ascenso | Constante | Consumo de combustible por minuto en ascenso | 5 |
| consumo_crucero | Constante | Consumo de combustible por minuto en crucero | 3 |
| consumo_descenso | Constante | Consumo de combustible por minuto en descenso | 2 |
| reserva_min | Constante | Minutos mínimos de reserva | 30 |
| consumo_conservador | Constante | Consumo usado para calcular reserva mínima | 3 |
| reserva_kg | Constante | Reserva mínima en kg | 90 |

### Fórmula
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
       Escribir "1. Ascenso, 2. Crucero, 3. Descenso"
       Leer fase
       Si fase = 1 Entonces
           consumo = consumo_ascenso
       Si fase = 2 Entonces
           consumo = consumo_crucero
       Si fase = 3 Entonces
           consumo = consumo_descenso
       Si fase inválida Entonces
           consumo = consumo_crucero
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
       Escribir "Vuelo completado con reserva suficiente"
   Si no
       Escribir "Vuelo completado sin reserva suficiente"
   Fin si
Fin

```


## DECLARACIÓN USO DE IA
Se utilizó asistencia de inteligencia artificial (ChatGPT) únicamente para ayudar en la redacción del análisis y sugerencias de mejora del código. Las ideas conceptuales, el diseño de funciones y la implementación final fueron realizadas por los autores.