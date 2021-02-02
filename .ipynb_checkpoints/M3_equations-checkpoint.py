from M1_equations import *

import pint
u = pint.UnitRegistry()
Q = u.Quantity

def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac

def hole_size(bolt_size):
    if bolt_size < 1 * u.inch:
        return bolt_size + 1/8 * u.inch
    else:
        return bolt_size + 3/16 * u.inch

def design_strength(system,strength,load_type):
    if system == "LRFD":
        if load_type == "yield":
            return 0.9 * strength
        if load_type == "rupture":
            return 0.75 * strength
    if system == "ASD":
            if load_type == "yield":
                return 0.6 * strength
            if load_type == "rupture":
                return 0.5 * strength

def tension_members(w_plate,h_plate,F_y,F_u,A_g,num_holes,bolt_size,effective_factor):
    w_plate = convert_to_float(w_plate) * u.inch
    h_plate *= u.inch
    # steel = "A36"
    #from steel bible
    F_y *= u.kips
    F_u *= u.kips
    A_g *= u.inch * u.inch

    #num_holes = 2
    bolt_size = convert_to_float(bolt_size) * u.inch

    #effective_factor
    
    
    
    
    
    if A_g == 0:
#         print(w_plate)
#         print(h_plate)
        A_g =  w_plate * h_plate
    A_g

    d_hole = hole_size(bolt_size)
    A_hole = w_plate * d_hole

    print(f"d_hole = {d_hole:.3}")
    print(f"A_hole = {A_hole:.3}")

    #holes = 4, 5/8 * u.inch

    #Nominal strength

    #F_y = 36 * u.lbs
    P_n_gross = F_y * A_g

    print(f"Nominal strength gross= {P_n_gross}")

    #For rupture of the net section

    A_holes = A_hole * num_holes
    # print(A_holes)
    A_n = A_g - A_holes
    A_n

    A_e = A_n
    # F_u = F_y
    P_n_net = F_u * A_e 
    #assume effective net area is 85% of computed net area
    P_n_net *= effective_factor
    print(f"Nominal strength net = {P_n_net:.3}")

    #`design_strength(system,strength,load_type)`
    print("\nLRFD design strength")
    LRFD_y = design_strength("LRFD",P_n_gross,"yield")
    LRFD_r = design_strength("LRFD",P_n_net,"rupture")

    print(f"Yield strength = {LRFD_y:.3}")
    print(f"Rupture strength = {LRFD_r:.3}")
    
    print("\nASD allowable strength")
    ASD_y = design_strength("ASD",P_n_gross,"yield")
    ASD_r = design_strength("ASD",P_n_net,"rupture")

    print(f"Yeild strength = {ASD_y:.3}")
    print(f"Rupture strength = {ASD_r:.3}")

# # Example 3.1

# w_plate = (1/2)
# h_plate = (5)
# # steel = "A36"
# #from steel bible
# A_g = 0
# F_y = 36 
# F_u = 58 


# num_holes = 2
# bolt_size = 5/8 

# effective_factor = 1
# tension_members(w_plate,h_plate,F_y,F_u,A_g,num_holes,bolt_size,effective_factor)
# print("")

# # Example 3.2

# w_plate = (3/8 )
# h_plate = (0)
# # steel = "A36"
# #from steel bible
# A_g = 2.5 
# F_y = 36 
# F_u = 58 
# num_holes = 1
# bolt_size = 7/8 

# effective_factor = .85
# tension_members(w_plate,h_plate,F_y,F_u,A_g,num_holes,bolt_size,effective_factor)