
### Python module for overplotting emission lines on plots
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

### LIST OF EMISSION LINES APPROPRIATE FOR VARIOUS SOURCES

### SDSS line list
with open("sdss_lines/emission_lines_sdss.txt", 'r') as f:
    emlines=[line.split() for line in f]

sdss_wave = []
sdss_name = []
for i in range(len(emlines)):
    sdss_wave.append(float(emlines[i][0]))
    sdss_name.append(emlines[i][3])


### SDSS absorption line list
with open("sdss_lines/absorption_lines_sdss.txt", 'r') as f:
    ablines=[line.split() for line in f]

sdss_wave = []
sdss_name = []
for i in range(len(ablines)):
    sdss_wave.append(float(ablines[i][0]))
    sdss_name.append(ablines[i][3])


    
sdss_wave = np.array(sdss_wave)

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

def show_restlines(lines, names, min_wave, max_wave, ypos=2.2e-20, xoffset=0.02e4, lnames=False, alpha=0.3):
    for i in range(len(lines)):
        if lines[i] < min_wave or lines[i] > max_wave:
            continue
        else:
            plt.axvline(lines[i], ls='--', c='k', alpha=alpha)
            plt.text((lines[i] + xoffset), ypos, names[i], rotation=90, fontsize=8)
        if lnames:
                plt.text((lines[i] + xoffset), ypos, names[i], color=c, rotation=90, fontsize=fontsize)
            
    return()
