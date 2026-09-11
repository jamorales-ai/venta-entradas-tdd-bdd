# Venta de Entradas - MVP con TDD

Proyecto base para la Actividad 2 (TDD/ATDD/BDD).

## Requisitos

- Python 3.9 o superior
- pip

## Instalacion

```
pip install pytest
```

## Estructura

```
venta_entradas/
    modelos.py        <- codigo a implementar (contiene NotImplementedError)
tests/
    test_aceptacion.py <- pruebas de aceptacion, NO MODIFICAR
    test_unitarias.py  <- aqui escribes tus pruebas unitarias (TDD)
```

## Como trabajar

1. Ejecuta las pruebas de aceptacion para verlas fallar (rojo):

```
pytest tests/test_aceptacion.py -v
```

2. Implementa el codigo en `venta_entradas/modelos.py` paso a paso, escribiendo
   primero tus propias pruebas unitarias en `tests/test_unitarias.py` (ciclo
   TDD: rojo, verde, refactor).

3. Cuando termines, ejecuta todas las pruebas:

```
pytest -v
```

Todas deben pasar en verde.
