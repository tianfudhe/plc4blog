Title: BP and Artificial Neural Network
Date: 2016-05-13 20:34
Category: machine learning

To calculate the derivative of the parameters, we leverage the temp resutls computed of each layer to compute all the gradients backward, performing like a propagation.

![BP at `l` and `l+1` level]({filename}/images/bp/layer-l.png)

Given data $\mathcal{D}=\{X,y\}$.
  
Let $L-1$ denote the number of hidden layers, $n_l$ the neurals of $l^{th}$ layer, $W_l$ the weight matrix of $l^{th}$ layer, $o_l$ the input of $l^{th}$ layer, also the input of ${l+1}^{th}$ layer(of course $o_0$ is the input data $X$). We also define $z$ with
$$z _ {l+1}=W _ {l+1}o _ l+b _ {l+1}$$
$$o _ l=g(z _ l)$$
, where $g(x)$ is usually `sigmoid` or `ReLU` function. The rest of this article will take $g(x)=\frac{1}{1+e^{-x}}$

The objective function is to optimize the `l2-norm` of the prediction error that
$$J=\frac{1}{2}(o_L-y)^{T}(o_L-y)$$

After an epoch of `Feed Forward`, we have all $z_l$'s and $o_l$'s. However we don't derive the gradients directly, but the so called `Residual` $\delta_l$ instead. We shall see later how this item helps us to calculate the gradients. Define 
$$\delta_l=\frac{\partial J}{\partial z_l}$$
, so
$$\delta_L=\frac{\partial J}{\partial o_L} \frac{\partial o_L}{\partial z_L} = (o_L-y) \circ o_L \circ (1-o_L)$$
  
But what about $\delta_l$? We can simply calculate this item stepwise as usual, and we get
$$\delta_l = \frac{\partial J}{\partial z _ {l+1}} \frac{\partial z _ {l+1}}{\partial o_l} \frac{\partial o_l}{\partial z_l} = \delta_{l+1} \frac{\partial z _ {l+1}}{\partial o_l} \frac{\partial o_l}{\partial z_l}$$
  
This means that we only need to leverage the $\delta$ computed in the upper layer to get $\delta$ of this layer. While we get the $\delta_{l+1}$ of $n_{l+1}\times 1$ vector, the second item is
$$\frac{\partial z _ {l+1}}{\partial o_l}=\frac{\partial W _ {l+1}o _ l+b _ {l+1}}{\partial o_l}=W _ {l+1}$$
, which is a $n_{l+1}\times n_l$ matrix, and the multiplication apparently does not work. Why? **This is because that differential for vector-objected functions is actaully not allowed**, but simply making a hypothesis, we would believe it to be
$$\delta_l = (W_{l+1}^T \delta_{l+1})\frac{\partial o_l}{\partial z_l}$$
, actually this is true, and we can make element-wise differential to prove this:

>Let $z_l^i$ be the $i^{th}$ element of $z_l$, we have
$$\delta_l = \sum _{i=1} ^ {n_{l+1}} {\frac{\partial J}{\partial z _ {l+1}^i} \frac{\partial z _ {l+1}^i}{\partial o_l} \frac{\partial o_l}{\partial z _ l} } \\\
= \sum _{i=1} ^ {n_{l+1}} {\delta_{l+1}^i (W_{l+1})_{(i,:)} \frac{\partial o_l}{\partial z _ l} } \\\
= (W_{l+1}^T \delta_{l+1})\frac{\partial o_l}{\partial z_l} \\\
= (W_{l+1}^T \delta_{l+1}) \circ o_l \circ (1-o_l)$$

Now, with $\delta_l$, we can easily compute all the gradients of parameters,
$$\frac{\partial J}{\partial W_l} = \frac{\partial J}{\partial z_l} \frac{\partial z_l}{\partial W_l} = \delta_l \cdot o_{l-1}^T$$
$$\frac{\partial J}{\partial b_l} = \frac{\partial J}{\partial z_l} \frac{\partial z_l}{\partial b_l} = \delta_l$$
  
Now we can implement a toy Neural Network in `python`, [the source code is here](https://coding.net/u/tianfudhe/p/pynn/git).


```python
%matplotlib inline
import os
os.chdir('..')
from pynn import *
```

## The momentum
Momentum is a commonly used trick to jump out of local optima and speed up parameter updating.
  
In optimization, we would like to handle convex problems. However, in Neural Networks, the error surface is usually not ideal, that parameters might ran into some small local optimas. A solution for this, is adding a `momentum` to gradient update. More formally, in $i^{th}$ epoch, the updating of $W_l$ and $b_l$ in $l^{th}$ layer would be
$$\Delta W_l^i = - \frac{\partial J}{\partial W_l^i} - m \cdot \Delta W_l^i$$
, which can be interpreted as the remember of the last updating of parameter with a factor $m$. This remember would help adjusting the gradient still toward the global optimal as if it helps to jump out of local ones.
  
Besides, the momentum also acts as a "smooth" that to some extent weaken those gradient components irrelevant to the global optima, thus speeds up the process of training.

## Batch Learning vs. Stochastic Learning
It's know that we can conduct Stochastic Learning adapting Neural Network to online applications, besides, stochastic learning can also avoid local optima as the error surface would change given different training examples (**Error Surface Variance**). To these fruits of stochastic learning usually we would prefer it to batch algorithm.
  
However, unlike batch algorithm (**Matrix Manipulation**), stochastic learning solely iterate all examples in the very slooooow `loop` operation, discarding the fast matrix computation of the build-in math library. This problem would reveal apparently in morden languages such as `python`.
  
So, it's suggested to take a small subset at a time, called *mini-batch*, to conduct batch algorithm, which might be a good trade-off between **Matrix Manipulation** and **Error Surface Invariance**, therefore guarantees both efficiency and optima. *It should be noted that we cannot take too much examples during each batch epoch, as a sizable subset would be nearly sufficient representing the Error Bound of the whole data.*


```python
X,y=gen_fake_data(1600)
y=[np.roll([1,0], i) for i in  y]
mdl=nn([len(X[0]), 4,3,len(y[0])])
# 800 of 1600 batched each epoch
mdl.fit(X,y,10000, 800, 0.1, 0.75)
test_model(mdl, demo=True)

X,y=gen_fake_data(1600)
y=[np.roll([1,0], i) for i in  y]
mdl=nn([len(X[0]), 4,3,len(y[0])])
# 100 of 1600 batched each epoch
mdl.fit(X,y,10000, 100, 0.1, 0.75)
test_model(mdl, demo=True)
```


![png]({filename}/images/bp/output_4_0.png)



![png]({filename}/images/bp/output_4_1.png)





    array([[ 367.,    9.],
           [   3.,  421.]])



## Gaussian Discriminate Analysis, Logistic and Softmax
In K-classes classification tasks, we assume either class obeys a multi-variate gaussian distribution, then we have

- Shared ovariance matrix: $\Sigma$
- Mean vecotr: $\mu_0,\mu_1, \mu_2, \ldots, \mu_{K-1}$

Given $\mathcal{D} = \{X,y\}$, we can write the `likelihood` for $\mathcal{D}$ for model $\mathcal{M}=\{\Sigma, \mu_0,\mu_1, \mu_2, \ldots\}$,

$$p(\mathcal{D} \mid \mathcal{M})=\prod_{i=1}^{N}{\frac{p(X^{(i)} \mid y^{(i)};\mathcal{M})p(y^{(i)})}{\sum^K{p(X \mid y=k;\mathcal{M})p(y=k)}}}$$

and prior distribution for $y$ that $p(y=k)=\phi_k$, where $\phi_k>=0$ and $\sum^K{\phi_k}=1$, then the target model is learned by maximizing the `likelihood` function.

### A revisit of Logistic Regression
Logistic function $\sigma(o)$ is applied to perceptron learning as an activation function, linking the output value $o$ and the probability, by $\sigma(o)=1/e^{-o}$. One example of this is `logistic regression` where the linear boundary is soften by $\sigma(o)$, i.e., $y(x)=I[\sigma(\theta^T x)>0.5]$
  
From the view of GDA, we shall see the interesting relation between GDA and `logistic regression`. Assuming that the two classes of data obeys Gaussian distribution with means $\mu_0, \mu_1$ and shared distribution $\Sigma$, we have

$$p(y=1 \mid x)=\frac{p(x \mid y=1)p(y=1)}{p(x \mid y=0)p(y=0)+p(x \mid y=1)p(y=1)} = \frac{1}{1 + \frac{p(x \mid y=0)p(y=0)}{p(x \mid y=1)p(y=1)}} $$
$$\frac{p(x \mid y=0)p(y=0)}{p(x \mid y=1)p(y=1)}
= \frac{(1-\phi)}{\phi} \exp\{ -\frac{1}{2} ((x-\mu_0)^T \Sigma^{-1} (x-\mu_0) - (x-\mu_1)^T \Sigma^{-1} (x-\mu_1))\} \\\
= \frac{(1-\phi)}{\phi} \exp\{-\frac{1}{2}(\mu_0^T \Sigma^{-1} \mu_0 -\mu_1^T \Sigma^{-1} \mu_1)\} \exp\{ - (\mu_1 - \mu_0)^T\Sigma^{-1} x\}$$

, and the $\theta$ refered in `logistic function` is just $(\mu_1 - \mu_0)^T\Sigma^{-1}$ here.
### Softmax
From the last charpter we can see that $p(x|y=k)p(y=k)$ is in proportion to $p(x \mid y=l)p(y=l)$ by $Z \cdot \exp\{ - (\mu_k - \mu_l)^T\Sigma^{-1} x \}$, thus we sucessfully derive from GDA to softmax.
