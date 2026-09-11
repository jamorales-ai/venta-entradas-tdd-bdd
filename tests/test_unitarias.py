import pytest
from venta_entradas.modelos import Evento, SistemaVentas, VentaError

# -------------------------------
# PRUEBAS DE LA CLASE EVENTO
# -------------------------------

def test_evento_inicia_con_aforo_y_precio():
    evento = Evento("Concierto", aforo_maximo=100, precio_entrada=50.0)
    assert evento.nombre == "Concierto"
    assert evento.aforo_maximo == 100
    assert evento.precio_entrada == 50.0
    assert evento.entradas_vendidas == 0
    assert evento.entradas_disponibles == 100

def test_evento_hay_disponibilidad_true_y_false():
    evento = Evento("Teatro", aforo_maximo=10, precio_entrada=25.0)
    assert evento.hay_disponibilidad(5) is True
    evento._entradas_vendidas = 8
    assert evento.hay_disponibilidad(3) is False

# -------------------------------
# PRUEBAS DE SISTEMAVENTAS.REGISTRAR_EVENTO
# -------------------------------

def test_registrar_evento_lo_guarda_en_sistema():
    sistema = SistemaVentas()
    evento = Evento("Cine", 50, 30.0)
    sistema.registrar_evento(evento)
    assert sistema.eventos["Cine"] == evento

# -------------------------------
# PRUEBAS DE SISTEMAVENTAS.VENDER_ENTRADAS
# -------------------------------

def test_vender_entradas_valido_actualiza_aforo():
    sistema = SistemaVentas()
    evento = Evento("Festival", 10, 20.0)
    sistema.registrar_evento(evento)
    total = sistema.vender_entradas("Festival", 2)
    assert total == 40.0
    assert evento.entradas_vendidas == 2
    assert evento.entradas_disponibles == 8

def test_vender_entradas_evento_inexistente_lanza_error():
    sistema = SistemaVentas()
    with pytest.raises(VentaError):
        sistema.vender_entradas("Fantasma", 1)

def test_vender_entradas_cantidad_invalida_lanza_error():
    sistema = SistemaVentas()
    evento = Evento("Partido", 5, 15.0)
    sistema.registrar_evento(evento)
    with pytest.raises(VentaError):
        sistema.vender_entradas("Partido", 0)

def test_vender_entradas_excede_aforo_lanza_error():
    sistema = SistemaVentas()
    evento = Evento("Show", 3, 10.0)
    sistema.registrar_evento(evento)
    sistema.vender_entradas("Show", 3)
    with pytest.raises(VentaError):
        sistema.vender_entradas("Show", 1)

# -------------------------------
# PRUEBAS DE SISTEMAVENTAS.CALCULAR_TOTAL_CON_DESCUENTO
# -------------------------------

def test_calcular_total_con_descuento_valido():
    sistema = SistemaVentas()
    evento = Evento("Festival", 100, 100.0)
    sistema.registrar_evento(evento)
    total = sistema.calcular_total_con_descuento("Festival", 2, 10)
    assert total == 180.0

def test_calcular_total_con_descuento_invalido_lanza_error():
    sistema = SistemaVentas()
    evento = Evento("Festival", 100, 100.0)
    sistema.registrar_evento(evento)
    with pytest.raises(VentaError):
        sistema.calcular_total_con_descuento("Festival", 1, 150)
