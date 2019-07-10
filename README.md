# aml_2019_gd
Gradient Descent
In most of the machine learning applications, the objective is to minimize a loss function. To achieve this, one of the most common methods is gradient descent. Gradient descent is an algorithm that iteratively adjusts the parameters in order to minimize the loss function. In every iteration, the gradient or slope of the loss function is estimated and the parameters are tweaked in the opposite direction (if the slope is positive (negative) they are decreased (increased)). This procedure continues until the loss function reaches a minimum. One important hyper-parameter is the learning rate or step size. This hyper-parameter defines how much the parameters will be altered subject to the gradient value. If the learning rate is too small, then it will take a long time for the algorithm to converge. On the other hand, if the learning rate is too high, the algorithm may diverge because it would overcome the minimum and end up on a point with even higher gradient.

![image](https://user-images.githubusercontent.com/52329752/60841552-fefcf580-a1c9-11e9-8989-f63ca363e2e8.png)

For the plain vanilla gradient descent, the learning rate is set to be constant. Therefore, the size of the movement solely depends on the gradient at the specific location in the loss function. However, as the point approaches the minimum, the gradient gets smaller and smaller which results in smaller movement steps. This leads to a slower convergence to the minimum. In addition, if the point approaches a saddle point where the gradient is zero, but it is not a minimum, the plain vanilla gradient descent will fail to find the global minimum and take the saddle point as the solution of the algorithm. This issue is due to the learning rate used, since if the step size was large enough, it could go through the saddle point. On the other hand, if the step size was too large, the algorithm would diverge and could not find any solution.

As a result, there are variants of gradient descent developed. In this project, we will demonstrate two types which are Momentum and RMSprop gradient descent. The addition of Momentum on the plain vanilla is that the size of movement also depends on the gradient at previous points. This makes the algorithm to converge faster, as it approaches a minimum in fewer steps due to the accumulated momentum of previous more steep points. Furthermore, this behaviour might also help to overcome saddle points. The development of RMSprop is that the step size is reduced as it goes through iterations. This allow us to have larger step sizes in the very first iterations which make convergence faster.

In this project, we will demonstrate the gradient descent algorithm via Six-Hump Camel function as shown in figure below. The optimization path will be shown in 3D diagram as well as an animation (running in Colab). Additionally, the interactive animation can be used to see the effects of each parameter on the algorithm. A heatmap graph was also used to demonstrate the speed of convergence for different parameters.

<p align="center">
  <img width="572" height="286" src="https://user-images.githubusercontent.com/52329752/60832682-660faf80-a1b4-11e9-8e93-9dd6117c7204.png">
</p>

The fastest convergence of each gradient descent along with their hyperparameters are shown below.
 
 | Algorithms | NO of Iterations | Learning rate (Eta) | Another Hyperparameter |
| :---:        |     :---:      |          :---: | :---: |
| Plain vanilla Gradient Descent   | 11   | 0.08212    |-|
| Momentum  Gradient Descent     | 9       | 0.07411     |0.08273|
| RMSprop  Gradient Descent     | 6       | 0.1603      |0.898|

RMSprop Gradient Descent has the fastest convergence with 6 iterations. This was accomplished by allowing large movements during the first iterations and shorter movements as it went through iterations. This behaviour prevents diverging from the minimum. The second fastest algorithm was Momentum Gradient Descent. Its learning rate was much smaller than that of RMS prop and slightly lower than that of plain vanilla, since it accounts of the gradient on previous positions. Therefore, it needed a lower learning rate than that of plain vanilla to reach the minimum. However, the optimal reported values are only for the given starting point and loss function.
