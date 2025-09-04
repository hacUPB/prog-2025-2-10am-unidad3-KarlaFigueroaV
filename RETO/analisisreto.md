## Límite de ángulo de ataque
Este problema consiste en simular lo que pasa cuando el avión aumenta su ángulo de ataque. El usuario empieza con un valor inicial y decide si quiere aumentarlo o mantenerlo. A medida que sube, el coeficiente de sustentación crece, pero si se pasa del ángulo límite (por ejemplo 15°), el avión entra en pérdida y se muestra una alerta. De esta forma se entiende cómo el ángulo de ataque tiene un límite seguro que no se puede superar.


## Peso y balance
Aquí el usuario va agregando peso al avión: pasajeros, carga o combustible. Con cada carga se recalcula el peso total y la posición del centro de gravedad (CG). Si el CG está dentro del rango permitido, el avión está balanceado y puede volar estable. Pero si queda fuera, se muestra una advertencia de que el avión es inestable y existe riesgo de pérdida de control. 

## Plan de vuelo con reserva de combustible
En este caso se simula un vuelo considerando el consumo de combustible. El usuario ingresa la cantidad inicial y el tiempo que durará el vuelo. Luego, minuto a minuto, el programa descuenta combustible según la fase de vuelo (ascenso, crucero o descenso). Al final se revisa si, además de llegar al destino, quedó la reserva mínima (por ejemplo 30 minutos extra). Si la reserva no alcanza, aparece una alerta de emergencia. 