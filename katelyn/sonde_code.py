
"""
Spyder Editor

This code makes a Skew-T from sonde data.
"""

import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
import math

import metpy.calc as mpcalc
from metpy.plots import SkewT
from metpy.units import units

from scipy.signal import medfilt

col_names = ['time', 'pressure', 'temperature', 'relative_humidity', 'rh',
             'speed', 'direction', 'geopot', 'dewpoint']

# Column 1: time (UTC)
# Column 2: pressure (hPa)
# Column 3: temperature (C)
# Column 4: relative humidity (%)
# Column 4b: relative humidity
# Column 6: wind speed (m/s)
# Column 7: wind direction (degrees)
# Column 13: dewpoint (C)

date = input('What is the date of the radiosonde launch (YYYYMMDD)? ')

# Read the data in
df = pd.read_fwf(r"C:\\Users\kbarbs57\Desktop\SUNY_Oswego\Fall_2023" \
                 r"\MET390_eclipse_lab\Data\NEBP_Annular_Eclipse" \
                 r"\Launches\SUO251700_101423_id1.txt",
                 encoding='latin', header=18,
                 infer_nrows=2000,
                 usecols=[1, 2, 3, 4, 5, 6, 7, 11, 13],
                 names=col_names)

# Replace '-' with np.NaN
df = df.replace('-', np.NaN)

# Drop any rows with all NaN values for T, Td, winds
df = df.dropna(subset=('pressure', 'temperature', 'rh', 'direction',
                       'speed', 'dewpoint', 'geopot'), how='any'
               ).reset_index(drop=True)

# Read in the specific variables
time = df['time'].values
p = df['pressure'].values*units.hPa
T = df['temperature'].values*units.degC
RH = df['rh'].values*units('%')
wind_speed = df['speed'].values
wind_dir = df['direction'].values
Td = df['dewpoint'].values*units.degC
geopot = df['geopot'].values

# Convert from objects to floats
wind_speed2 = np.zeros(len(wind_speed))
wind_dir2 = np.zeros(len(wind_dir))
p2 = df['pressure'].values
p3 = np.zeros(len(p))
T2 = df['temperature'].values
Td2 = df['dewpoint'].values
T3 = np.zeros(len(T))
Td3 = np.zeros(len(Td))
g3 = np.zeros(len(geopot))

# Convert variables to floats for mathematical operations
for i in range(0, len(wind_speed)):
    wind_speed2[i] = float(wind_speed[i])*1.944
    wind_dir2[i] = float(wind_dir[i])
    p3[i] = float(p2[i])
    T3[i] = float(T2[i])
    Td3[i] = float(Td2[i])
    g3[i] = float(geopot[i])

# Compute the u and v components of wind
wind_speed22 = wind_speed2[:]*units("knots")
wind_dir22 = wind_dir2[:]*units.degrees
u, v = mpcalc.wind_components(wind_speed22, wind_dir22)

# Find times where geopotential decreases for more than 5 time stamps
# and identify what time it recovers
decrease_height = np.zeros((len(g3),2))
for i in range(0,len(g3)-6):
    decrease_height[i,1] = g3[i]
    if g3[i+5]-g3[i] <= 0:
        decrease_height[i,0] = 1
        g3[i] = np.nan
        u[i] = np.nan
        v[i] = np.nan
        T3[i] = np.nan
        Td3[i] = np.nan
        p3[i] = np.nan

# Figure out where the balloons altitude is greater than it was
# prior to drop*
where_recovery = np.where(decrease_height[:] == 1)
if where_recovery[0].size != 0:
    height_prior_to_loss = g3[where_recovery[0][0]-1]
    next_height = np.where(g3 > height_prior_to_loss)
    
    u2 = u[0:where_recovery[0][0]-1]
    u3 = u[next_height[0][0]:]
    v2 = v[0:where_recovery[0][0]-1]
    v3 = v[next_height[0][0]:]
    g4 = g3[0:where_recovery[0][0]-1]
    g5 = g3[next_height[0][0]:]
    T4 = T3[0:where_recovery[0][0]-1]
    T5 = T3[next_height[0][0]:]
    Td4 = Td3[0:where_recovery[0][0]-1]
    Td5 = Td3[next_height[0][0]:]
    p4 = p3[0:where_recovery[0][0]-1]
    p5 = p3[next_height[0][0]:]

    # Bring the variables back together as one profile
    u = np.concatenate([np.array(u2),np.array(u3)])
    v = np.concatenate([np.array(v2),np.array(v3)])
    geopot = np.concatenate([np.array(g4),np.array(g5)])
    p = np.concatenate([np.array(p4),np.array(p5)])
    T = np.concatenate([np.array(T4),np.array(T5)])
    Td = np.concatenate([np.array(Td4),np.array(Td5)])
else:
    p = p3
    T = T3
    Td = Td3
    
# Smooth pressure
smooth_pres = medfilt(p, 7) * units.hPa
p = np.array(smooth_pres)

# Find where the pressure reaches a minimum and only analyze those points
minmin = np.nanmin(p)     
minmin = np.where(p == minmin)
minmin = minmin[0][0]
p = p[0:minmin]
T = T[0:minmin]
Td = Td[0:minmin]
u = u[0:minmin]
v = v[0:minmin]
geopot = geopot[0:minmin]

# Remove nans
p = p[np.logical_not(np.isnan(p))]
T = T[np.logical_not(np.isnan(T))]
Td = Td[np.logical_not(np.isnan(Td))]
u = u[np.logical_not(np.isnan(u))]
v = v[np.logical_not(np.isnan(v))]
geopot = geopot[np.logical_not(np.isnan(geopot))]

# Compute CIN and CAPE
cape,cin = mpcalc.most_unstable_cape_cin(p*units.hPa, T*units.degC,\
                                          Td*units.degC)
print('CAPE is: ',cape)
print('CIN is: ',cin)
    
# Compute the planetary boundary layer height using RI
# theta = mpcalc.potential_temperature(p*units.hPa, T*units.degC)
# ri = mpcalc.gradient_richardson_number(geopot*units.m, theta, u*units.knots,\
#                                        v*units.knots, vertical_dim=0)

# Compute the equilibrium level
prof = mpcalc.parcel_profile(p*units.hPa, T[0]*units.degC, Td[0]*units.degC)
el = mpcalc.el(p[0:len(p)]*units.hPa,T[0:len(T)]*units.degC,Td[0:len(Td)]*units.degC,prof)
print('el: ', el)

# Compute the lifted condensation level
lclp, lclt = mpcalc.lcl(p[0]*units.hPa, T[0]*units.degC, Td[0]*units.degC)
lfcp = mpcalc.lfc(p*units.hPa, T*units.degC, Td*units.degC)
print('lclp: ',lclp)
print('lclt: ',lclt)
print('lfcp: ', lfcp)

# Compute the lifted index
lift_index = mpcalc.lifted_index(p*units.hPa, T*units.degC, prof)
print('lifted_index: ', lift_index)

fig = plt.figure(figsize=(9, 9))
#add_metpy_logo(fig, 115, 100)
skew = SkewT(fig, rotation=45)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot.
skew.plot(p[0:len(p)], T[0:len(T)], 'r')
skew.plot(p[0:len(p)], Td[0:len(Td)], 'g')
skew.plot_barbs(p[0::75], u[0::75], v[0::75])
skew.ax.set_ylim(1000, 5)
skew.ax.set_xlim(-70, 120)
skew.ax.set_yticks([1000, 900, 800, 700, 600, 500,
                    400, 300, 200, 100, 50, 25, 10, 5])
skew.ax.set_xticks([-70,-60, -50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90])
skew.ax.xaxis.set_tick_params(which='major', labelsize=16, direction='out')
skew.ax.yaxis.set_tick_params(which='major', labelsize=16, direction='out')
skew.ax.set_ylabel('Pressure (hPa)', fontsize=24,fontweight='bold')
skew.ax.set_xlabel('Temperature ($^\circ$C)', fontsize=24,fontweight='bold')
skew.ax.set_title("Balloon Launch at %s UTC" %
                  time[0], fontsize=26, fontweight='bold')

props = dict(boxstyle='round', facecolor='white', alpha=1)
skew.ax.text(0.05, 0.95, 'Date: 10/14', transform=skew.ax.transAxes,
              fontsize=18, verticalalignment='top',bbox=props)

# Add the relevant special lines
skew.plot_dry_adiabats()
skew.plot_moist_adiabats()
skew.plot_mixing_lines()

# # Save the plot
# launch_time = time[0].replace(':','')
# plt.savefig('sonde_' + launch_time +'_'+ date + '.png',dpi=300)

