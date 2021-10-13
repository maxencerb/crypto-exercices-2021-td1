# Cryptography problem solving

&copy; Maxence Raballand 2021

These are small algorithms to resolve [these exercises](https://vqhuy.github.io/teaching/crypto/td1) of cryptography.

## Answers to Questions

### T5 : Brute-force attacks

With a million dollar, we could run 20,000 50$ ASIC in parrallel.

The current recommended key length by the AES is 128 bits. So there are many possible keys.

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=n_{key} = 2^128 = 3.4 \times 10 ^ 38" />
</p>

With 20,000 of these ASIC, we could search for :

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=n_{\frac{key}{sec}} = 5 \times 10 ^ 8 \times 20000 = 1 \times 10^13" />
</p>

We know that ther is 31536000 seconds approximatively in a year. Knowing that, testing all the keys would take us :

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=T_{max} = \frac{3.4 \times 10 ^ 38}{1 \times 10^13 \times 31536000} = 1.1 \times 10 ^ 18 years" />
</p>

Even if we check only half of all keys (~50% chance to find the key), it would take us around *5 x 10¹⁷* years to find the key. So this would take 100,000,000 times the total age of the universe.

Now let's take Moore law into account that states that computer performance doubles every 18 months with a constant price. Without taking inflation into account, we will still invest 1,000,000 $ in ASIC and what we are trying to find is a date where these ASIC would compute the key in ~24hours. We have :

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=n_{\frac{key}{sec}}(0) = 1 \times 10^13" />
</p>

According to Moore's law, the function of *t* (in months) that tells us the number of key computed per second would be :

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=n_{\frac{key}{sec}}(t) = 1 \times 10^13 %2B \frac{t \times 1 \times 10 ^ 13}{18} = (\frac{18 %2B t}{18}) \times 1 \times 10^13" />
</p>

In a day there is 86400 seconds so we are solving *t* for :

<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=n_{\frac{key}{sec}}(t) = \frac{3.4 \times 10 ^ 38}{86400}" />
    <br/>
    <img src="https://render.githubusercontent.com/render/math?math=(\frac{18 %2B t}{18}) \times 1 \times 10^13 = \frac{3.4 \times 10 ^ 38}{86400}" />
    <br/>
    <img src="https://render.githubusercontent.com/render/math?math=t = \frac{18 \times 3.4 \times 10 ^ 25}{86400} - 18" />
    <br/>
    <img src="https://render.githubusercontent.com/render/math?math=t = 7 \times 10 ^ 21" />
</p>

So it would take more time to wait for technology to allow this than computing the key with today's technology (~ 7 x 10¹¹ times the age of the universe).

### T6 : Password

1. If the password consist of 8 ASCII characters (7 bits each), then the size of the key space would be <img src="https://render.githubusercontent.com/render/math?math=2^{8 \times 7} = 7.2 \times 10 ^ 16" />.

2. The corresponding key length would be a 56 bits key.

3. With only the 26 lowercase letters, we could encode the alphabet on 5 bits (32 possibilities). Then the corresponding key length would be 40.

4. To have a corresponding key length of 128 bits :

    - with 7 bits ASCII, we would need a password of <img src="https://render.githubusercontent.com/render/math?math=\frac{128}{7} \simeq 19 characters" />.
    - with 5 bits lowercase alphabet, we would need a password of <img src="https://render.githubusercontent.com/render/math?math=\frac{128}{5} \simeq 26 characters" />.