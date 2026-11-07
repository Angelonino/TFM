# -*- coding: utf-8 -*-
"""Figura 2.7 (fig:Cenelec_FCC_bands): asignación de bandas NB-PLC según
CENELEC (EN 50065-1) y FCC (47 CFR Parte 15 / IEEE 1901.2).
v3: letra de 9-12,5 pt EFECTIVOS en página, fondo transparente (sin tarjeta
gris). Cifras idénticas a la prosa de Angelo en subsec:marcos_espectrales:
  CENELEC 3-148,5 kHz; A 9-95 (exclusiva DSO), B 95-125, C 125-140,
  D 140-148,5 (consumidor); FCC 9-490 kHz; IEEE 1901.2-2013 < 500 kHz.
El tramo 3-9 kHz no tiene sub-banda con nombre: se dibuja en gris neutro."""
import textwrap
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle
from common import *

FIG_W = 7.6
fig, ax, eff, scale = make_fig(FIG_W, (0, 13.0), (0.0, 10.35))
UNASSIGNED = "#c9c7c0"

def rbox(x0, x1, y0, y1, fc, ec, lw=1.6, rounding=0.09, zorder=3, shadow=True):
    if shadow:
        ax.add_patch(FancyBboxPatch((x0, y0-0.045), x1-x0, y1-y0,
                     boxstyle=f"round,pad=0,rounding_size={rounding}",
                     facecolor=SHADOW, edgecolor="none", zorder=zorder-0.5))
    ax.add_patch(FancyBboxPatch((x0, y0), x1-x0, y1-y0,
                 boxstyle=f"round,pad=0,rounding_size={rounding}",
                 facecolor=fc, edgecolor=ec, lw=lw, zorder=zorder))

def label(x, y, text, size=11, color=INK, weight="normal", ha="center",
          va="center", style="normal", zorder=6, ls=1.2):
    ax.text(x, y, text, ha=ha, va=va, fontsize=eff(size), color=color,
            weight=weight, fontstyle=style, zorder=zorder, linespacing=ls)

def badge(x, y, text, fc, r=0.25, zorder=7):
    ax.add_patch(Circle((x, y), r, facecolor=fc, edgecolor="white", lw=1.3,
                 zorder=zorder))
    ax.text(x, y-0.005, text, ha="center", va="center", fontsize=eff(10),
            color="white", weight="bold", zorder=zorder+0.1)

# eje de frecuencia no lineal por tramos (kHz -> x)
ANCH_F = [3, 9, 95, 125, 140, 148.5, 150, 490]
X_END = 11.85
ANCH_X = [0.70, 1.25, 4.40, 6.00, 7.00, 7.65, 7.75, X_END]
def warp(f):
    return float(np.interp(f, ANCH_F, ANCH_X))

CEN_TOTAL, CEN_A = (3, 148.5), (9, 95)
CEN_B, CEN_C, CEN_D, FCC = (95, 125), (125, 140), (140, 148.5), (9, 490)

# ---------------- título ----------------
label(6.5, 10.0, "Asignación de bandas espectrales para NB-PLC", size=12.5,
      weight="bold")
label(6.5, 9.55,
      "Marcos normativos CENELEC (EN 50065-1) y FCC (47 CFR Parte 15 / IEEE 1901.2)",
      size=10, style="italic", color=SECINK)
ax.plot([1.9, 11.1], [9.2, 9.2], color=BLUE_LIGHT, lw=1.6, zorder=2)

# ---------------- fila CENELEC ----------------
CY0, CY1 = 6.85, 7.65
label(0.35, 8.75, "Europa — CENELEC (EN 50065-1)", size=11, weight="bold",
      ha="left")
rbox(warp(3), warp(148.5), CY0, CY1, UNASSIGNED, "none", lw=0, rounding=0.06)
for (f0, f1), letra in [(CEN_B, "B"), (CEN_C, "C"), (CEN_D, "D")]:
    rbox(warp(f0), warp(f1), CY0, CY1, ORANGE, "white", lw=1.2, rounding=0.06,
         shadow=False, zorder=4)
    badge((warp(f0)+warp(f1))/2, CY1+0.45, letra, ORANGE)
rbox(warp(9), warp(95), CY0, CY1, BLUE_MID, "white", lw=1.4, rounding=0.06,
     shadow=False, zorder=5)
badge((warp(9)+warp(95))/2, CY1+0.45, "A", BLUE_MID)
label((warp(9)+warp(95))/2, (CY0+CY1)/2, "uso exclusivo\nDSO / AMI", size=9.5,
      color="white", weight="bold", zorder=6)
for f in [3, 9, 95, 125, 140, 148.5]:
    x = warp(f)
    ax.plot([x, x], [CY0-0.12, CY0], color=SECINK, lw=1.0, zorder=6)
    label(x, CY0-0.20, f"{f:g}".replace(".", ","), size=9, color=SECINK,
          va="top")
label(warp(148.5)+0.42, CY0-0.20, "kHz", size=9, color=SECINK, ha="left",
      va="top", style="italic")

# ---------------- fila FCC ----------------
FY0, FY1 = 4.55, 5.35
label(0.35, 5.80, "EE. UU. — FCC (47 CFR Parte 15) / IEEE 1901.2", size=11,
      weight="bold", ha="left")
rbox(warp(9), warp(490), FY0, FY1, BLUE_MID, "white", lw=1.4, rounding=0.06,
     zorder=4)
label(4.5, (FY0+FY1)/2,
      "FCC — banda principal\npara NB-PLC en EE. UU.", size=10,
      color="white", weight="bold")
# marca de cambio de escala (150 kHz)
XB = warp(150)
ax.plot([XB, XB], [FY0+0.06, FY1-0.06], color="white", lw=1.4,
        ls=(0, (1.2, 1.4)), zorder=7)
for f in [9, 490]:
    x = warp(f)
    ax.plot([x, x], [FY0-0.12, FY0], color=SECINK, lw=1.0, zorder=6)
    label(x, FY0-0.20, f"{f:g}", size=9, color=SECINK, va="top")
ax.plot([XB, XB], [FY0-0.12, FY0], color=SECINK, lw=1.0, zorder=6)
label(XB, FY0-0.20, "150", size=9, color=SECINK, va="top", style="italic")
label(warp(490)+0.33, FY0-0.20, "kHz", size=9, color=SECINK, ha="left",
      va="top", style="italic")

# ---------------- leyenda ----------------
LEG_Y = 3.40
leg = [(BLUE_MID, "Banda principal — uso exclusivo/reservado (CENELEC-A, FCC)"),
       (ORANGE, "Sub-bandas CENELEC para consumidor final (B, C, D)"),
       (UNASSIGNED, "Tramo del rango CENELEC sin sub-banda con nombre (3-9 kHz)")]
for i, (col, txt) in enumerate(leg):
    yy = LEG_Y - i*0.52
    ax.add_patch(FancyBboxPatch((0.35, yy-0.14), 0.5, 0.28,
                 boxstyle="round,pad=0,rounding_size=0.05", facecolor=col,
                 edgecolor="white", lw=1.0, zorder=6))
    label(1.05, yy, txt, size=9.5, ha="left")

# ---------------- notas ----------------
notes = [
    "CENELEC: EN 50065-1, señalización en baja tensión, 3-148,5 kHz. FCC: 47 CFR Parte 15, banda extendida 9-490 kHz. IEEE 1901.2-2013 estandariza PHY/MAC para NB-PLC por debajo de 500 kHz en ambos marcos.",
    "Eje frecuencial comprimido a partir de 150 kHz por propósitos ilustrativos.",
]
yy = 1.72
for n in notes:
    txt = textwrap.fill(n, width=98)
    label(0.35, yy, txt, size=9, style="italic", color=SECINK, ha="left",
          va="top")
    yy -= 0.33*(txt.count("\n")+1) + 0.18

save(fig, "Cenelec_FCC_bands")
print("done")
