import matplotlib.pyplot as plt


class Analytics:

    def __init__(self):
        self._x = []
        self._y = []

    def add_data(self, x, y):
        self._x.append(x)
        self._y.append(y)

    def draw(self, title, ylabel):
        fig, ax = plt.subplots()
        ax.plot(self._x, self._y)
        ax.set(xlabel="Iterations", ylabel=ylabel, title=title)
        plt.show()