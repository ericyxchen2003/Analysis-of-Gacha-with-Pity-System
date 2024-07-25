# Analysis of Gacha with a Pity System

---

Created by ericyxchen

## Introduction

Nowadays, more and more games are introducing a pity system in their gacha systems or lottery pools. A pity system guarantees that if a player does not obtain a certain prize after a certain number of pulls, the next pull is guaranteed to be the prize. 

For example, in the game *Genshin Impact*, the chance of pulling out a 5-star character is $0.6$% for each wish but the player is guaranteed to win a 5-star character in the $90$-th wish if the player fails to obtain any 5-star character in the previous $89$ wishes.

We want to look into the behaviour  of *the pity system*. Also, we will discuss *the 50/50 system* which is based on the pity system.

## Code

In the folder [./experiment](https://github.com/ericyxchen2003/Pulls-with-Pity-System/tree/main/experiment),  you can use the program to conduct experiments to verify the conclusions that follow.


## Assumption

Assume that for each pull, the probability of obtaining a grand prize is $p$. The pity system guarantees that if a player does not obtain any grand prize after $\left(N-1\right)$ pulls, the $N$-th pull is guaranteed to be the grand prize. Assume that the player starts from the first pull, which means that the player has never pulled before or just obtained a grand prize in his last pull.



## Definition

Let $T$ be the random variable of the waiting time of to obtain a grand prize. Its probability mass function is given by
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

We call such $T$ a random variable follows a geometric distribution with a pity system, denoted by 
```math
T\sim\mathrm{P-Geom}\left(p, N\right).
```

## Cummulative Distribution Function
Take $p=0.006$,  $N = 90$ and plot the graph of the cummulative distribution function $F_T$:

![Cummulative Distribution Function](/GRAPH/CDF.png)

We can see that there is a huge gap between $F_T(89)$ and $F_T(90)$. By the definition of $F_{T}(x) = \mathbb{P}\circ T^{-1}\left((-\infty, x]\right)$ and the fact that $F_T(89)$ is about $0.4$, we can conclude that there is about $0.6$ chance of not pulling out any grand prize until the guaranteed pull, i.e. the $90$-th pull.

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

Take $p=0.006$ and $N=90$. The expectation of the waiting time of the pulls is approximately to be $69.6998$, implying that it takes a player about $70$ pulls to obtain the grand prize on average. We can also say that it takes an average of about $70$ pulls between two grand prizes.

Define a random variable $\hat{T}\sim \mathrm{Geom}\left(q\right)$, where
```math
q = \frac{1}{\mathbb{E}T} = \frac{p}{1-\left(1-p\right)^N}.
```
We can see that $\mathbb{E}T=\mathbb{E}\hat{T}$.

With $q\approx 0.0144$ and the cummulative distribution function
```math
F_{\hat{T}}\left(x\right) = 1-\left(1-q\right)^x,\quad x=1,2,\ldots,
```
we can plot the graph of the function:

![Cummulative Distribution Function](/GRAPH/CDF-T-hat.png)

Although the function curve of $F_{\hat{T}}$ is smoother, it can be seen that there is still about a $0.2$ probability of not winning any  grand prize after $90$ pulls. Despite the fact that the two expectations are equal, the cummulative distribution function of the geometrically distributed random variable $\hat{T}$ implies that from the game publisher's point of view, about $20$ percent of players fail to win any grand prizes after $90$ pulls, which can cause players to give up playing the game.

The pity ensures that even if the average number of pulls required for a player to win the grand prize is the same, the player will definitely win the grand prize within the specified number of draws, encouraging players to continue investing.




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

Take $p = 0.006$ and $N = 90$. The variance of the waiting time of pulls to obtain a grand prize is approximately to be $851.4702$, which gives the standard deviation $\sigma_T \approx 29.1800$.

Consider the previous defined random variable $\hat{T}$. It follows that 
```math
\mathrm{Var}\hat{T}=\frac{1-q}{q^2}\approx 4788.3628,\quad \sigma_{\hat{T}}\approx 69.1980,
```
indicating that with the equal expectation, $T$ is more stable than $\hat{T}$.

We can conclude that a lottery pool with a pity system is more stable than one without a pity system while the expected investment of each player to obtain a grand prize is the same. This avoids the situation where players invest too much but no prizes are awarded, while also ensuring the revenue of game publishers.

## 50/50 System

In the game Genshin Impact, there is a lottery pool called a limited banner. When a player draws a 5-star character, the probability of drawing a specific character is higher than the other 5-star characters. If a 5-star character obtained from this banner is not the featured one, the next 5-star character that the player obtained from the banner is guaranteed to be the featured one. 

Now, we keep the previous assumptions and add new ones. We assume that there are $k$ categories for the grand prize. Assume that there are $k$ categories of the grand prize. One of them has a higher probability of being drawn. We call this category the featured prize. When the grand prize is drawn, there is a $0.5$ chance of drawing the featured prize, and a $0.5$ percent chance of drawing the remaining $\left(k-1\right)$ categories. If a grand prize obtained is not a featured one, the next grand prize that the player obtained is guaranteed to be the featured one.

Let $T^*$ be the random variable of the waiting time to obtain the featured prize. 

When a player obtains a featured prize, there are two situations:
- The first grand prize the player wins is the featured prize.
- If the first grand prize won by the player is not the featured prize, the draw will continue until the second grand prize is won. The 50/50 system ensures that the second grand prize will definitely be the featured prize.

With this idea, let $Y$ be the random variable of the number of the grand prize the player obtains, which is either $1$ or $2$. Let 
```math
\psi(y) = \mathbb{E}\left(T^*\mid Y=y\right).
```
By the law of total expectation,
we know that
```math
\mathbb{E}T^* = \mathbb{E}\left(\psi\left(Y\right)\right) = \mathbb{E}\left(T^*\mid Y=1\right)f_{Y}\left(1\right)+\mathbb{E}\left(T^*\mid Y=2\right)f_{Y}\left(2\right).
```

If the first grand prize won by the player is the featured prize, then the player stops pulling, i.e. $Y=1$ and the probability of winning the featured prize given that the player obtains a grand prize is $0.5$. Hence, it follows that
```math
f_{Y}(y)=\frac{1}{2},\quad y\in\{1,2\}.
```
Therefore, we have
```math
\mathbb{E}T^* = \frac{\mathbb{E}\left(T^*\mid Y=1\right)+ \mathbb{E}\left(T^*\mid Y=2\right)}{2}.
```
Given that the first grand prize the player wins is the featured prize, $T^*$ can be considered as a random variable following a geometric distribution with a pity system, i.e. $T^*\sim \mathrm{P-Geom}\left(p, N\right)$ because under this condition, the probability of obtaining the featured prize for each trial equals to $p$ before the guaranteed pull. Therefore, it follows that 
```math
\mathbb{E}\left(T^*\mid Y=1\right) = \frac{1-\left(1-p\right)^N}{p}.
```
On the other hand, under the condition $Y=2$, the first grand prize the player wins is not the featured one and the second grand prize is guaranteed to be the featured one. Let $T^*_1, T^*_2$ be the random variable of the waiting time to obtain the first grand prize and the waiting time to obtain the second grand prize after winning the first prize. By our definition, it follows that $T^* = T^*_1 + T^*_2$. Similar to the previous argument, we shall notice that
```math
T^*_{1}, T^*_{2}\sim\mathrm{P-Geom}\left(p, N\right).
```

Therefore,
```math
\mathbb{E}\left(T^*\mid Y=2\right) = \mathbb{E}\left(T^*_1\mid Y=2\right) +\mathbb{E}\left(T^*_2\mid Y=2\right) = 2\cdot\frac{1-\left(1-p\right)^N}{p}.
```

Hence, we can conclude that
```math
\mathbb{E}T^* = \frac{3}{2}\cdot\frac{1-\left(1-p\right)^N}{p} = \frac{3}{2}\mathbb{E}T.
```

Taking $p=0.006$ and $N=90$, 
```math
\mathbb{E}T^*\approx 104.5497
```

It shows that it takes about $105$ pulls to obtain the featured prize.

## Common Practices
In actual applications, gacha games often adopt *the soft and hard pity system*, that is, in the few pulls before the classic guarantee which is called the hard pity, the probability of winning the grand prize will increase gradually.
