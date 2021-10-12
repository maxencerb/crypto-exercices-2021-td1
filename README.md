# Cryptography problem solving

&copy; Maxence Raballand 2021

These are small algorithms to resolve [these exercises](https://vqhuy.github.io/teaching/crypto/td1) of cryptography.

## Answers to Questions

### T5 : Brute-force attacks

With a million dollar, we could run 20,000 50$ ASIC in parrallel.

The current recommended key length by the AES is 128 bits. So there are many possible keys.

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=n_{key} = 2^128 = 3,402823669 \times 10 ^ 38" />
</p>

With 20,000 of these ASIC, we could search for :

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=n_{\frac{key}{sec}} = 5 \times 10 ^ 8 \times 20000 = 1 \times 10^13" />
</p>

