import numpy as np
import matplotlib.pyplot as plt

def plot_log():
    import ipdb; ipdb.set_trace()
    fig, ax = plt.subplots()
    x = np.logspace(1, 2, 10)
    ax.plot(x, np.log(x))
    plt.show()

plot_log()