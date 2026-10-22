# Decisiones técnicas

## Decisión 1: validar antes de calcular

**Problema:** el código inicial calculaba antes de validar los datos.

**Decisión:** comprobar los valores antes de realizar el cálculo.

**Justificación:** evita continuar con entradas inválidas.

## Decisión 2: separar responsabilidades

**Problema:** la función original validaba, calculaba e imprimía mensajes.

**Decisión:** crear funciones de validación y mantener el cálculo separado.

**Justificación:** el código es más fácil de leer y probar.

## Decisión 3: automatizar las comprobaciones

**Decisión:** usar Pytest para verificar los resultados esperados.

**Justificación:** permite repetir las comprobaciones después de cada cambio.

## Decisión 4: rechazar los valores negativos con ValueError

**Problema:** devolver `None` y mostrar mensajes no cumplía las pruebas.

**Decisión:** lanzar `ValueError` desde las funciones de validación y eliminar
las impresiones y el ejemplo ejecutado al importar el módulo.

**Justificación:** quien usa la función puede gestionar el error y decidir
cómo presentar el resultado.

## Resultados comprobados

- Pylint inicial: 6.36/10; final: 10.00/10, sin desactivar avisos.
- Pytest inicial: dos pruebas correctas y dos fallidas.
- Pytest final: las cuatro pruebas pasan.
- Las salidas completas se conservan en `evidencias`.

La mejora corrige tanto el estilo como el comportamiento ante datos negativos.
Las anotaciones de tipos documentan el uso esperado; no validan tipos al
ejecutar. Se conserva el alcance de la guía: días y tarifas no negativos.
El cálculo usa la multiplicación numérica de Python, sin añadir reglas de
redondeo monetario que el laboratorio no solicita.
