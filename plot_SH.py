# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:44:41 2022

@author: hding
"""

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import cmaps
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

def main():
    root_path = "/work/mh0066/m300971/Data/CMIP6/process/"
    models = ["TaiESM1", "AWI-ESM-1-1-LR", "BCC-ESM1", "CAMS-CSM1-0", "CAS-ESM2-0",\
              "CanESM5", "ACCESS-ESM1-5", "MPI-ESM-1-2-HAM", "MIROC6", "MPI-ESM1-2-LR",\
              "MRI-ESM2-0", "GISS-E2-1-H", "CESM2", "NorESM2-LM", "NESM3"]
    c = ["k", "brown", "r", "lightsalmon", "chocolate", "orange", "gold", "darkkhaki", "lightgreen", "darkgreen",\
        "aqua", "skyblue", "navy", "orchid", "blueviolet"]
        
    DJF_mon = np.hstack((np.arange(1380,1969,12), np.arange(1381,1970,12), np.arange(1391,1980,12)))
    DJF_mon = np.sort(DJF_mon)
    
    JJA_mon = np.hstack((np.arange(1385,1974,12), np.arange(1386,1975,12), np.arange(1387,1976,12)))
    JJA_mon = np.sort(JJA_mon)
        
    latst=-90
    lated=90
    lonst=0
    loned=360
    
    """fig=plt.figure(figsize=[10,10.5], dpi=200)
    ax = plt.subplot(111,projection=ccrs.PlateCarree(central_longitude=0))
    file = root_path + "zg_Amon_" + models[0] + "_historical_r1i1p1f1_gn_185001-201412.nc"
    data = Dataset(file)
    lon0 = data["lon"][:]
    lat0 = data["lat"][:]
    ax = cartopy_map(ax,lon0,lat0,lonst,loned,latst,lated,"DJF")
    b = []
    for i in range(len(models)):
        model = models[i]
        file = root_path + "zg_Amon_" + model + "_historical_r1i1p1f1_gn_185001-201412.nc"        
    
        data = Dataset(file)
        lon = data["lon"][:]
        lat = data["lat"][:]
        plev = data["plev"][:]
        ppick = np.where((plev>=84900) & (plev<=85100))
        zg = data["zg"][:,ppick[0][0],:,:]
        zg_DJF = np.average(zg[DJF_mon,:,:], axis=0)
        
        a = ax.contour(lon,lat,smooth(zg_DJF),levels=[1530],colors=c[i],linewidths=0.5,transform=ccrs.PlateCarree())
        h,_ = a.legend_elements()
        b.append(h[0])
        plt.clabel(a,fontsize=4,colors="k",fmt="%.0f") 
    
    ax.legend(b, models, fontsize=5, loc='lower center', bbox_to_anchor=(0.5, -0.15), ncol=5)
    plt.show()
    figname = "/work/mh0066/m300971/Output/850zg_DJF.png"
    plt.savefig(figname)"""
    
    
    fig=plt.figure(figsize=[10,10.5], dpi=200)
    ax = plt.subplot(111,projection=ccrs.PlateCarree(central_longitude=0))
    file = root_path + "zg_Amon_" + models[0] + "_historical_r1i1p1f1_gn_185001-201412.nc"
    data = Dataset(file)
    lon0 = data["lon"][:]
    lat0 = data["lat"][:]
    ax = cartopy_map(ax,lon0,lat0,lonst,loned,latst,lated,"JJA")
    b = []
    for i in range(len(models)):
        model = models[i]
        file = root_path + "zg_Amon_" + model + "_historical_r1i1p1f1_gn_185001-201412.nc"        
    
        data = Dataset(file)
        lon = data["lon"][:]
        lat = data["lat"][:]
        plev = data["plev"][:]
        ppick = np.where((plev>=84900) & (plev<=85100))
        zg = data["zg"][:,ppick[0][0],:,:]
        zg_JJA = np.average(zg[JJA_mon,:,:], axis=0)
        
        a = ax.contour(lon,lat,smooth(zg_JJA),levels=[1530],colors=c[i],linewidths=0.5,transform=ccrs.PlateCarree())
        h,_ = a.legend_elements()
        b.append(h[0])
        plt.clabel(a,fontsize=4,colors="k",fmt="%.0f") 
    
    ax.legend(b, models, fontsize=5, loc='lower center', bbox_to_anchor=(0.5, -0.15), ncol=5)
    plt.show()
    figname = "/work/mh0066/m300971/Output/850zg_JJA.png"
    plt.savefig(figname)
    
    
    
def plot_slp(lon, lat, slp, u, v, figname, subname):
    latst=-90
    lated=90
    lonst=0
    loned=360
    
    fig=plt.figure(figsize=[10,10.5], dpi=200)    
    ax = plt.subplot(111,projection=ccrs.PlateCarree(central_longitude=(lonst+loned)/2))
    ax = cartopy_map(ax,lon,lat,lonst,loned,latst,lated,subname)
    #a=ax.contourf(lon,lat,slp,cmap=cmaps.BlueDarkRed18,levels=np.arange(-4.5,4.6,0.5),extend="both",transform=ccrs.PlateCarree())
    a=ax.contourf(lon,lat,slp,transform=ccrs.PlateCarree())
    b=ax.contour(lon,lat,slp,colors="k",linewidths=0.5,transform=ccrs.PlateCarree())
    plt.clabel(b,fontsize=7,colors="k",fmt="%.1f")
    h1=ax.quiver(lon[::4],lat[::4],u[::4,::4],v[::4,::4],color='gray',width=0.002,scale=1300,transform=ccrs.PlateCarree())
    font={'family' : 'serif',
          'weight' : 'normal',
          'size'   : 8}
    ax.quiverkey(h1,                         #传入quiver句柄
                 X=0.8, Y=-0.1,              #确定label所在位置，图片在[0,1]之间
                 U=70,                       #参考箭头长度 表示风速为70m/s
                 angle=0,                    #参考箭头摆放角度。默认为0，即水平摆放
                 label='70m/s',              #箭头的补充：label的内容
                 labelpos='S',               #label在参考箭头的哪个方向; S表示南边
                 color='k',labelcolor='k',   #箭头颜色 + label的颜色
                 fontproperties = font)
    plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.1)
    plt.savefig(figname)
    
    
def cartopy_map(ax,lon,lat,lonst,loned,latst,lated,subname):
    ax.coastlines(resolution='50m',lw=0.4,color='grey')
    img_extent=[lonst,loned,latst,lated]
    ax.set_extent(img_extent,crs = ccrs.PlateCarree())
    ax.set_xticks([0,30,60,90,120,180,210,240,270,300,330], crs=ccrs.PlateCarree())         #指定要显示的经纬度
    ax.set_yticks([-90,-60,-30,0,30,60,90], crs=ccrs.PlateCarree())
    ax.xaxis.set_major_formatter(LongitudeFormatter())                           #刻度格式转换为经纬度样式
    ax.yaxis.set_major_formatter(LatitudeFormatter())
    ax.tick_params(axis='both',which='major',labelsize=7,direction='out',length=4,width=0.5,pad=0.2,top=True,right=True)
    ax.minorticks_on()
    ax.tick_params(axis='both',which='minor',direction='out',width=0.3,top=True,right=True)
    ax.spines['geo'].set_linewidth(0.5)                                         #调节边框粗细
    ax.set_title(subname,fontsize=9,fontweight='bold')
    
    return ax
    
def smooth(A):
    from scipy import ndimage
    B = ndimage.gaussian_filter(A,sigma=2)
    return B

if __name__ == "__main__":
    main()