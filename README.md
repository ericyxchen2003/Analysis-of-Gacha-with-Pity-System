# Expectation of Pulls with a Pity System

---

## Introduction

Nowadays, more and more games are introducing a pity system in their gacha systems. We want to derive the expectation of the number of pulls to get the grand prize.

## Assumption

Assume that for each pull, the probability of obtaining a grand prize is $p$. The pity system guarantees that if a player does not obtain any grand prize after $N-1$ pulls, the $N$-th pull is guaranteed to be the grand prize. Assume that the player starts from the first pull.

## Definition

Let $X$ be the random variable of the pulls to obtain a grand prize. Its probability mass function is given by
```math
f_{X}(x)=\begin{cases}
\left(1-p\right)^{x-1}p&x=1,2,\ldots,N-1,\\
\left(1-p\right)^{x-1}&x=N.
\end{cases}
```
One can tell that the distribution of $X$ is similar to a geometric distribution, but $f_X$ has a finite domain.

## Derivation

Consider the probability generating function:
```math
G_X\left(s\right)=\mathbb{E}s^X = \sum_{i=1}^{N-1}s^{i}\left(1-p\right)^{i-1}p+s^{N}\left(1-p\right)^{N-1}.
```
Since
```math
G_{X}\left(s\right)=\frac{p}{1-p}\sum_{i=1}^{N-1}\left(s\left(1-p\right)\right)^{i} + s^{N}\left(1-p\right)^{N-1},
```
we have 
```math
G_{X}\left(s\right)=\frac{p}{1-p}\cdot\frac{s\left(1-p\right)-\left(s\left(1-p\right)\right)^N}{1-s\left(1-p\right)}+s^{N}\left(1-p\right)^{N-1}.
```
 
Next, compute the derivatives:
```math
\frac{\mathrm{d}}{\mathrm{d}s}G_{X}\left(s\right) = \frac{p}{1-p}\cdot\frac{\left(1-N\left(s\left(1-p\right)\right)^{N-1}\right)\left(1-s\left(1-p\right)\right)-\left(-1\right)\left(s\left(1-p\right)-\left(s\left(1-p\right)\right)^N\right)}{\left(1-s\left(1-p\right)\right)^2} + N\left(1-p\right)^{N-1}s^{N-1}.
```
Therefore, the expectation of $X$ is given by:
```math
\left.\frac{\mathrm{d}}{\mathrm{d}s}G_{X}\left(s\right)\right|_{s=1} = \mathbb{E}X = \frac{1-\left(1-p\right)^N}{p}.
```
