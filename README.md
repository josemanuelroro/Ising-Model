# Ising Model
## Study of second-order phase transitions using the Ising Model

Ising's model is a qualitative model to study second-order phase transitions in ferromagnetic materials. When the temperature  which a ferromagnetic is subjected reaches a certain value, it loses his magnetic properties. This temperature is known as the Curie temperature. At this point, the second order phase-transitions occurs.

In this model the energy is expressed as:


![](https://latex.codecogs.com/gif.latex?E%3D-J%5Csum_%7B%3Cij%3E%7D%5E%7BN%7Ds_%7Bi%7Ds_%7Bj%7D-B%5Csum_%7Bi%7D%5E%7BN%7Ds_%7Bi%7D)        


Where ![](https://latex.codecogs.com/gif.latex?s_%7Bi%7D) can be +1 or -1, N is the total number of spins, J is a copuling constant and can take positive or negative values. If J>0 the spins line up and at low temperatures they all point in the same direction. As the temperature increases, the thermal agitation ends up defeating the coupling between spins and the spins tend to point randomly. B is the external magnetic field that we will consider 0.

Our 2D lattice has the next configuration



![alt text](https://github.com/josemanuelroro/Ising_model/blob/main/spin.png?raw=true)



To limit the effects of having a finite size we are going to consider infinite boundary conditions where the first and last rows and columns interact with each other.


The energy as we see earlier is expressed as:

![](https://latex.codecogs.com/gif.latex?E%3D-J%5Csum_%7B%3Cij%3E%7D%5E%7BN%7Ds_%7Bi%7Ds_%7Bj%7D)

Where the sum represents the interaction between first neighbors as seen in the following image, the particle in the red position interacts with its closest neighbors marked in blue and the energy would be calculated with the given expression

![alt text](https://github.com/josemanuelroro/Ising_model/blob/main/spin2.png?raw=true)

We want to calculate different magnitudes of the system, the energy, magnetization, specific heat and magnetic susceptibility.
