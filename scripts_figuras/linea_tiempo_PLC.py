# -*- coding: utf-8 -*-
"""Figura 2.1 (fig:linea_tiempo_plc): línea temporal de la evolución del PLC.
v3: dibujada a TAMAÑO REAL de página (1 unidad de datos = 1 pt; ancho =
\\textwidth = 439,2 pt) con letra de 9-10,5 pt, fondo transparente.

Contenido idéntico al de la v2 (fuentes 5764444 y SHARMA2017704). Corrección
al reconstruir: el fin de la banda sólida de la 2ª generación y el inicio de la
3ª se colocan en 2006, coherente con el eje (en la v2 quedaban hacia 2002-03).
"""
import numpy as np
from matplotlib.patches import Circle, PathPatch
from matplotlib.path import Path
from common import *

W, H = 439.2, 636.0
fig, ax, eff, scale = make_fig(W/72, (0, W), (H, 0))   # y hacia abajo
assert abs(scale - 1.0) < 1e-3

C1, C2 = BLUE_LIGHT, ORANGE
C2L = "#f3ad92"
CP, CG, CM = "#1aab78", "#4636a6", "#0e3768"
GREY = "#8a8883"
WB = dict(fc="white", ec="none", pad=1.2)

# ---------------- eje temporal no lineal (año -> x) ----------------
ANCH = [(1920, 28), (1930, 49), (1950, 91), (1980, 150), (2000, 200),
        (2006, 232), (2013, 310), (2014, 332), (2017, 354), (2020, 377),
        (2026, 402)]
def X(y):
    return float(np.interp(y, [a for a, _ in ANCH], [b for _, b in ANCH]))

def T(x, y, s, size=9, color=INK, weight="normal", style="normal", ha="left",
      va="top", ls=1.22, z=6, **kw):
    return ax.text(x, y, s, fontsize=size, color=color, weight=weight,
                   fontstyle=style, ha=ha, va=va, linespacing=ls, zorder=z,
                   **kw)

def bar(x0, x1, y, color, lw=11, z=4):
    ax.plot([x0, x1], [y, y], color=color, lw=lw, solid_capstyle="round",
            zorder=z)

def dot(x, y, color, r=3.6, z=6):
    ax.add_patch(Circle((x, y), r, facecolor=color, edgecolor="white",
                        lw=1.5, zorder=z))

def arrow(x0, x1, y, color):
    ax.annotate("", xy=(x1, y), xytext=(x0, y),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.6,
                                mutation_scale=11, shrinkA=0, shrinkB=0),
                zorder=3)

XR = X(2026) - 7          # borde derecho de los textos alineados a la derecha

# ---------------- leyenda ----------------
LY = 8
ax.plot([8, 30], [LY+5, LY+5], color=INK, lw=2.4, solid_capstyle="round")
T(38, LY, "Banda continua = generación en despliegue activo / desarrollo")
ax.plot([8, 30], [LY+20, LY+20], color=GREY, lw=2.4, ls=(0, (1.6, 1.3)))
T(38, LY+15, "Banda discontinua = parque histórico instalado, sin nuevas unidades*")
arrow(8, 30, LY+35, INK)
T(38, LY+30, "Flecha abierta = tecnología vigente en la actualidad")

# ---------------- posiciones verticales ----------------
Y1, Y2 = 152, 256
YP, YM, YG = 378, 442, 502
Y_AXIS = 562
T_ANT, T1, T2, T3 = 57, 122, 203, 326

# ---------------- guías verticales (detrás) ----------------
for yr, ytop in [(1950, Y1), (1980, Y2), (2006, YP)]:
    ax.plot([X(yr), X(yr)], [ytop, Y_AXIS], color=GRID, lw=0.9,
            ls=(0, (3, 3)), zorder=1)
ax.plot([X(2026), X(2026)], [T_ANT-6, Y_AXIS], color="#9a9893", lw=0.9,
        ls=(0, (1, 2)), zorder=1)
T(X(2026), T_ANT-8, "Actualidad\n(2026)", weight="bold", ha="center", va="bottom")
for yr, n in [(1950, "1ª"), (1980, "2ª"), (2006, "3ª")]:
    T(X(yr), Y_AXIS-6, f"Inicio {n} gen.", style="italic", color=SECINK,
      ha="center", va="bottom", bbox=WB, z=7)

# ---------------- antecedentes ----------------
T(8, T_ANT, "Antecedentes (UNB-PLC)", size=9.5, color=GREY, style="italic",
  weight="bold")
ya = 87
ax.plot([X(1922), X(1930)], [ya, ya], color=GREY, lw=1.8, ls=(0, (1.2, 1.2)),
        zorder=3)
for yr in (1922, 1930):
    ax.add_patch(Circle((X(yr), ya), 3.8, color=GREY, zorder=5))
T(8, ya+8, "1922 – Telemetría sobre\nAT (15–500 kHz)", style="italic",
  color=SECINK)
T(X(1930)+11, ya, "~1930 – TWACS (UNB-PLC) sobre 60 Hz", style="italic",
  color=SECINK, va="center")

# ---------------- 1ª generación ----------------
T(8, T1, "1ª generación — Control de rizado (ripple control)", size=10.5,
  color=C1, weight="bold", z=7)
bar(X(1950), X(2026), Y1, C1)
arrow(X(2026), W-8, Y1, C1)
dot(X(1950), Y1, C1)
T(X(1950)+3, Y1+11,
  "1950s – Landis & Gyr, Brown Boveri:\ncontrol centralizado de cargas,\npeak shaving (~1 b/s)")
T(XR, Y1+11, "Vigente: en uso diario para\nreparto de cargas en\nnumerosos países europeos", color=C1,
  weight="bold", ha="right")

# ---------------- 2ª generación ----------------
T(8, T2, "2ª generación — Lectura remota (AMR) / CENELEC", size=10.5,
  color=C2, weight="bold", z=7)
bar(X(1980), X(2006), Y2, C2)
ax.plot([X(2006)+6, X(2026)], [Y2, Y2], color=C2L, lw=9,
        ls=(0, (1.5, 0.9)), solid_capstyle="butt", dash_capstyle="round",
        zorder=3)
for yr in (1980, 1991, 2006):
    dot(X(yr), Y2, C2)
T(X(1980)-5, Y2+12, "1980s – Sistemas\nbidireccionales MT/BT;\narquitectura troncal +\nconcentrador MT/BT",
  ha="right")
T(X(1991)+6, Y2+12,
  "1991 – CENELEC EN 50065-1\n(banda A: 3–95 kHz)\nS-FSK (L&G), FSK (ENEL),\nDLMS/COSEM")
T(X(2006)+10, Y2-14, "~2006 – nuevas instalaciones\nmigran a la 3ª generación",
  weight="bold", color=C2, va="bottom")
T(XR, Y2+12, "Parque histórico en\nexplotación* (p. ej. S-FSK\nen Francia, FSK ENEL\nen Italia)",
  style="italic", color=SECINK, ha="right")

# ---------------- 3ª generación ----------------
T(8, T3, "3ª generación — Banda estrecha de alta velocidad (OFDM)",
  size=10.5, color=CM, weight="bold", z=7)
XE = X(2013)
XM = X(2014)
bar(X(2006), XE, YP, CP)
bar(X(2007), XE, YG, CG)
for yr in (2006, 2007, 2011):
    dot(X(yr), YP, CP)
for yr in (2007, 2009):
    dot(X(yr), YG, CG)
for y0 in (YP, YG):
    verts = [(XE, y0), (XM, y0), (XM, YM)]
    ax.add_patch(PathPatch(Path(verts, [Path.MOVETO, Path.CURVE3,
                                        Path.CURVE3]), fc="none", ec=CM,
                           lw=2.4, zorder=3))
bar(XM, X(2026), YM, CM)
arrow(X(2026), W-8, YM, CM)
dot(XM, YM, CM, r=4.4)

# PRIME
T(X(2006)-5, YP-10, "2006 – Consorcio PRIME\n(Iberdrola + fabricantes)", ha="right", va="bottom")
T(X(2007)+4, YP-10, "2007 – Spec.\nPRIME v1.0", va="bottom")
T(X(2011)+4, YP+12, "2011 – >25.000\ncontadores en\ncampo (España)", ha="right")
# estándares (hito de convergencia)
T(XM+11, YP-8, "2013 – IEEE\n1901.2-2013\n2014 – ITU-T G.9903\n(G3-PLC) y G.9904\n(PRIME)", color=CM,
  weight="bold", bbox=WB, z=7)
# G3-PLC
T(X(2007)-5, YG+12, "2007 – Desarrollo G3-PLC\n(Maxim/Sagem, convocatoria ERDF)", ha="right")
T(X(2009)+4, YG+12, "2009 – Pruebas de campo\n(Metering Barcelona)")
T(W-8, YM+13, "Vigente: estándares\ninternacionales\nactuales para\nSmart Grid / AMI", color=CM,
  weight="bold", ha="right", bbox=WB, z=7)

# ---------------- eje inferior ----------------
ax.plot([8, W-8], [Y_AXIS, Y_AXIS], color=INK, lw=1.0, zorder=2)
for yr in [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2006, 2009,
           2011, 2013, 2014, 2017, 2020]:
    ax.plot([X(yr), X(yr)], [Y_AXIS, Y_AXIS+4], color=INK, lw=0.9)
    if yr in (1930, 1940, 1960, 1970, 1990):
        continue
    T(X(yr), Y_AXIS+6, str(yr), size=9, color=SECINK, ha="center")
ax.plot([X(2026)]*2, [Y_AXIS, Y_AXIS+4], color=INK, lw=0.9)
T(X(2026), Y_AXIS+6, "hoy", size=9, weight="bold", ha="center")

T(8, Y_AXIS+22, "Eje temporal no lineal: el tramo 2004-2017 se muestra ampliado para separar\nlos hitos de estandarización.",
  style="italic", color=SECINK)
T(8, Y_AXIS+48, "* Continuidad de la 2ª generación estimada a partir de los grandes parques desplegados\ncitados en la bibliografía; no corresponde a una fecha de cese documentada.",
  style="italic", color=SECINK)

save(fig, "linea_tiempo_evolucion_PLC")
print("done")
