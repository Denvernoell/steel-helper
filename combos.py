def Combo_Load(load_type,combo,D = 0,L = 0,L_r = 0,S = 0,R = 0,W = 0):
    if load_type == "LRFD":
        if combo == 1:
            return 1.4 * D
        elif combo == 2:
            return 1.2 * D + 1.6 * L + 0.5 * (max(L_r,S,R))
        elif combo == 3:
            return 1.2 * D + 1.6 * max(L_r, S, R) + max(0.5*L, 0.5 * W)
        elif combo == 4:
            return 1.2 * D + 1.0 * W + 1.0 * L + 0.5 * max(L_r, S, R)
        elif combo == 5:
            return 0.9 * D + 1.0 * W 
        
    if load_type == "ASD":
        if combo == 1:
            return D

        elif combo == 2:
            return D + L

        elif combo == 3:
            return D + max(L_r, S, R)

        elif combo == 4:
            return D + 0.75 * L + 0.75 * max(L_r, S, R)

        elif combo == 5:
            return D + 0.6 * W 

        elif combo == 6:
            return D + 0.75 * L + 0.75 * 0.6 * W + 0.75 * max(L_r,S,R) 

        elif combo == 7:
            return 0.6 * D + 0.6 * W
def get_combo_loads(D,L_r,S,R,W,L):
    omega = 1.67
    phi = 0.9
    mymax = 0
    
#     LRFD
    print("LRFD")
    for i in range(1,6):
        combo_value_LRFD = Combo_Load("LRFD",i,D,L,L_r,S,R,W)
        
        print(f"Combonation {i} = {(combo_value_LRFD):.3}")
        if combo_value_LRFD > mymax:
            mymax = combo_value_LRFD
    print(f"max = {mymax:.3}")
    print(f"max / phi = {(mymax / phi):.3}")
    
    
    mymax = 0
    print("")
    print("ASD")
    for i in range(1,8):
        combo_value_ASD = float(Combo_Load("ASD",i,D,L,L_r,S,R,W))
        
        print(f"Combonation {i} = {(combo_value_ASD):.3}")
        if combo_value_ASD > mymax:
            mymax = combo_value_ASD
    print(f"max = {mymax:.3}")
    print(f"max * omega = {(mymax * omega):.3}")