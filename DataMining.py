import numpy as np

def f(x, m, std): #PDF for Normal distribution
    return (1 / (np.sqrt(2 * np.pi) * std)) * np.e**(-1 * ((x - m)**2/(2 * std**2)))

def LH_SG(P3_x, P2_x, TRB_x, AST_x, STL_x, BLK_x):    # Likelihood of SG
    return (50/100) * f(P3_x, 1.7976, 0.5573) * f(P2_x, 2.714, 1.4898) * f(TRB_x, 3.0937, 1.0266) * f(AST_x, 2.3687, 1.0757) * f(STL_x, 0.862, 0.2918) * f(BLK_x, 0.2931, 0.1749)

def LH_C(P3_x, P2_x, TRB_x, AST_x, STL_x, BLK_x):     # Likelihood of C
    return (50/100) * f(P3_x, 0.3577, 0.5779) * f(P2_x, 3.8003, 1.9936) * f(TRB_x, 6.9771, 3.239) * f(AST_x, 1.4092,  1.229) * f(STL_x, 0.588,  0.332) * f(BLK_x, 1.1264, 0.5743)

def result():
    print("new instance")
    P3_x  = float(input("3P : "))
    P2_x  = float(input("P2 : "))
    TRB_x = float(input("TRB : "))
    AST_x = float(input("AST : "))
    STL_x = float(input("STL : "))
    BLK_x = float(input("BLK : "))
    print("=============================")
    if LH_SG(P3_x, P2_x, TRB_x, AST_x, STL_x, BLK_x) <= LH_C(P3_x, P2_x, TRB_x, AST_x, STL_x, BLK_x):
        print("recommend : SG") # Shooting Guard
    else:
        print("recommend : C") # Center
result()
