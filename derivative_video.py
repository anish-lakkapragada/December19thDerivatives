# ahh, doesn't it feel good to actually use python

import warnings
warnings.filterwarnings("ignore") # screw it 

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import imageio
from tqdm import tqdm 

def slope(x, f):
    # yeah, yeah finite differentiation approximation !goess brr
    return (f(x + 0.001) - f(x)) / 0.001

def line(x, x1, y1, f): 
    return slope(x1,f)*(x - x1) + y1

def plot_derivative(a, b, f, video_name = "deriv.mp4", pres = 0.01): 
    """
        Plots the tangent lines and creates an image video. 
    """

    iterations = (b - a) / pres
    X_s = np.linspace(a, b, int(iterations))
    Y_s = np.vectorize(f)(X_s)
    

    plt.ylim(np.min(Y_s), np.max(Y_s))
    IMAGES = []
    length = b - a
    
    DYDX = []

    for i in tqdm(range(len(X_s))): 

        x1 = X_s[i]
        y1 = Y_s[i]
        
        fig = plt.figure() # create the figure 
        deriv =  round(slope(x1, f), 3)
        plt.title(f"Derivative @ ({round(x1, 2)}, {round(y1,2)}) : {deriv}")
        DYDX.append(deriv)

        plt.plot(X_s, Y_s)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.scatter(x1, y1, color='C1', s=50)
        xrange = np.linspace(max(x1 - 0.1 * length, a), min(b, x1 + 0.1 * length), 100)
        plt.plot(xrange, line(xrange, x1, y1, f), 'C1--', linewidth = 2)
    

        canvas = FigureCanvas(fig)
        canvas.draw()
        IMAGES.append(np.array(canvas.renderer._renderer))
    
    # plot the entire derivative graph 
    fig = plt.figure()
    plt.title("f(x) vs. f'(x)")
    plt.plot(X_s, Y_s, label="f(x)")
    plt.plot(X_s, DYDX, label="f'(x)")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()


    canvas = FigureCanvas(fig)
    canvas.draw()

    for i in range(int(0.05 * iterations)): 
        IMAGES.append(np.array(canvas.renderer._renderer))
    
    # rita would be proud

    imageio.mimsave(video_name, IMAGES)


