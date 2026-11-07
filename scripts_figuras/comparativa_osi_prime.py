# -*- coding: utf-8 -*-
"""Figura 2.5 (fig:osi_prime): correspondencia OSI <-> capas de PRIME.
v3: letra de 9,5-12,5 pt EFECTIVOS en página, fondo transparente, sin
tarjetas grises. Misma correspondencia exacta: PHY=capa 1; MAC=subcapa inferior
de la capa 2; CL=subcapa superior de la capa 2 + capa 3 completa."""
from matplotlib.patches import FancyBboxPatch, Circle, PathPatch
from matplotlib.path import Path
from common import *

FIG_W = 7.2
LH = 1.3                      # alto de una capa OSI (unidades)
fig, ax, eff, scale = make_fig(FIG_W, (0, 14.5), (-1.05, 12.15))

def rbox(x0, x1, y0, y1, fc, ec, lw=1.6, ls="-", rounding=0.09, zorder=3,
         shadow=True):
    if shadow:
        ax.add_patch(FancyBboxPatch((x0, y0-0.045), x1-x0, y1-y0,
                     boxstyle=f"round,pad=0,rounding_size={rounding}",
                     facecolor=SHADOW, edgecolor="none", zorder=zorder-0.5))
    ax.add_patch(FancyBboxPatch((x0, y0), x1-x0, y1-y0,
                 boxstyle=f"round,pad=0,rounding_size={rounding}",
                 facecolor=fc, edgecolor=ec, lw=lw, ls=ls, zorder=zorder))

def label(x, y, text, size=11, color=INK, weight="normal", ha="center",
          va="center", style="normal", zorder=6, ls=1.2):
    ax.text(x, y, text, ha=ha, va=va, fontsize=eff(size), color=color,
            weight=weight, fontstyle=style, zorder=zorder, linespacing=ls)

def badge(x, y, text, fc, tc, r=0.25, zorder=7):
    ax.add_patch(Circle((x, y), r, facecolor=fc, edgecolor="white", lw=1.3,
                 zorder=zorder))
    ax.text(x, y-0.005, text, ha="center", va="center", fontsize=eff(9.5),
            color=tc, weight="bold", zorder=zorder+0.1)

def bracket(x0, x_tip, y0, y1, color, lw=1.4):
    ymid = (y0+y1)/2
    verts = [(x0, y0), (x_tip, y0), (x_tip, ymid-0.02), (x_tip+0.18, ymid),
             (x_tip, ymid+0.02), (x_tip, y1), (x0, y1)]
    codes = [Path.MOVETO] + [Path.LINETO]*6
    ax.add_patch(PathPatch(Path(verts, codes), facecolor="none",
                 edgecolor=color, lw=lw, joinstyle="round",
                 capstyle="round", zorder=4))

# ---------------- título ----------------
label(7.25, 11.55, "Correspondencia entre el modelo OSI y\nla arquitectura de capas de PRIME",
      size=12.5, weight="bold")
ax.plot([3.3, 11.2], [10.82, 10.82], color=BLUE_LIGHT, lw=1.6, zorder=2)

# ---------------- columna OSI ----------------
OX0, OX1 = 0.45, 4.75
OSI = [(1, "Física"), (2, "Enlace de datos"), (3, "Red"), (4, "Transporte"),
       (5, "Sesión"), (6, "Presentación"), (7, "Aplicación")]
label((OX0+OX1)/2, 10.25, "Modelo OSI", size=13, weight="bold")
label((OX0+OX1)/2, 9.65, "ISO/IEC 7498-1\n7 capas de referencia", size=9.5,
      style="italic", color=SECINK)
TINTS = {1: TINT_3, 2: TINT_2, 3: TINT_1}
for n, name in OSI:
    y0, y1 = (n-1)*LH, n*LH
    cov = n <= 3
    rbox(OX0, OX1, y0+0.06, y1-0.06, TINTS.get(n, "white"),
         (BLUE_LIGHT if cov else "#c9c7c0"),
         lw=1.5 if cov else 1.1, rounding=0.08, shadow=False)
    label((OX0+OX1)/2+0.15, (y0+y1)/2, name, size=11,
          color=INK if cov else SECINK, weight="bold" if cov else "normal")
    badge(OX0+0.40, y1-0.06-0.02-0.0, str(n), BLUE_LIGHT if cov else "white",
          "white" if cov else SECINK)
    if not cov:
        ax.patches[-1].set_edgecolor("#c9c7c0")
label((OX0+OX1)/2, -0.55, "capas 1-3: único tramo con\nequivalente directo en PRIME",
      size=9.5, style="italic", color=SECINK)

# ---------------- columna PRIME ----------------
PX0, PX1 = 10.0, 14.25
label((PX0+PX1)/2, 10.25, "PRIME", size=13, weight="bold")
label((PX0+PX1)/2, 9.65, "3 capas\n(inspirada en IEEE 802.16)", size=9.5,
      style="italic", color=SECINK)
g = 0.06
B = [0, 1*LH, 1.5*LH, 3*LH]
rbox(PX0, PX1, B[3]+g, 7*LH-g, "none", "#b9b7b0", lw=1.3, ls=(0, (4.5, 3)),
     rounding=0.09, shadow=False)
label((PX0+PX1)/2, (B[3]+7*LH)/2,
      "resto de la pila\n(p. ej. aplicación\nDLMS/COSEM) no\nespecificada por PRIME", size=9.5,
      style="italic", color=SECINK)
rbox(PX0, PX1, B[2]+g, B[3]-g, BLUE_LIGHT, "none", lw=0, rounding=0.09)
label((PX0+PX1)/2, (B[2]+B[3])/2+0.22, "Capa de convergencia", size=11,
      color="white", weight="bold")
label((PX0+PX1)/2, (B[2]+B[3])/2-0.25, "(CL)", size=10, color="#dfeaf9",
      style="italic")
rbox(PX0, PX1, B[1]+g, B[2]-g, BLUE_MID, "none", lw=0, rounding=0.09)
label((PX0+PX1)/2, (B[1]+B[2])/2, "MAC", size=11, color="white",
      weight="bold")
rbox(PX0, PX1, B[0]+g, B[1]-g, BLUE_DARK, "none", lw=0, rounding=0.09)
label((PX0+PX1)/2, 0.78, "Capa física", size=11, color="white", weight="bold")
label((PX0+PX1)/2, 0.38, "(PHY)", size=10, color="#c9dbf3", style="italic")
label((PX0+PX1)/2, -0.55, "3 capas: PHY, MAC y capa\nde convergencia (CL)", size=9.5,
      style="italic", color=SECINK)

# ---------------- corchetes / conectores ----------------
xb = OX1 + 0.62
bx0 = OX1 + 0.12
TX = xb + 0.38
bracket(bx0, xb, B[0]+g, B[1]-g, BLUE_DARK)
label(TX, (B[0]+B[1])/2, "PHY $\\equiv$ capa 1", size=10, color=BLUE_DARK,
      ha="left", style="italic")
bracket(bx0, xb, B[1]+g, B[2]-g, BLUE_MID)
label(TX, (B[1]+B[2])/2, "MAC $\\equiv$ subcapa inferior\nde la capa 2", size=9.5,
      color=BLUE_MID, ha="left", style="italic")
bracket(bx0, xb, B[2]+g, B[3]-g, BLUE_LIGHT)
label(TX, (B[2]+B[3])/2, "CL $\\equiv$ subcapa superior\nde la capa 2 + capa 3\ncompleta", size=9.5,
      color=BLUE_LIGHT, ha="left", style="italic")

save(fig, "comparativa_OSI_PRIME")
print("done")
