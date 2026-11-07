# -*- coding: utf-8 -*-
"""Figura 2.6 (fig:prime_topology): topología dinámica de red PRIME.
v3: letra de 9,5-13 pt EFECTIVOS en página, fondo transparente (sin tarjeta
gris), título/subtítulo del Nodo Base separados."""
from matplotlib.patches import FancyBboxPatch, Circle, Arc
import numpy as np
from common import *

FIG_W = 7.6
fig, ax, eff, scale = make_fig(FIG_W, (0, 13.6), (1.25, 12.0))

def rbox(x0, x1, y0, y1, fc, ec, lw=1.6, ls="-", rounding=0.12, zorder=1,
         shadow=True):
    if shadow:
        ax.add_patch(FancyBboxPatch((x0, y0-0.06), x1-x0, y1-y0,
                     boxstyle=f"round,pad=0,rounding_size={rounding}",
                     facecolor=SHADOW, edgecolor="none", zorder=zorder-0.5))
    ax.add_patch(FancyBboxPatch((x0, y0), x1-x0, y1-y0,
                 boxstyle=f"round,pad=0,rounding_size={rounding}",
                 facecolor=fc, edgecolor=ec, lw=lw, ls=ls, zorder=zorder))

def label(x, y, text, size=11, color=INK, weight="normal", ha="center",
          va="center", style="normal", zorder=6, ls=1.2):
    ax.text(x, y, text, ha=ha, va=va, fontsize=eff(size), color=color,
            weight=weight, fontstyle=style, zorder=zorder, linespacing=ls)

def edge(x0, y0, x1, y1, color=SECINK, lw=1.2, zorder=2):
    ax.plot([x0, x1], [y0, y1], color=color, lw=lw, zorder=zorder,
            solid_capstyle="round")

def node_shadow(x, y, r):
    ax.add_patch(Circle((x, y-0.035), r, facecolor=SHADOW, edgecolor="none",
                 zorder=2.4))

def icon_base(x, y, r=0.62, lw=2.0, spoke_lw=1.6, shadow=True):
    if shadow:
        node_shadow(x, y, r)
    ax.add_patch(Circle((x, y), r, facecolor=BLUE_DARK, edgecolor="white",
                 lw=lw, zorder=3))
    for ang in range(0, 360, 45):
        a = np.radians(ang)
        ax.plot([x+0.322*r*np.cos(a), x+0.645*r*np.cos(a)],
                [y+0.322*r*np.sin(a), y+0.645*r*np.sin(a)], color="white",
                lw=spoke_lw, zorder=3.1, solid_capstyle="round")
    ax.add_patch(Circle((x, y), 0.226*r, facecolor="white", edgecolor="none",
                 zorder=3.2))

def node_base(x, y):
    r = 0.62
    icon_base(x, y, r)
    # subtítulo pegado al círculo y título claramente por encima
    label(x, y+r+0.20, "(Embebido en el DCU)", size=9.5, color=SECINK,
          style="italic")
    label(x, y+r+0.56, "Nodo Base", size=13, weight="bold")

def icon_switch(x, y, r=0.34, lw=1.4, arc_lw=1.5, shadow=True):
    if shadow:
        node_shadow(x, y, r)
    ax.add_patch(Circle((x, y), r, facecolor=BLUE_MID, edgecolor="white",
                 lw=lw, zorder=3))
    dy = 0.147*r
    for rad_ratio in (0.294, 0.5):
        rad = rad_ratio*r
        ax.add_patch(Arc((x, y-dy), rad*2, rad*2, angle=0, theta1=30,
                     theta2=150, color="white", lw=arc_lw, zorder=3.1))
        ax.add_patch(Arc((x, y+dy), rad*2, rad*2, angle=180, theta1=30,
                     theta2=150, color="white", lw=arc_lw, zorder=3.1))

def icon_service(x, y, r=0.24, lw=1.2, shadow=True):
    if shadow:
        node_shadow(x, y, r)
    ax.add_patch(Circle((x, y), r, facecolor=TINT_2, edgecolor=BLUE_LIGHT,
                 lw=lw, zorder=3))
    ax.add_patch(Circle((x, y), 0.208*r, facecolor=BLUE_DARK, edgecolor="none",
                 zorder=3.1))
    ax.plot([x, x+0.417*r], [y, y+0.375*r], color=BLUE_DARK, lw=lw,
            zorder=3.1, solid_capstyle="round")

node_switch = lambda x, y: icon_switch(x, y)
node_service = lambda x, y: icon_service(x, y)

# ---------------- título ----------------
label(6.8, 11.62, "Topología dinámica de red PRIME", size=13, weight="bold")
label(6.8, 11.15, "Árbol lógico con niveles de conmutación (Switches) coordinados por el Nodo Base",
      size=10, style="italic", color=SECINK)
ax.plot([2.3, 11.3], [10.80, 10.80], color=BLUE_LIGHT, lw=1.6, zorder=2)

# ---------------- niveles ----------------
Y_BASE, Y_L1, Y_L2, Y_L3 = 9.0, 7.35, 5.55, 3.75
for yy, txt in [(Y_L1, "Nivel 1"), (Y_L2, "Nivel 2"), (Y_L3, "Nivel 3")]:
    ax.plot([0.3, 13.3], [yy, yy], color=GRID, lw=1.0, ls=(0, (2, 3)),
            zorder=1.2)
    label(0.3, yy+0.27, txt, size=9.5, color=SECINK, style="italic", ha="left")
label(0.3, Y_BASE+0.27, "Nivel 0", size=9.5, color=SECINK, style="italic",
      ha="left")

# ---------------- árbol ----------------
X_BASE = 6.8
L1_X = [1.9, 4.6, 9.0, 11.7]
L1_SWITCH = {4.6, 9.0}
L2 = {4.6: [3.1, 4.6, 6.1], 9.0: [7.5, 9.0, 10.5]}
L2_SWITCH = {3.1, 10.5}
L3 = {3.1: [2.3, 3.9], 10.5: [9.7, 11.3]}

for x1 in L1_X:
    edge(X_BASE, Y_BASE-0.55, x1, Y_L1+0.30, color=BLUE_LIGHT, lw=1.6)
for parent, children in L2.items():
    for x2 in children:
        edge(parent, Y_L1-0.30, x2, Y_L2+0.22, color=SECINK, lw=1.1)
for parent, children in L3.items():
    for x3 in children:
        edge(parent, Y_L2-0.22, x3, Y_L3+0.18, color=SECINK, lw=1.0)

node_base(X_BASE, Y_BASE)
for x1 in L1_X:
    (node_switch if x1 in L1_SWITCH else node_service)(x1, Y_L1)
for parent, children in L2.items():
    for x2 in children:
        (node_switch if x2 in L2_SWITCH else node_service)(x2, Y_L2)
for parent, children in L3.items():
    for x3 in children:
        node_service(x3, Y_L3)

# ---------------- promoción dinámica a Switch (halo sobre el nodo real) ----
PROMO_X, PROMO_Y, PROMO_R = 4.6, Y_L1, 0.34 + 0.14
ax.add_patch(Circle((PROMO_X, PROMO_Y), PROMO_R, facecolor="none",
             edgecolor=SECINK, lw=1.2, ls=(0, (2, 1.5)), zorder=4))
_ang = np.radians(148)
_tip = (PROMO_X + PROMO_R*np.cos(_ang), PROMO_Y + PROMO_R*np.sin(_ang))
ax.annotate("", xy=_tip, xytext=(1.2, 8.07),
            arrowprops=dict(arrowstyle="-|>", color=SECINK, lw=1.1,
            connectionstyle="arc3,rad=-0.18", linestyle=(0, (3, 2))),
            zorder=4)
label(0.3, 8.50, "Nodo promovido a Switch\ntras evaluar la calidad de enlace",
      size=9.5, color=SECINK, style="italic", ha="left")

# ---------------- zona de degradación ----------------
rbox(0.3, 13.3, 1.55, 3.05, "none", "#b9b7b0", lw=1.3, ls=(0, (4.5, 3)),
     rounding=0.10, shadow=False, zorder=1.5)
label(6.8, 2.62,
      "Más allá de 4-5 saltos lógicos: la latencia de propagación crece de forma exponencial",
      size=10, color=SECINK, style="italic")
label(6.8, 2.00,
      "penaliza la lectura masiva de load profiles y satura el ancho de banda del DCU",
      size=10, color=SECINK, style="italic")

# ---------------- leyenda (iconos reales en miniatura) ----------------
LX0, LY, ROW_H = 8.85, 9.95, 0.55
TEXT_X = LX0 + 0.42
for i, (kind, txt) in enumerate([("base", "Nodo Base (raíz)"),
                                 ("switch", "Switch (repetidor)"),
                                 ("service", "Nodo de Servicio (contador)")]):
    yy = LY - i*ROW_H
    if kind == "base":
        icon_base(LX0, yy, r=0.21, lw=1.3, spoke_lw=1.0, shadow=False)
    elif kind == "switch":
        icon_switch(LX0, yy, r=0.18, lw=1.1, arc_lw=1.0, shadow=False)
    else:
        icon_service(LX0, yy, r=0.16, lw=1.0, shadow=False)
    label(TEXT_X, yy, txt, size=9.5, ha="left", color=INK)

save(fig, "topologia_red_PRIME")
print("done")
