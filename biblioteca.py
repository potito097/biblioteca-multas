"""Funciones para calcular multas por retraso en préstamos de biblioteca."""


def validar_dias_retraso(dias_retraso: int) -> None:
    """Valida que los días de retraso no sean negativos."""
    if dias_retraso < 0:
        raise ValueError("Los días de retraso no pueden ser negativos.")


def validar_tarifa_diaria(tarifa_diaria: float) -> None:
    """Valida que la tarifa diaria no sea negativa."""
    if tarifa_diaria < 0:
        raise ValueError("La tarifa diaria no puede ser negativa.")


def calcular_multa(dias_retraso: int, tarifa_diaria: float) -> float:
    """Calcula la multa total por retraso en la devolución de un libro."""
    validar_dias_retraso(dias_retraso)
    validar_tarifa_diaria(tarifa_diaria)
    return dias_retraso * tarifa_diaria
