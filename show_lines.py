
### Python module for overplotting emission lines on plots
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

import astropy.units as u

### LIST OF EMISSION LINES APPROPRIATE FOR VARIOUS SOURCES

### SDSS line list
sdss_wave = [ 1033.82 ,  1215.24 ,  1240.81 ,  1305.53 ,  1335.31 ,  1397.61 ,
        1399.8  ,  1549.48 ,  1640.4  ,  1665.85 ,  1857.4  ,  1908.734,
        2439.5  ,  2799.117,  3346.79 ,  3426.85 ,  3727.092,  3729.875,
        3868.76 ,  3967.47 ,  3889.   ,  4102.89 ,  4341.68 ,  4364.436,
        4685.71 ,  4862.68 ,  4932.603,  4960.295,  5008.24 ,  6302.046,  6365.536,
        6549.86 ,  6564.61 ,  6585.27 ,  6718.29 ,  6732.67 ,  7155.157,
        7319.99 ,  7330.73 ,  9068.6  ,  9531.1  , 10049.368]

sdss_name = ['OVI','Ly$\\alpha$','NV','OI','CII','SiIV','SiIV+OIV','CIV','HeII','OIII]','AlIII','CIII]',
'[NeIV]','MgII]','[NeV]','[NeV]','[OII]','[OII]','[NeIII]','[NeIII]','HeI','H$\\delta$','H$\\gamma$','[OIII]',
'HeII','H$\\beta$','[OIII]','[OIII]','[OIII]','[OI]','[OI]','[NII]','H$\\alpha$','[NII]','[SII]','[SII]',
'[FeII]','[OII]','[OII]','[SIII]','[SIII]','Pad']

### SDSS Absorption line list

sdss_wave_ab = [3934.777, 3969.588, 4305.61 , 5176.7  , 5895.6  , 8500.36 ,
       8544.44 , 8664.52 ]

sdss_name_ab = ['K', 'H', 'G', 'Mg', 'Na', 'CaII', 'CaII', 'CaII']


### Emission line library with rest-frame vacuum wavelengths (taken from: http://astronomy.nmsu.edu/drewski/tableofemissionlines.html) and other sources
lines_all = [1215.7, 1240.8, 1549., 1640., 1660., 1666., 1909., 2800., 2945., 3645., 3727., 
            3868.8, 3888., 3967.5, 4026.2, 4101.7, 4340.5, 4363.2, 
            4861.3, 4958.9, 5007, 6548.0, 6562.8, 6583.4, 6716., 6731., 
            9069., 9531.1, 10940, 12820, 18750]
names_all = [r"Ly$\alpha$", "NV", "CIV", "HeII", "OIII]", "OIII]", "CIII]", "MgII", "HeI", "B-break", "[OII]", 
            "[NeIII]", "HeI", "[NeIII]", "HeI", r"H$\delta$", r"H$\gamma$", "[OIII]", 
            r"H$\beta$", "[OIII]", "[OIII]", "[NII]", r"H$\alpha$", "[NII]", "[SII]", "[SII]", 
            "[SIII]", "[SIII]","Pag", "Pab", "Paa"]

lines_lim = [1215.7, 1449., 1909., 2800., 3727., 3868.8, 3967.5, 4101.7, 4340.5,
         4861.3, 4958.9, 5007, 6562.8, 6583.4, 6716., 6731., 
         9069., 9531.1, 10830.340, 10938, 12820, 18750]
names_lim = [r"Ly$\alpha$", "CIV", "CIII]", "MgII", "[OII]", "[NeIII]", "[NeIII]", r"H$\delta$", r"H$\gamma$",
         r"H$\beta$", "[OIII]", "[OIII]", r"H$\alpha$", "[NII]", "[SII]", "[SII]", 
         "[SIII]", "[SIII]", "HeI", r"Pa$\gamma$", r"Pa$\beta$", r"Pa$\alpha$"]

lines_LA7 = [1215.670, 3727., 4340.471, 4861.333, 4958.911, 5006.843]
names_LA7 = [r"Ly$\alpha$", "[OII]",r"H$\gamma$", r"H$\beta$", "[OIII]", "[OIII]"]

lines_paper = [1215.670, 3727., 4861.333, 4958.911, 5006.843, 6562.8]
names_paper = [r"Ly$\alpha$", "[OII]", r"H$\beta$", "[OIII]", "[OIII]", r"H$\alpha$"]

lines_gnz11 = [1215.670, 1486.5, 1748.6, 1909., 2800., 3727., 3868.8, 3967.5, 4101.7, 4340.471]
names_gnz11 = [r"Ly$\alpha$", "NIV]", "NIII]", "CIII]", "MgII", "[OII]", "[NeIII]", "[NeIII]", r"H$\delta$", r"H$\gamma$"]

### ALMA lines
# Line names array
ALMA_ISM_line_names = [
    "[C II]", "[N II]", "[O III]", "[O I]", "[O I]"   
    # Add other lines here if needed
]

# Rest frame wavelengths in microns array
ALMA_ISM_lines = [
    157.74, 205.18, 88.36, 145.52, 63.18  
    # Add rest frame wavelengths of other lines here if needed
]

ALMA_CO_line_names = [
    "CO(1-0)", "CO(2-1)", "CO(3-2)", "CO(4-3)", "CO(5-4)", "CO(6-5)", "CO(7-6)"
]

ALMA_CO_lines = [
        2.60, 1.30, 0.87, 0.65, 0.52, 0.43, 0.37
]

ALMA_H2O_line_names = [
    "H2O(1₁-0₁)", "H2O(2₁-1₂)", "H2O(3₁-2₂)", "H2O(4₁-3₂)", "H2O(5₁-4₂)",
    "OH(2Π1/2 J = 3/2-1/2)", "OH(2Π3/2 J = 3/2-1/2)"
]

ALMA_H2O_lines = [
        1113.343, 752.033, 489.346, 325.153, 213.235,
    183.31, 161.63
]


### Functions to display lines
def show_lines(lines, names, z, c='k', min_wave=0.6e4, max_wave=5.3e4, ypos=2.2e-20, xoffset=0.02e4, lnames=False, alpha=0.5, fontsize=8):
    for i in range(len(lines)):
        if (lines[i]*(1+z)) < min_wave or (lines[i]*(1+z)) > max_wave:
            continue
        else:
            plt.axvline((lines[i]*(1+z)), ls='--', c=c, alpha=alpha, zorder=3)
            if lnames:
                plt.text(((lines[i]*(1+z)) + xoffset), ypos, names[i], color=c, rotation=90, fontsize=fontsize)
            
    return()


def show_lines_LA7(lines, names, z, c='k', alpha=0.6, lnames=True):
    for i in range(len(lines)):
        if (lines[i]*(1+z)) < 0.6e4 or (lines[i]*(1+z)) > 5.3e4:
            continue
        else:
            plt.axvline((lines[i]*(1+z)), ls='--', c=c, alpha=alpha, zorder=3)
            if lnames:
                if i==4:
                    plt.text(((lines[i]*(1+z)) + 0.02e4), 0.5e-20, names[i], color=c, rotation=90, fontsize=8)
                else:
                    plt.text(((lines[i]*(1+z)) + 0.02e4), 0.62e-20, names[i], color=c, rotation=90, fontsize=8)
            
    return()

def show_restlines(lines, names, min_wave, max_wave, c='k', ypos=2.2e-20, xoffset=0.02e4, lnames=False, alpha=0.3):
    for i in range(len(lines)):
        if lines[i] < min_wave or lines[i] > max_wave:
            continue
        else:
            plt.axvline(lines[i], ls='--', c='k', alpha=alpha)
        if lnames:
                plt.text((lines[i] + xoffset), ypos, names[i], color=c, rotation=90, fontsize=fontsize)
            
    return()


def show_ALMA_lines(lines, names, z, min_freq=35e9, max_freq=950e9, c='k', ypos=1e-2, xoffset=3e9, alpha=0.3, frequency=True, lnames=False):
    if frequency:
        lines = (lines*u.micron).to(u.Hz, equivalencies=u.spectral()).value

    for i in range(len(lines)):
        if (lines[i]/(1+z)) < min_freq or (lines[i]/(1+z)) > max_freq:
            continue
        else:
            plt.axvline((lines[i]/(1+z)), ls='--', c=c, alpha=alpha, zorder=3)
            if lnames:
                plt.text(((lines[i]/(1+z)) + xoffset), ypos, names[i], color=c, rotation=90, fontsize=fontsize)

    return()
