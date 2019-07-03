# aml_2019_gd
Gradient Descent
In most of the machine learning applications, the objective is to minimize a loss function. For example, people would like to use machine learning to predict the sale price of a house with the objective that the predicted price is as close as possible to the actual price. Then, they might use some algorithm to predict the sale price, and the performance can be accessed by the absolute difference between the predicted and the actual sale price. The lower the difference, the better the performance is. Therefore, the loss function in this case is the absolute difference between the two prices. 

In order to minimize a loss function, one of the most common methods is gradient descent. Gradient descent is an algorithm that iteratively adjust the parameters in order to minimize the loss function. In every iteration, the gradient or slope of the loss function is estimated and the parameters are tweaked in the opposite direction (if the slope is positive (negative) they are decreased (increased)). This procedure continues until the loss function reaches a minimum. One important hyper-parameter of the gradient descent is the learning rate or step size. This hyper-parameter defines how much the parameters will be altered subject to the gradient value. If the learning rate is too small, then it will take a long time for the algorithm to converge. On the other hand, if the learning rate is too high, the algorithm may diverge because it would overcome the minimum and end up on a point with even higher gradient.

For the plain vanilla gradient desccent or the most common method in this kind of algorithm, the step size is set to be constant; therefore, the size of movement in the plain vanilla gradient desccent solely depend on the gradient at specific location in the loss function. However, as the point aproach the minimum point, the gradient get smaller and smaller which result in smaller size of movement. This lead to slower convergence to the minimum point. In addition, if the point approaches saddle point where the gradient is zero but it is not the minimum, the plain vanilla gradient descent will fail to find minimum point but take saddle point as solution of the algorithm. This issue is due to step size used in the algorithm since if the step size is large enough, it can go through the saddle point. However, if the step size is too large, the algorithm will diverge and can find the point where gradient is zero.


 As a result, there are variants of gradient descent developed. In this project, we will demonstrate two types which are Momentum and RMSprop gradient descent. The addition of the first method from the plain vanilla one is that the size of movement also depend  of the gradient at previous point which make the algorithm converge faster as it is close to minimum point and might be able to go through saddle point. The development of thesecond method is that the step size is reduced as go through iteration. This allow us to use larger step size in the very first iterations which make convergence faster.
 
 In this project, we will demonstrate the gradient descent algorithm via ......... function as shown in figure below. The optimization path will be shown in 3D diagram as well as the animation which can be seen in Colab. Additaionally, the interactive animation can be used to see the effects of each parameter on the algorithm by running the code in your own notebook, and the heatmap graph is also used to investigate the speed of convergence of sets of parameters. 

The fastest covergence of each gradient descent along with their hyperparamters are shown below.
 
 | Algorithms | NO of Iterations | Learning rate (Eta) | Another Hyperparameter |
| :---:        |     :---:      |          :---: | :---: |
| Plain vanilla Gradient Descent   | 11   | 0.08212    |-|
| Momentum  Gradient Descent     | 9       | 0.07411     |0.08273|
| RMSprop  Gradient Descent     | 6       | 0.1603      |0.898|


