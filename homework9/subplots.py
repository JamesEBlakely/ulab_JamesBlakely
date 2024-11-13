# File name: subplots.py

import numpy as np
import matplotlib.pyplot as plt

def horizontal_subplots(lower,upper):
    # Displays subplots side-by-side
    x = np.linspace(lower,upper,100)
    h = np.cos(x)
    k = np.sin(x)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    plt.suptitle("Horizontal subplots")
    ax1.plot(x,h)
    ax2.plot(x,k)   
    ax1.set(xlabel="x",ylabel="y")
    ax2.set(xlabel="x",ylabel="y")


def vertical_subplots(lower,upper):
    # Displays subplots stacked vertically
    x = np.linspace(lower,upper, 100)
    h = np.cos(x)
    k = np.sin(x)
    fig, axs = plt.subplots(2)
    plt.suptitle("Vertical subplots")
    axs[0].plot(x,h)
    axs[1].plot(x,k)
    axs[0].set_xlabel("x")
    axs[1].set_xlabel("x")
    axs[0].set_ylabel("y")
    axs[1].set_ylabel("y")
    plt.show()