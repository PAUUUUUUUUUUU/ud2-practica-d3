# Práctica D3: Calculadora de presupuestos

* **Módulo:** 0485 Programación (1.º CFGS DAW)
* **Unidad Didáctica:** UD 2 - Primeros pasos con Python
* **Autor:** Pau García Blasco

## Descripción de las mejoras implementadas

Ampliación del programa `presupuesto.py` (apartado 10.4) con las siguientes características:
1. **Aplicación de descuento sobre la base:** Solicita por teclado un porcentaje de descuento (`float`) y lo descuenta del subtotal antes de calcular el IVA y el umbral de envío.
2. **Cálculo y visualización del ahorro:** Muestra en una línea específica la cantidad exacta ahorrada en euros.
3. **Alineación con formato `:8.2f`:** Todos los importes se muestran alineados a la derecha con un ancho de 8 caracteres y 2 decimales fijos.
4. **Uso de constantes:** Se emplean `IVA_GENERAL = 0.21`, `ENVIO = 4.95` y `UMBRAL_ENVIO_GRATIS = 50.0`.

## Comprobación con tres pedidos distintos

| Pedido | Artículo | Precio (`€`) | Ud. | Dto. (`%`) | Subtotal (`€`) | Ahorro (`€`) | Base (`€`) | IVA 21% (`€`) | Envío (`€`) | TOTAL (`€`) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | Ratón inalámbrico | `15.00` | `2` | `10` | `30.00` | `3.00` | `27.00` | `5.67` | `4.95` | **`37.62`** |
| **2** | Teclado mecánico | `55.00` | `1` | `20` | `55.00` | `11.00` | `44.00` | `9.24` | `4.95` | **`58.19`** |
| **3** | Monitor 24 pulgadas | `120.00` | `2` | `15` | `240.00` | `36.00` | `204.00` | `42.84` | `0.00` | **`246.84`** |

## Ejecución

```bash
python3 presupuesto.py
```