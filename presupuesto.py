"""Calcula el importe final de un pedido con descuento, IVA y gastos de envío.

Módulo 0485 Programación
UD 2 - Práctica D3
Autor: Pau García Blasco
Fecha: 15/10/2026
"""

# 1. Bibliotecas
# No se requieren bibliotecas externas para este programa.

# 2. Constantes
IVA_GENERAL = 0.21
ENVIO = 4.95
UMBRAL_ENVIO_GRATIS = 50.0


# 3. Funciones
def calcular_presupuesto(precio, unidades, porcentaje_dto):
    """Calcula el desglose completo del pedido aplicando el descuento a la base.

    Devuelve el subtotal inicial, el ahorro obtenido, la base imponible
    tras el descuento, la cuota de IVA, el coste de envío y el total final.
    """
    subtotal = precio * unidades
    ahorro = subtotal * (porcentaje_dto / 100)
    base = subtotal - ahorro
    iva = base * IVA_GENERAL
    envio = 0.0 if base >= UMBRAL_ENVIO_GRATIS else ENVIO
    total = base + iva + envio
    return subtotal, ahorro, base, iva, envio, total


# 4. Programa principal
def main():
    """Pide los datos del pedido por teclado y muestra el presupuesto alineado."""
    # Entradas (con conversión explícita en la misma línea de lectura)
    articulo = input("Artículo: ")
    precio = float(input("Precio unitario sin IVA (€): "))
    unidades = int(input("Unidades: "))
    porcentaje_dto = float(input("Descuento (%): "))

    # Proceso
    subtotal, ahorro, base, iva, envio, total = calcular_presupuesto(
        precio, unidades, porcentaje_dto
    )

    # Salidas alineadas a 8 caracteres de ancho y 2 decimales (8.2f)
    print(f"\nPresupuesto de {unidades} x {articulo} (Dto. {porcentaje_dto:.0f}%)")
    print(f"  Subtotal:       {subtotal:8.2f} €")
    print(f"  Ahorro (dto.):  {ahorro:8.2f} €")
    print(f"  Base imponible: {base:8.2f} €")
    print(f"  IVA (21%):      {iva:8.2f} €")
    print(f"  Envío:          {envio:8.2f} €")
    print(f"  TOTAL:          {total:8.2f} €")


if __name__ == "__main__":
    main()