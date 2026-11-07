# -*- coding: utf-8 -*-
"""Utilidades comunes de las figuras del Cap. 2 (v3: tamaño real de letra y
fondo transparente).

Criterio de tamaño: la memoria se compone en 12 pt con \\textwidth = 15,5 cm
(= 439,2 pt = 6,1 in). Cada figura se dibuja con un ancho FIG_W_IN y se
incluye a \\textwidth, de modo que el tamaño de letra EFECTIVO en página es
        fontsize_matplotlib * (6.1 / FIG_W_IN).
`eff(pt)` devuelve el fontsize de matplotlib que produce `pt` puntos en página.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

TEXTWIDTH_IN = 15.5 / 2.54  # 6.10 in

_HERE = os.path.dirname(os.path.abspath(__file__))
# PT Serif: tipografía del proyecto (Memoria_TFM_limpio/Fuentes/PT-Serif)
_FONT_DIRS = [os.path.join(_HERE, "..", "Memoria_TFM_limpio", "Fuentes",
                           "PT-Serif") + os.sep,
              os.path.join(_HERE, "fonts") + os.sep, "/tmp/work/fonts/"]
for _f in ["PTSerif-Regular.ttf", "PTSerif-Bold.ttf", "PTSerif-Italic.ttf",
           "PTSerif-BoldItalic.ttf"]:
    for _dir in _FONT_DIRS:
        try:
            fm.fontManager.addfont(_dir + _f)
        except Exception:
            pass
plt.rcParams["font.family"] = "PT Serif"
plt.rcParams["pdf.fonttype"] = 42   # TrueType embebido (texto seleccionable)

BLUE_DARK = "#104281"
BLUE_MID = "#1c5cab"
BLUE_LIGHT = "#2a78d6"
TINT_1, TINT_2, TINT_3 = "#cde2fb", "#b7d3f6", "#9ec5f4"
ORANGE = "#eb6834"
INK, SECINK, GRID = "#0b0b0b", "#52514e", "#e1e0d9"
SHADOW = "#00000014"


def make_fig(fig_w_in, xlim, ylim):
    """Lienzo que rellena la figura por completo (sin recorte tight), con el
    aspecto de los datos igual al de la figura y fondo TRANSPARENTE."""
    x0, x1 = xlim
    y0, y1 = ylim
    h_in = fig_w_in * abs(y1 - y0) / abs(x1 - x0)
    fig = plt.figure(figsize=(fig_w_in, h_in), dpi=200)
    fig.patch.set_alpha(0)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.patch.set_alpha(0)
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
    ax.axis("off")
    scale = TEXTWIDTH_IN / fig_w_in

    def eff(pt):
        return pt / scale

    return fig, ax, eff, scale


# carpeta de salida: variable de entorno FIG_OUT o ./salida junto a los scripts
OUT_DIR = os.environ.get("FIG_OUT", os.path.join(_HERE, "salida"))


def save(fig, name):
    os.makedirs(OUT_DIR, exist_ok=True)
    fig.savefig(os.path.join(OUT_DIR, f"{name}.pdf"), transparent=True,
                pad_inches=0)
    fig.savefig(os.path.join(OUT_DIR, f"{name}.png"), transparent=True,
                pad_inches=0, dpi=300)
