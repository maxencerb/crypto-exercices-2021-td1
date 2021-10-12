# Cryptography problem solving

&copy; Maxence Raballand 2021

These are small algorithms to resolve [these exercises](https://vqhuy.github.io/teaching/crypto/td1) of cryptography.

## Answers to Questions

### T5 : Brute-force attacks

With a million dollar, we could run 20,000 50$ ASIC in parrallel.

The current recommended key length by the AES is 128 bits. So there are many possible keys.

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=n_{key} = 2^128 = 3.402823669 \times 10 ^ 38" />
</p>

With 20,000 of these ASIC, we could search for :

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=n_{\frac{key}{sec}} = 5 \times 10 ^ 8 \times 20000 = 1 \times 10^13" />
</p>

We can describe the probability of finding the key with an hypergeometric distribution. Let X be the random variable that tells if we found the key in the current second. The units will be seconds. As such, the proportion of possible keys scanned per second is :

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=n_{\frac{scanned}{sec}} = \frac{1 \times 10^13}{3.402823669 \times 10 ^ 38} = 2.9387563 \times 10^{-26}" />
</p>

So to scan all the keys, it would approximatively take 3,5×10²⁵ seconds. As we can see here this is only a small proportion. Now let :

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=X \sim Hypergeometric(K, N, n)" />
</p>

Where *K* is the the number of correct keys, so here *K = 1*, *N* is the size of the population (<img src="https://render.githubusercontent.com/render/math?math=N = 3.402823669 \times 10 ^ 38" />) and *n* the number of key searched. The mean of an hypergeometrical distribution is :

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=\mu = n \frac{K}{N}" />
</p>

So we can approximate the mean time (in seconds) it would take to find a 128 bit key.

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=\mu_{time} = \frac{1}{3.5 \times 10^25} \sum_{n=1}^{3.5 \times 10^25} n \times 1 \times 10^13 \times \frac{1}{3.402823669 \times 10 ^ 38}" />
    <br/>
    <img src="https://render.githubusercontent.com/render/math?math=\mu_{time} = \frac{(3.5 \times 10^25)^2}{2 \times 3.5 \times 10^25}  \times 1 \times 10^13 \times \frac{1}{3.402823669 \times 10 ^ 38}" />
    <br/>
    <img src="https://render.githubusercontent.com/render/math?math=\mu_{time} = \frac{17.5 \times 10^38}{23.8 \times 10^38}  " />
</p>