from plotly.tools import mpl_to_plotly

def create_sine_graph():
    fig, ax = plt.subplots()
    x = np.range(0, 3 * np.pi, 0.1)
    ax.set_title("Sine Wave Form")
    ax.plot(x, np.sin(x), "r--")
    return mpl_to_plotly(fig)

