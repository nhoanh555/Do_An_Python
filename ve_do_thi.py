import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
def ve_do_thi_yen_ngua():
    def ham_Rosenbrock(x, y):
        z = (x/3)**2-(y/2)**2
        return z
    x = np.linspace(start=-40.0, stop=40.0,num=100)
    y = np.linspace(start=-40.0, stop=40.0,num=100)
    x, y = np.meshgrid(x, y)
    z = ham_Rosenbrock(x, y)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    rosen_surf = ax.plot_surface(x, y, z,cmap=cm.gist_heat_r,linewidth=0, antialiased=False)
    ax.set_zlim(-250, 250)
    plt.show()


def ham_hyperbolic(x, y):
    z = 2 * ((x / 3) ** 2 + (y / 5) ** 2 - 1) ** 1 / 2
    return z
def ve_hyperbolic():
    x = np.linspace(start=-5, stop=5, num=2000)
    y = np.linspace(start=-5, stop=5, num=2000)
    x, y = np.meshgrid(x, y)
    a = ham_hyperbolic(x, y)
    b = - ham_hyperbolic(x, y)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(x, y, a, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
    ax.plot_surface(x, y, b, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
    ax.set_zlim(-7, 7)
    plt.show()


def mat_cau0():
    def mat_cau1(x, y):
        z = (4 - (x + 2) ** 2 - (y - 1) ** 2) ** (1 / 2) + 4
        return z

    def mat_cau2(x, y):
        z = -(4 - (x + 2) ** 2 - (y - 1) ** 2) ** (1 / 2) + 4
        return z

    x = np.linspace(-5, 1, 100)
    y = np.linspace(-2, 4, 100)
    x, y = np.meshgrid(x, y)
    a = mat_cau1(x, y)
    b = mat_cau2(x, y)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(x, y, a, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
    ax.plot_surface(x, y, b, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
    ax.set_zlim(2, 7)
    plt.show()

def main():
    ve_do_thi_yen_ngua()
    ve_hyperbolic()
    mat_cau0()

if __name__=="__main__":
    main()