class Evento:
    """Representa un evento con un aforo máximo de entradas."""

    def __init__(self, nombre: str, aforo_maximo: int, precio_entrada: float):
        self.nombre = nombre
        self.aforo_maximo = aforo_maximo
        self.precio_entrada = precio_entrada
        self._entradas_vendidas = 0  # Encapsulado para evitar modificaciones externas

    @property
    def entradas_vendidas(self) -> int:
        """Número de entradas vendidas hasta el momento."""
        return self._entradas_vendidas

    @property
    def entradas_disponibles(self) -> int:
        """Entradas disponibles (aforo - vendidas)."""
        return self.aforo_maximo - self._entradas_vendidas

    def hay_disponibilidad(self, cantidad: int) -> bool:
        """Verifica si se pueden vender 'cantidad' entradas más."""
        return cantidad > 0 and (self._entradas_vendidas + cantidad) <= self.aforo_maximo

    def registrar_venta(self, cantidad: int) -> None:
        """Registra la venta de entradas, asumiendo que ya fue validada."""
        self._entradas_vendidas += cantidad


class VentaError(Exception):
    """Excepción que se lanza cuando una venta no se puede realizar."""
    pass


class SistemaVentas:
    """Gestiona la venta de entradas para uno o varios eventos."""

    def __init__(self):
        self.eventos: dict[str, Evento] = {}

    def registrar_evento(self, evento: Evento) -> None:
        """Agrega un evento nuevo al sistema."""
        self.eventos[evento.nombre] = evento

    def obtener_evento(self, nombre_evento: str) -> Evento:
        """Devuelve el evento por nombre o lanza error si no existe."""
        if nombre_evento not in self.eventos:
            raise VentaError("Evento no registrado")
        return self.eventos[nombre_evento]

    def vender_entradas(self, nombre_evento: str, cantidad: int) -> float:
        """Vende 'cantidad' entradas del evento indicado."""
        evento = self.obtener_evento(nombre_evento)
        if cantidad <= 0:
            raise VentaError("Cantidad inválida")
        if not evento.hay_disponibilidad(cantidad):
            raise VentaError("No hay aforo disponible")
        evento.registrar_venta(cantidad)
        return cantidad * evento.precio_entrada

    def calcular_total_con_descuento(
        self, nombre_evento: str, cantidad: int, porcentaje_descuento: float
    ) -> float:
        """Calcula el total con descuento sin registrar la venta."""
        if porcentaje_descuento < 0 or porcentaje_descuento > 100:
            raise VentaError("Porcentaje de descuento inválido")
        evento = self.obtener_evento(nombre_evento)
        descuento = 1 - (porcentaje_descuento / 100)
        return cantidad * evento.precio_entrada * descuento
