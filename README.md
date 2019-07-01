# aml_2019_gd
Gradient Descent
In machine learning, there are several model developed. Additionally, the models have their own parameters which are needed to be set to suit the data in each circumference. In order to determine the suitability of those parameter, the loss function is used as measurement. As  the loss function is minimized, the set of paramters are more suiltable for those data. One of the most typical method used to achieve those paramter is gradient descent algorithm. The algorithm exploit the gradient of the function by taking a number of iterations to determine the minimum point. Going through iterations, the point is moved in opposite in direction to the gradient and stop at where the gradient is close to zero as shown in figure.





The size of movement depend on size of gradient as well as another paramter called step size. For the plain vanilla gradient desccent or the most common method in this kind of algorithm, the step size is set to be constant; therefore, the size of movement in the plain vanilla gradient desccent solely depend on the gradient at specific location in the loss function. However, as the point aproach the minimum point, the gradient get smaller and smaller which result in smaller size of movement. This lead to slower convergence to the minimum point. In addition, if the point approaches saddle point where the gradient is zero but it is not the minimum, the plain vanilla gradient descent will fail to find minimum point but take saddle point as solution of the algorithm. This issue is due to step size used in the algorithm since if the step size is large enough, it can go through the saddle point. However, if the step size is too large, the algorithm will diverge and can find the point where gradient is zero.


 As a result, there are variants of gradient descent developed. In this project, we will demonstrate two types which are Momentum and RMSprop gradient descent. The addition of the first method from the plain vanilla one is that the size of movement also depend  of the gradient at previous point which make the algorithm converge faster as it is close to minimum point and might be able to go through saddle point. The development of thesecond method is that the step size is reduced as go through iteration. This allow us to use larger step size in the very first iterations which make convergence faster.
 
 In this project, we will demonstrate the gradient descent algorithm via ......... function as shown in figure below. The optimization path will be shown in 3D diagram as well as the animation which can be seen in Colab. Additaionally, the interaactive animation can be used to see the effects of each parameter on the algorithm by running the code in your own notebook
