Title: PCA and Mahalanobis Distance
Date: 2016-05-13 10:57
Category: machine learning

# PCA

 $(X^{T} X)V=V \Lambda$  
 $\to (X^{T} X)^{-1} = C _ {X}^{-1} = V\Lambda^{-1} V^{-1} = V\Lambda^{-1} V^{T}$  
 $\to C _ {X}^{-1} = V\Lambda^{-1} V^{T}$

where $C_X$ is the kernel matrix of $X$. From this, it's intuitive that if we decompose the original kernel matrix $K^{-1}$ in $chrosky$, i.e.
$$K^{-1}=L^{T}L \to X^T(L^T L)X = (LX)^T (LX) = I$$
, the component $L$ actually linearly maps $X$ to a space that $XL$ are features-independent with $variance$ all equal to $1$, hence a normalized metric for $distance(x_1,x_2)$ is built, that
$$distance(x_1,x_2)=(x_1-x_2)^T K^{-1} (x_1-x_2)$$

## Case study
Let $X$ be `RAND(100,4)` and compute $$ V\Lambda^{-1} V^{T} -(X X^{T})^{-1} $$, and the result is `ZERO(4,4)`, showing that $C _ {X}^{-1} = V\Lambda^{-1} V^{T}$ exists.


```python
import numpy as np
import matplotlib.pyplot as plt


X=np.random.rand(100, 4)
X-=np.mean(X, axis=0)
C=X.transpose().dot(X)
LD,V=np.linalg.eig(C)

print np.linalg.inv(C) - V.dot(np.diag(1/LD).dot(V.T))
```

    [[  5.55111512e-17   5.37764278e-17   2.34187669e-17  -5.20417043e-17]
     [  5.46437895e-17  -1.94289029e-16  -9.19403442e-17   2.60208521e-18]
     [  9.54097912e-18  -9.19403442e-17   5.55111512e-17  -4.51028104e-17]
     [ -4.85722573e-17   8.67361738e-18  -3.81639165e-17   4.16333634e-17]]
    
