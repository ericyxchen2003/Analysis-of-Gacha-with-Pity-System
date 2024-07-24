# Analysis of Pulls with a Pity System

---

## Introduction

Nowadays, more and more games are introducing a pity system in their gacha systems. A pity system guarantees that if a player does not obtain a certain prize after a certain number of pulls, the next pull is guaranteed to be the prize. We want to look into the behaviour  of such system.

For example, in the game *Genshin Impact*, the chance of pulling out a 5-star character is $0.6$% for each wish but the player is guaranteed to win a 5-star character in the $90$-th wish if the player fails to obtain any 5-star character in the previous $89$ wishes.

## Assumption

Assume that for each pull, the probability of obtaining a grand prize is $p$. The pity system guarantees that if a player does not obtain any grand prize after $N-1$ pulls, the $N$-th pull is guaranteed to be the grand prize. Assume that the player starts from the first pull.

## Definition

Let $T$ be the random variable of the pulls to obtain a grand prize. Its probability mass function is given by
```math
f_{T}(x)=\begin{cases}
\left(1-p\right)^{x-1}p&x=1,2,\ldots,N-1,\\
\left(1-p\right)^{x-1}&x=N.
\end{cases}
```
One can see that the distribution of $T$ is similar to a geometric distribution, but $f_T$ has a finite domain.

It follows that the cummulative distribution function is given by
```math
F_{T}\left(x\right)=\begin{cases}
1-\left(1-p\right)^x&x=1,2,\ldots,N-1,\\
1&x=N.
\end{cases}
```
## Cummulative Distribution Function
Take $p=0.006$,  $N = 90$ and plot the graph of the cummulative distribution function $F_T$:

![Cummulative Distribution Function](/GRAPH/CDF.png)

We can see that there is a huge gap between $F_T(89)$ and $F_T(90)$. By the definition of $F_{T}(x) = \mathbb{P}\circ T^{-1}\left((-\infty, x]\right)$, we can conclude that there is less than a $0.4$ chance of obtaining a grand prize in the first $89$ pulls.

## Expectation

Consider the moment generating function:
```math
M_T\left(t\right) = \mathbb{E}e^{tT}=\sum_{i=1}^{N-1}e^{ti}\left(1-p\right)^{i-1}p+e^{tN}\left(1-p\right)^{N-1}
```
Since
```math
M_{T}\left(t\right)=\frac{p}{1-p}\sum_{i=1}^{N-1}\left(e^t\left(1-p\right)\right)^{i} + e^{tN}\left(1-p\right)^{N-1},
```
we have 
```math
M_{T}\left(t\right)=\frac{p}{1-p}\cdot\frac{e^t\left(1-p\right)-\left(e^t\left(1-p\right)\right)^N}{1-e^t\left(1-p\right)}+e^{tN}\left(1-p\right)^{N-1}.
```
 
Next, compute the derivatives:
```math
\frac{\mathrm{d}}{\mathrm{d}t}M_{T}\left(t\right) =pe^t\cdot\frac{1-N\alpha^{N-1}+\left(N-1\right)\alpha^N}{\left(1-\alpha\right)^2}+N\left(1-p\right)^{N-1}e^{tN},
```
where
```math
\alpha = e^t\left(1-p\right).
```
Therefore, the expectation of $T$ is given by:
```math
\left.\frac{\mathrm{d}}{\mathrm{d}t}M_{T}\left(t\right)\right|_{t=0} = \mathbb{E}T = \frac{1-\left(1-p\right)^N}{p}.
```
It is easy to see that $\mathbb{E}T$ is similar to but slightly less than $\mathbb{E}T'=\frac{1}{p}$, where $T'\sim \mathrm{Geom}\left(p\right)$.

It is also not suprising to see that
```math
\lim_{N\rightarrow\infty}\mathbb{E}T=\frac{1}{p},\quad\lim_{p\uparrow 1}\mathbb{E}T = 1\quad\text{and}\quad\lim_{p\downarrow 0}\mathbb{E}T=N.
```

## Variance
Compute the second order derivative of the moment generating function:
```math
\frac{\mathrm{d}^2}{\mathrm{d}t^2}M_T\left(t\right) = p e^t\frac{\beta}{\left(1-\alpha\right)^2} + p(1-p)e^{2t}\frac{N\left(N-1\right)\left(\alpha^{N-1}-\alpha^{N-2}\right)}{\left(1-\alpha\right)^2} + 2p(1-p)e^{2t}\frac{\beta}{\left(1-\alpha\right)^3}+N^2\left(1-p\right)^{N-1}e^{tN},
```
where
```math
\beta = 1-N\alpha^{N-1}+\left(N-1\right)\alpha^N.
```
Therefore, the second order moment is given by
```math
\left.\frac{\mathrm{d}^2}{\mathrm{d}t^2}M_T\left(t\right)\right|_{t=1}=\mathbb{E}T^2 =\frac{-\left(\left(2N-1\right)p+2\right)\left(1-p\right)^N-p+2}{p^2} .
```
By $\mathrm{Var} T=\mathbb{E}T^2-\left(\mathbb{E}T\right)^2$, 
```math
\mathrm{Var}T = \frac{1-p - \left(2N-1\right)p\left(1-p\right)^N-\left(1-p\right)^{2N}}{p^2}.
```
For $T'\sim \mathrm{Geom}\left(p\right)$, the variance is given by $\mathrm{Var}T'=\frac{1-p}{p^2}$.
Hence, it is not difficult to see that
```math
\mathrm{Var}T < \mathrm{Var}T',\quad\lim_{N\uparrow\infty}\mathbb{E}T=\mathbb{E}T'\quad\text{and}\quad\lim_{p\uparrow1}\mathbb{E}T=0.
```
