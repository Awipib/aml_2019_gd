import os
import pandas as pd
import numpy as np
import pickle

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from ipywidgets import interact,interactive, fixed, interact_manual
import ipywidgets as widget
from IPython.display import HTML
from matplotlib import animation, rc

class camel_fn:

    def fn_loss(self):
        x1 = self.x[0]
        x2 = self.x[1]
        t1 = (4 - 2.1 * x1 ** 2 + x1 ** 4 / 3) * x1 ** 2
        t2 = x1 * x2
        t3 = (-4 + 4 * x2 ** 2) * x2 ** 2
        return t1 + t2 + t3

    def fn_grad(self):
        x1 = self.x[0]
        x2 = self.x[1]
        g1 = 8 * x1 - 2.1 * 4 * x1 ** 3 + 2 * x1 ** 5 + x2
        g2 = x1 - 8 * x2 + 16 * x2 ** 3
        return np.array([g1, g2])




class gdcls(camel_fn):

    def gd_pv_result(self,n_iter, starting_pt, eta, tol):
        
        self.n_iter = n_iter
        self.x = np.array(starting_pt)
        self.eta = eta
        self.tol = tol
        
        lst_loss = []
        lst_x = []
        lst_x1 = []
        lst_x2 = []
        loss_this = self.fn_loss()
        lst_loss.append(loss_this)
        lst_x.append(list(self.x))
        lst_x1.append(self.x[0])
        lst_x2.append(self.x[1])
        g = self.fn_grad()
        g_mag = np.sum(np.square(g))
        j = 0

        for i in range(self.n_iter):
            if g_mag < self.tol:
                break

            g = self.fn_grad()
            g_mag = np.sum(np.square(g))
            self.x += -self.eta * g

            # print(self.beta)
            loss_this = self.fn_loss()
            lst_loss.append(loss_this)
            lst_x.append(list(self.x))
            lst_x1.append(self.x[0])
            lst_x2.append(self.x[1])
            j += 1
        self.x1p = lst_x1
        self.x2p = lst_x2
        self.zp = lst_loss
        self.speedp=j
        return {'speed': j, 'min_value': lst_loss[-1], 'x_op': lst_x[-1], 'x_path': lst_x, 'x1_path': lst_x1,
                'x2_path': lst_x2, 'min_value_path': lst_loss}

    def gd_m_result(self,n_iter, starting_pt, eta, tol, beta):
        self.n_iter = n_iter
        self.x = np.array(starting_pt)
        self.eta = eta
        self.tol = tol
        self.beta = beta
        lst_loss = []
        lst_x = []
        lst_x1 = []
        lst_x2 = []
        loss_this = self.fn_loss()
        lst_loss.append(loss_this)
        lst_x.append(list(self.x))
        lst_x1.append(self.x[0])
        lst_x2.append(self.x[1])
        g = self.fn_grad()
        g_mag = np.sum(np.square(g))
        n = len(self.x)
        v = np.zeros(n)
        j = 0

        for i in range(self.n_iter):
            
            if g_mag < self.tol:
                break
            g = self.fn_grad()
            g_mag = np.sum(np.square(g))
            v = self.beta * v + self.eta* g
            self.x += -v
            # print(self.beta)
            loss_this = self.fn_loss()
            lst_loss.append(loss_this)
            lst_x.append(list(self.x))
            lst_x1.append(self.x[0])
            lst_x2.append(self.x[1])
            j += 1

        self.x1p = lst_x1
        self.x2p = lst_x2
        self.zp = lst_loss
        self.speedp=j
        return {'speed': j, 'min_value': lst_loss[-1], 'x_op': lst_x[-1], 'x_path': lst_x,
                'x1_path': lst_x1, 'x2_path': lst_x2, 'min_value_path': lst_loss}

    def gd_rms_result(self,n_iter, starting_pt, eta, tol, beta):
        
        self.n_iter = n_iter
        self.x = np.array(starting_pt)
        self.eta = eta
        self.tol = tol
        self.beta = beta
           
            
        lst_loss = []
        lst_x = []
        lst_x1 = []
        lst_x2 = []
        loss_this = self.fn_loss()
        lst_loss.append(loss_this)
        lst_x.append(list(self.x))
        lst_x1.append(self.x[0])
        lst_x2.append(self.x[1])
        g = self.fn_grad()
        g_mag = np.sum(np.square(g))
        n = len(self.x)
        v = np.zeros(n)
        j = 0
        e = 1e-8
        s = 0
        for i in range(self.n_iter):
            
            if g_mag < self.tol:
                break
            g = self.fn_grad()
            g_mag = np.sum(np.square(g))
            s = self.beta * s + (1 - self.beta) * g ** 2
            self.x += -self.eta * g / (s + e) ** 0.5

            # print(self.beta)
            loss_this = self.fn_loss()
            lst_loss.append(loss_this)
            lst_x.append(list(self.x))
            lst_x1.append(self.x[0])
            lst_x2.append(self.x[1])
            j += 1
        self.x1p = lst_x1
        self.x2p = lst_x2
        self.zp = lst_loss
        self.speedp=j
        return {'speed': j, 'min_value': lst_loss[-1], 'x_op': lst_x[-1],
                'x_path': lst_x, 'x1_path': lst_x1, 'x2_path': lst_x2, 'min_value_path': lst_loss}


    def gd_anim(self,med):
      # some codes are from http://louistiao.me/notes/visualizing-and-animating-optimization-algorithms-with-matplotlib/
        self.med=med
        fig = plt.figure(figsize=(10, 5))
        ax = plt.axes(projection='3d', elev=50, azim=-50)
        x1 = np.linspace(-1, 1, 50)
        x2 = np.linspace(-1, 1, 50)
        x1, x2 = np.meshgrid(x1, x2)
        t1 = (4 - 2.1 * x1 ** 2 + x1 ** 4 / 3) * x1 ** 2
        t2 = x1 * x2
        t3 = (-4 + 4 * x2 ** 2) * x2 ** 2
        z = t1 + t2 + t3

        ax.plot_surface(x1, x2, z, cmap=plt.cm.jet, rstride=1, cstride=1, alpha=0.5, linewidth=0)
        ax.plot([0.0898], [-0.7126], [-1.0316], 'r*', markersize=10)
        ax.plot([-0.0898], [0.7126], [-1.0316], 'r*', markersize=10)

        x1p = self.x1p
        x2p = self.x2p
        zp = self.zp
        
        
        if self.med=='pv':
            ledg='eta='+str(self.eta)+' with NO. of iterations='+str(self.speedp)
        else:
            ledg='[eta, beta]='+'['+str(self.eta)+', '+str(self.beta)+']'+' and NO. of iterations='+str(self.speedp)
            
        
        line, = ax.plot([], [], 'b', lw=2,label=ledg)
        line, = ax.plot([], [], 'b', lw=2)
        point, = ax.plot([], [], 'bo')

        def init():
            line.set_data([], [])
            line.set_3d_properties([])
            point.set_data([], [])
            point.set_3d_properties([])
            return line, point

        def animate(i):
            line.set_data(x1p[:i], x2p[:i])
            line.set_3d_properties(zp[:i])
            point.set_data(x1p[i - 1:i], x2p[i - 1:i])
            point.set_3d_properties(zp[i - 1:i])
            return line, point

        ax.set_xlabel('$x1$')
        ax.set_ylabel('$x2$')
        ax.set_zlabel('$z$')
        #ax.legend(loc='upper right',fontsize='x-small')
        ax.set_title('Optimized path with'+'\n'+ledg,fontsize='small')
        anim = animation.FuncAnimation(fig, animate, init_func=init,
                                       frames=np.array(x1p).shape[0], interval=500,
                                       repeat_delay=1, repeat=True, blit=True)

        HTML(anim.to_html5_video())
        rc('animation', html='html5')
        return anim

    def plot2Dpath(self, start_index):

        font = {'size': 18}
        matplotlib.rc('font', **font)
        fig = plt.figure(figsize=(20, 8))
        ax1 = fig.add_subplot(1, 2, 1)
        x1p = self.x1p
        x2p = self.x2p
        zp = self.zp
        n = len(zp)
        for i in np.arange(start_index, n - 1):
            if i == start_index:
                ax1.plot([x1p[i], x1p[i + 1]], [zp[i], zp[i + 1]], label='First Line')
            elif i == n - 2:
                ax1.plot([x1p[i], x1p[i + 1]], [zp[i], zp[i + 1]], label='Last Line')
            else:
                ax1.plot([x1p[i], x1p[i + 1]], [zp[i], zp[i + 1]])
        ax1.set_xlabel('x1')
        ax1.set_ylabel('loss')
        #ax1.legend()
        ax1 = fig.add_subplot(1, 2, 2)
        for i in np.arange(start_index, n - 1):
            if i == start_index:
                ax1.plot([x2p[i], x2p[i + 1]], [zp[i], zp[i + 1]], label='First Line')
            elif i == n - 2:
                ax1.plot([x2p[i], x2p[i + 1]], [zp[i], zp[i + 1]], label='Last Line')
            else:
                ax1.plot([x2p[i], x2p[i + 1]], [zp[i], zp[i + 1]])
        ax1.set_xlabel('x2')
        ax1.set_ylabel('loss')
        ax1.legend()

