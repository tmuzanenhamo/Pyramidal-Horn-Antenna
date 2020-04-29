import math
import numpy as np

def microstrip_patch(f,Er, h):
    
    h = h/1000
    f = f*1e9
    c = 3e8
    
    # Calculating the width and the Length of the Patch
    
    W = (c/(2*f))* math.sqrt(2/(Er+1))
    Er_eff = (Er+1)/2 + ((Er-1)/2)*(1/math.sqrt(1+(12*(h/W))))
    L_eff = c/(2*f*math.sqrt(Er_eff))
    a1 = (Er_eff + 0.3) * ((W/h)+0.264)
    a2 = (Er_eff - 0.258) * ((W/h)+0.8)
    delta_L = (0.412*(a1/a2))*h
    L = L_eff- 2*delta_L
    print()
    print(f"The width of the patch is {W*1000} mm")
    print(f"The length of the patch is {L*1000} mm")
    print()
    # Calculating the input impedance of the patch 
    Zo = 90 * (Er**2) * ((L/W)**2)/(Er-1)
    # Calculating the Strip transition line
    Zt = math.sqrt(50*Zo)
    a3 = math.exp(Zt*math.sqrt(Er)/60)
    p = -4*h*a3
    q = 32*h**2
    Wt1 = -(p/2) + math.sqrt((p/2)**2-q)
    Wt2 = -(p/2) - math.sqrt((p/2)**2-q)
    
    Er_t = (Er+1)/2 + ((Er-1)/2)*(1/(math.sqrt(1+(12*(h/Wt2)))))
    L_t =(c/f)/(4*math.sqrt(Er_t))
    
    print(f"The width of the transimion line is {Wt2*1000} mm")
    print(f"The width of the transimion line is {L_t*1000} mm")
    print()
      
    
    
def main():
    
    f = eval(input("Énter Frequency: "))
    Er = eval(input("Énter Dielectric Constant: "))
    h = eval(input("Énter Height in mm:     "))
    
    mic = microstrip_patch(f,Er,h)
    
if __name__ == '__main__':
    main()
    




