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

To calculate the specific heat and magnetic susceptibility we must make use of statistical physics. In the canonical essemble, both magnitudes are defined as follows.


Where the sum represents the interaction between first neighbors as seen in the following image, the particle in the red position interacts with its closest neighbors marked in blue and the energy would be calculated with the given expression

![alt text](https://github.com/josemanuelroro/Ising_model/blob/main/spin2.png?raw=true)

We want to calculate different magnitudes of the system, the energy, magnetization, specific heat and magnetic susceptibility. The magnetization is calculated as follows

![](https://latex.codecogs.com/gif.latex?M%3D%5Csum_%7Bi%7D%5E%7Bn%7Ds_%7Bi%7D)


To calculate the specific heat and magnetic susceptibility we must make use of statistical physics. In the canonical essemble, both magnitudes are defined as follows.

![](https://latex.codecogs.com/gif.latex?C_%7Bv%7D%3D%5Cfrac%7B%5Cpartial%20%3CE%3E%7D%7B%5Cpartial%20T%7D%3D%5Cfrac%7B%5Cbeta%20%7D%7BT%7D%5B%3CE%5E%7B2%7D%3E-%3CE%3E%5E%7B2%7D%5D)

![](https://latex.codecogs.com/gif.latex?%5Cchi%20%3D%5Cfrac%7B%5Cpartial%20%3CM%3E%7D%7B%5Cpartial%20T%7D%3D%5Cbeta%20%5B%3CM%5E%7B2%7D%3E-%3CM%3E%5E%7B2%7D%5D)

The procedure is as follows. We start from an initial configuration of spins that will be defined in the program.
We will flip a random spin of the system and calculate the energy difference between the system in the original state and the state after flipping the spin.
If the energy difference is less than 0 this means that the new state is energetically favorable and we accept it. However if the energy difference is greater than 0 there is still a small probability that the system will stay in this new configuration with the spin flipped. This is where the metropolis algorithm comes into play, which allows us to calculate the probability of transition from one configuration to another using the Bolztman distribution.

![](https://latex.codecogs.com/gif.latex?w%3D%5Cfrac%7Bf%28trial%29%7D%7Bf%28initial%29%7D)

The image above shows the transition probability using the metropolis algorithm where we measure the relationship that exists between the test state and the initial state and f represents a certain probability distribution that in our case will be Bolztman's


![](https://latex.codecogs.com/gif.latex?f%3D%5Cfrac%7Be%5E%7B-%5Cbeta%20E%7D%7D%7BA%7D)

A is a normalization constant that we can omit.
Summarizing all of the above, the procedure would be as follows.

1. We choose a random position and flip it.
2. Calculamos la diferencia de energia entre el estado prueba y el inicial ![](https://latex.codecogs.com/gif.latex?%5CDelta%20E)
3. If ![](https://latex.codecogs.com/gif.latex?%5CDelta%20E%5Cleq%200) we accept the test state with the espin flipped as valid since the system energy is lower than the initial state.
4. If ![](https://latex.codecogs.com/gif.latex?%5CDelta%20E%3E%200) we compute ![](https://latex.codecogs.com/gif.latex?w%3De%5E%7B%5Cbeta%20%5CDelta%20E%7D)
5. We genererate a random number r(0,1). If ![](https://latex.codecogs.com/gif.latex?r%5Cleq%20w) then accept the new configuration

As we can see, although the energy of a state when turning the spin is greater than that of the initial state, there is still a small probability of transition to this new configuration, even if it is not energetically favorable.

## Thermalization

As we said at the beginning at low temperature all the spins are aligned towards the same direction, as the temperature increases the thermal agitation causes the spins to begin to reorder randomly.
If we want our problem to be faithful to physical reality, we cannot start calculating the expected values of the magnitudes we want directly. When we increase the temperature, we have to wait for the system to reach a "steady" state for that temperature, this is what we call thermalization.
For example, let us consider that we take an initial configuration of spin in which all are aligned in the same direction, we know that this configuration is only valid at low temperatures. However we take this configuration for T>>0 and start calculating the expected values. We will find erroneous results since this configuration does not describe the system for T>>0 for this temperature the spins would be randomly distributed. Therefore, we have to wait for the system to thermalize before calculating anything.
