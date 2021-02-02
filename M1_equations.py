from math import pi

def circular_area(diameter):
    # Takes diameter and converts to area of circle
    return (pi * diameter ** 2) /4

def ultimate_force(P_u,area):
    # 
    return P_u/area

def elongation(L_i,L_f):
    # takes initial length and final length to find elongation as a percent
    return (L_f - L_i) / L_i * 100

def area_reduction(A_i,A_f):
    # takes initial and final area to find area reduction as a percent
    return (A_f - A_i) / A_i * 100

def psi_ksi(psi):
    return psi / 1_000

def stress(P,A):
    return(P/A)

def strain(L_i,L_f):
    return (L_f - L_i)/L_i

def modulus_elasticity(stress,strain):
    return stress / strain

