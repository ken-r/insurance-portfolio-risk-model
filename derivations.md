# Finding lognormal parameters from a target mean and standard deviation

Let $m$ and $s$ be the target mean and standard deviation. We want to find the parameters $\mu$ and $\sigma$ of a lognormal random variable $X$ with these values.

The mean and variance of $X$ are known in closed form (see, for example, [Wikipedia](https://en.wikipedia.org/wiki/Log-normal_distribution)):

$$
\begin{aligned}
\mathbb{E}[X] &= \exp\left(\mu + \frac{\sigma^2}{2}\right),\\
\operatorname{Var}(X) &= \left[\exp(\sigma^2) - 1\right] \exp(2\mu + \sigma^2).
\end{aligned}
$$

Matching these expressions to the target mean and variance gives

$$
\begin{aligned}
m &= \exp\left(\mu + \frac{\sigma^2}{2}\right),\\
s^2 &= \left[\exp(\sigma^2) - 1\right] \exp(2\mu + \sigma^2).
\end{aligned}
$$

Squaring the first equation gives $m^2 = \exp(2\mu + \sigma^2)$. Substituting this into the second equation yields

$$
\frac{s^2}{m^2} = \exp(\sigma^2) - 1.
$$

Adding $1$ and taking the logarithm, we obtain

$$
\sigma^2 = \log\left(1 + \frac{s^2}{m^2}\right),
\qquad
\sigma = \sqrt{\log\left(1 + \frac{s^2}{m^2}\right)}.
$$

Finally, rearranging the mean equation gives $\mu = \log(m) - \frac{\sigma^2}{2}$.
