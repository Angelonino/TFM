# scripts_figuras

Scripts de Python (matplotlib) que generan las figuras del TFM hechas con Claude.
Salida: PDF vectorial + PNG (300 dpi), fondo transparente, tipografía PT Serif.

## Uso

```
pip install matplotlib numpy
cd scripts_figuras
python linea_tiempo_PLC.py
python comparativa_osi_prime.py
python topologia_red_PRIME.py
python bandas_espectrales_NBPLC.py
```

Las figuras se escriben en `scripts_figuras/salida/` (o en la carpeta indicada en la
variable de entorno `FIG_OUT`). Después se copian a `Memoria_TFM_limpio/Imagenes/`
con el mismo nombre. La fuente se carga de
`Memoria_TFM_limpio/Fuentes/PT-Serif/` (esta carpeta debe estar junto a `TFM/Memoria_TFM_limpio`).

## Ficheros

| Script | Figura | Salida |
|---|---|---|
| `linea_tiempo_PLC.py` | 2.1 Línea temporal de la evolución del PLC | `linea_tiempo_evolucion_PLC` |
| `comparativa_osi_prime.py` | 2.5 Modelo OSI frente a capas de PRIME | `comparativa_OSI_PRIME` |
| `topologia_red_PRIME.py` | 2.6 Topología dinámica de red PRIME | `topologia_red_PRIME` |
| `bandas_espectrales_NBPLC.py` | 2.7 Bandas CENELEC / FCC | `Cenelec_FCC_bands` |
| `common.py` | Utilidades comunes (fuente, paleta, lienzo, guardado) | — |

## Criterio de tamaño de letra

La memoria usa 12 pt y `\textwidth` = 15,5 cm (6,1 in). Cada figura se incluye con
`\includegraphics[width=\textwidth]`, así que el tamaño real de letra en página es
`fontsize × (6,1 in / ancho de la figura en in)`. En `common.py`, `make_fig(ancho_in, xlim, ylim)`
crea un lienzo que ocupa toda la figura y `eff(pt)` devuelve el `fontsize` necesario para
obtener `pt` puntos reales en página. No usar `bbox_inches="tight"` (cambia la escala).

## Notas

- Las figuras de la cadena de valor, tipos de CT y esquema unifilar las rehízo/controla Angelo
  a mano: no hay script aquí.
- Versiones anteriores de los PDF: `Memoria_TFM_limpio/Imagenes/figuras sustituidas/`.
- La línea temporal se reconstruyó desde el PDF anterior (el script original se perdió);
  el fin de la 2ª generación y el inicio de la 3ª están en 2006, coherente con el eje.
