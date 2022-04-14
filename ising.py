import numpy as np
import random
import os as os
import matplotlib.pylab as plt


art=("_______________________________________________________________________________________________\n"
" _  _  _             _  _  _  _            _  _  _           _           _           _  _  _\n"       
"(_)(_)(_)          _(_)(_)(_)(_)_         (_)(_)(_)         (_) _       (_)       _ (_)(_)(_)(_)\n"   
"   (_)            (_)          (_)           (_)            (_)(_)_     (_)      (_)         (_)\n"   
"   (_)            (_)_  _  _  _              (_)            (_)  (_)_   (_)      (_)    _  _  _ \n"   
"   (_)              (_)(_)(_)(_)_            (_)            (_)    (_)_ (_)      (_)   (_)(_)(_)\n"   
"   (_)             _           (_)           (_)            (_)      (_)(_)      (_)         (_)\n"   
" _ (_) _          (_)_  _  _  _(_)         _ (_) _          (_)         (_)      (_) _  _  _ (_)\n"   
"(_)(_)(_)           (_)(_)(_)(_)          (_)(_)(_)         (_)         (_)         (_)(_)(_)(_)\n"
"_______________________________________________________________________________________________\n")    
print(art)

def aleatorio(A):
    for i in range(fil):
        for j in range(col):
            A[i,j]=random.choice(spin)

    np.savetxt("spin.txt",A,fmt='%1i')
    return A

def ajedrez(A):
    A[0,0]=1
    for i in range(fil-1):
        A[i+1,0]=-A[i,0]
    for j in range(col-1):
        A[:,j+1]=-A[:,j]
    np.savetxt("spin.txt",A,fmt='%1i')
    return A
        


def fundamental(A):
    for i in range(fil):
        for j in range(col):
            A[i,j]=1

    np.savetxt("spin.txt",A,fmt='%1i')
    return

fil=int(input("Number of Rows: "))
col=int(input("Number of Columns: "))
t=float(input("Initial Temperature: "))
tf=float(input("Final Temperature: "))
ts=float(input("Temperature Step: "))
equil=(input("Iterations until Termalization: "))
mc=int(input("MonteCarlo Iterations: "))
simu=int(input("Save Simulation 1-Yes, 2-No: "))
A=np.zeros([fil,col])
spin=[-1,1]

B=np.zeros([8,1])
B[0,0]=fil
B[1,0]=col
B[2,0]=t
B[3,0]=tf
B[4,0]=ts
B[5,0]=equil
B[6,0]=mc
B[7,0]=simu
np.savetxt("in.txt",B)
opcion={1:aleatorio,
        2:ajedrez,
        3:fundamental,
        }
        

print("Initial Configuration \n")
print("1-Ramdon\n2-Chess\n3-Fundamental")
seleccion=int(input())
A=opcion[seleccion](A)

opcion={1:"Ramdon",
        2:"Chess",
        3:"Fundamental",
        }

if not os.path.exists("results"):
    os.mkdir(f"{os.getcwd()}/results")
os.system("cls")
print(art)
print(f"Compiling using {fil}x{col} and spin {opcion[seleccion]}")
os.system("gfortran mt19937.f90 ising.f90 -o ising.exe")
print("Executing Program")
os.system(f"ising.exe <in.txt")
print("Done!!!!")
print("Plotting Initial & Final state")
fig,ax=plt.subplots(1,2)
Si=np.loadtxt("spin.txt")
Sf=np.loadtxt("spin_f.txt")

ax[0].imshow(Si)
ax[0].set_title("Initial State")
ax[1].imshow(Sf)
ax[1].set_title(f"Final State at T={tf}")
plt.show()




print("Plotting the Results!")
A=np.loadtxt("results.txt")
fig,ax =plt.subplots(2,2,figsize=(10,5))
plt.suptitle(f"{fil}x{col} Grid")
yaxis=["Energy","Cv","M","X"]
title=["Energy","Specific Heat","Magnetization","Susceptibility"]

k=0
for i in range(2):
    for j in range(2):
        ax[i,j].plot(A[:,4],A[:,k],"+")
        ax[i,j].set_title(f"{title[k]}")
        ax[i,j].set_xlabel("T")
        ax[i,j].set_ylabel(f"{yaxis[k]}")
        ax[i,j].grid()
        k=k+1
plt.show()

if (simu==1):
    j=0
    for i in os.listdir(f"{os.getcwd()}/results"):
        plt.cla()
        terma=np.loadtxt(f"{os.getcwd()}/results/{j}.txt")
        plt.title(f"iteracion {j}")
        plt.imshow(terma)
        plt.draw()
        plt.pause(0.01)
        j=j+1  