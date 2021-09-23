#Author : Ailton Oliveira, Lucas Damasceno
#Email : ailton.pinto@itec.ufpa.br, lucas.damasceno.silva@itec.ufpa.br
#License : This script is distributed under "Public Domain" license.
###################################################################

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import argparse

def ecc_33(type=0,f=1, d=(np.sqrt(164))/1000, hb=15, hr=2):
    Afs = 92.4 + (20*np.log10(d)) + (20*np.log10(f))

    Abm = 20.41 + (9.83*np.log10(d)) + (7.894*np.log10(f)) + (9.56*(np.log10(f)**2))

    Gb = np.log10(hb/200) * (13.958 + (5.8*(np.log10(d)**2)))

    #Medium cities
    if type == 'medium':
        Gr = (42.57 + 13.7*np.log10(f)) * (np.log10(hr) - 0.585)

    #Big cities
    elif type == 'big':
        Gr = 0.759*hr - 1.892
    
    else:
        raise TypeError("Invalid argument.")

    okumura_hata_extension = Afs + Abm - Gb - Gr

    return okumura_hata_extension

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--model", "-m", 
                        help='Pass City type for ECC-33 model ("medium" or "big")',
                        action="store", 
                        dest="model", 
                        type=str)

    args = parser.parse_args()

    city_type = args.model
    
    #1GHz to 3.5GHZ
    frequency_range = np.arange(1, 3.6, 0.1)

    path_loss = []
    
    for frequency in frequency_range:
        path_loss.append(ecc_33(city_type, frequency))
    
    mpl.style.use("seaborn")
    plt.plot(frequency_range, path_loss)
    plt.title("ECC-33 Propagation Model")
    plt.xlabel("Frequency (GHz)")
    plt.ylabel("Path Loss (dB)")
    plt.show()
