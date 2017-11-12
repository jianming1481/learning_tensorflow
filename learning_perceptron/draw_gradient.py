import numpy as np
import matplotlib.pyplot as plt

def m_func(X):
    return np.sum(X**2)

def numerical_gradient(f,x):
    h = 1e-4
    grad = np.zeros_like(x)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            grad[i][j] = (f(x[i][j]+h)-f(x[i][j]-h))/(2*h)
    return grad

if __name__ == '__main__':
    x = np.arange(-2, 2, 0.2)
    y = np.arange(-2, 2, 0.2)
    # Generate X,Y like a foto
    X, Y = np.meshgrid(x,y)
    # Calculate gradient on X-axis
    grad_x = numerical_gradient(m_func,X)
    # Calculate gradient on Y-axos
    grad_y = numerical_gradient(m_func,Y)
    plt.figure()
    plt.quiver(X, Y, -grad_x, -grad_y,  angles="xy",color="#666666")#,headwidth=10,scale=40,color="#444444")
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.xlabel('x0')
    plt.ylabel('x1')
    plt.grid()
    plt.legend()
    plt.draw()
    plt.show()
