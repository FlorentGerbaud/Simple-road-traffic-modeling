import sys
import numpy as np
import matplotlib.pyplot as plt


#______________________________________________________ Parameters ______________________________________________________
#________________________________________________________________________________________________________________________

if len(sys.argv) != 3:
    print("Usage: python your_script_name.py a2 h")
    sys.exit(1)


accident=False
a2 = float(sys.argv[1])
h = float(sys.argv[2])



T = 10.0  # Total simulation time
n_steps = int(T / h)  # Number of time steps

#________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________



#______________________________________________________ Set of values (position, time) ______________________________________________________
#____________________________________________________________________________________________________________________________________________
x1Pos = np.zeros(n_steps)
x2Pos = np.zeros(n_steps)
time = np.zeros(n_steps)

# Initial conditions
time[0] = 0.0  # Initial time
x1Pos[0] = 2.0  # Initial value for x1 as specified
x2Pos[0] = 1.0  # Initial value for x2 as specified

#____________________________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________________________


#______________________________________________________ Functions ______________________________________________________________________
#____________________________________________________________________________________________________________________________________________

def x2_prime(t):
    return a2 * (x1Pos[t] - x2Pos[t])

def x1_prime():
    return 130 * (1000 / 3600)

#____________________________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________________________

#______________________________________________________ Resolution of the position for the carsEuler's explicit method ______________________________________________________________
#____________________________________________________________________________________________________________________________________________________________________________________

for t in range(1, n_steps):
    
    x1Pos[t] = x1Pos[t-1] + x1_prime() * h
    x2Pos[t] = x2Pos[t-1] + x2_prime(t-1) * h
    time[t] = time[t-1] + h
    if(x2Pos[t] >= x1Pos[t]):
        accident=True
        break
        
#____________________________________________________________________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________________________________________________________________


#______________________________________________________ Plotting ______________________________________________________________
#____________________________________________________________________________________________________________________________

if(accident==True):
    plt.figure(figsize=(10, 6))
    plt.plot(time[0:t+1], x1Pos[0:t+1], label='x1(t)')
    plt.plot(time[0:t+1], x2Pos[0:t+1], label='x2(t)')
    plt.xlabel('Time (s)')
    plt.ylabel('Distance (m)')
    plt.legend()
    plt.title('Accident case')
    plt.grid(True)
    plt.show()
else:
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(time, x1Pos, label='x1(t)')
    plt.plot(time, x2Pos, label='x2(t)')
    plt.xlabel('Time (s)')
    plt.ylabel('Distance (m)')
    plt.legend()
    plt.title('Position of the cars')
    plt.grid(True)
    plt.show()

#____________________________________________________________________________________________________________________________
#____________________________________________________________________________________________________________________________