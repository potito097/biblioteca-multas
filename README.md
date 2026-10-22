# Biblioteca: cálculo de multas

## Descripción

Proyecto de práctica para calcular multas por retraso en la
devolución de libros.

## Reglas

- La multa se calcula multiplicando días de retraso por tarifa diaria.
- Los días de retraso no pueden ser negativos.
- La tarifa diaria no puede ser negativa.

## Requisitos

Python 3 y las dependencias indicadas en `requirements.txt`.

Para revisar Markdown también se necesitan Node.js y npm.

## Instalación en Windows

Desde la carpeta del proyecto, ejecuta en PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
npm.cmd ci
```

Puedes activar el entorno con `.\.venv\Scripts\Activate.ps1`.
Si no lo activas, sustituye `python` en los comandos siguientes por
`.\.venv\Scripts\python.exe`.

## Ejemplo de uso

```python
from biblioteca import calcular_multa

print(calcular_multa(3, 2))  # 6
```

La función devuelve el resultado y genera `ValueError` si recibe valores
negativos. No imprime mensajes ni ejecuta ejemplos al importarse.

## Ejecutar las pruebas

```bash
python -m pytest -v
```

## Revisar el código con Pylint

```bash
python -m pylint biblioteca.py
```

## Validar la documentación

```powershell
npx.cmd markdownlint-cli2 README.md DECISIONS.md
```

## Evidencia del laboratorio

La carpeta `evidencias` conserva las salidas iniciales y finales de Pylint
y Pytest, la validación Markdown y las versiones utilizadas.
El código original está en `evidencias/biblioteca_inicial.txt` para evitar
confundirlo con el módulo final.
