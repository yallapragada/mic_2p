'''
Created on Jul 21, 2015
@author: uday
'''

import sys
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
from numpy import array

def zipFile(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    values=[]
    list_of_lists=[]
    for line in lines:
        values=line.split(",")
    list_of_lists.append(values)    
    x,y,z=zip(*list_of_lists)
    return int(x[0]),int(y[0])

def readFile(filename,xmax,ymax):
    f = open(filename)
    lines = f.readlines()
    f.close()
    mic = [[0.0 for y in range(ymax+1)] for x in range(xmax+1)]
    print(len(mic), " ", len(mic[0]))
    x_old=0
    x=0
    residues=[]
    for line in lines[1:]:
        values=line.split(",")
        x=int(values[0])
        y=int(values[1])
        mic[x][y]=round(float(values[2]),2)
        if mic[x][y]>0.2:
            residues.append(y)
        if(x!=x_old):
            print(residues)
            residues=[]
        x_old=x  
    return mic

def create_2_plots_v(mic1, mic2, title1, title2, xlabel1, ylabel1, xlabel2, ylabel2, colormap):

    fig, axes = plt.subplots(2, sharex=True)
    mic_array = array(mic1)
    dimensions = mic_array.shape
    nx = dimensions[0]
    ny = dimensions[1]
    axes[0].imshow(mic1, extent=(0, nx, ny, 0),cmap=cm.get_cmap(colormap))
    axes[0].set_title(title1)
    axes[0].set_xlabel(xlabel1)
    axes[0].set_ylabel(ylabel1)
    axes[0].set_ylim([0,ny])
    
    mic_array = array(mic2)
    dimensions = mic_array.shape
    nx = dimensions[0]
    ny = dimensions[1]
    print(nx, ny)
    axes[1].imshow(mic2, extent=(0, nx, ny, 0),cmap=cm.get_cmap(colormap))
    axes[1].set_title(title2)
    axes[1].set_xlabel(xlabel2)
    axes[1].set_ylabel(ylabel2)
    axes[1].set_ylim([0,ny])
    plt.axis('tight')
    plt.autoscale(enable=True, axis='y', tight=True)

    plt.show()

def create_plot(mic,colormap,title,xlabel, ylabel):
    mic_array = array(mic)
    dimensions = mic_array.shape
    nx = dimensions[0]
    ny = dimensions[1]
    plt.imshow(mic, extent=(0, nx, ny, 0),cmap=cm.get_cmap(colormap))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.autoscale(enable=True, axis='y', tight=True)
    plt.show()
        
if __name__ == '__main__':
    
    print(len(sys.argv))
    input_file1 = sys.argv[1]
    title1=sys.argv[2]
    xlabel1=sys.argv[3]
    ylabel1=sys.argv[4]
    input_file2 = sys.argv[5]
    title2=sys.argv[6]
    xlabel2=sys.argv[7]
    ylabel2=sys.argv[8]
    colormap=sys.argv[9]
    
    xmax, ymax=zipFile(input_file1)
    mic1=readFile(input_file1,xmax,ymax)
    
    xmax, ymax=zipFile(input_file2)
    mic2=readFile(input_file2,xmax,ymax)
    
    create_2_plots_v(mic1, mic2, title1, title2, xlabel1, ylabel1, xlabel2, ylabel2, colormap)
    
    #create_plot(mic1,colormap,title1,xlabel1,ylabel1)