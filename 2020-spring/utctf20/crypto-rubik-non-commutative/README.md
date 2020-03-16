# Cube Crypto
* **Event:** UTCTF 2020
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**


Ok, so I accidentally cheesed this problem too much. I'll just go through my intended solution, the easier solution can be found in a lot of other writeups on CTFtime.​

## Steps​
#### Step 1
From the two very unusual names in the prompt, you should be able to find the [Anshel-Anshel-Goldfeld Key Exchange](https://en.wikipedia.org/wiki/Anshel%E2%80%93Anshel%E2%80%93Goldfeld_key_exchange). This key exchange works somewhat like [Diffie-Hellman](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange) in that you are using public/asymmetric cryptography to generate a symmetric key. The only difference is that Anshel-Anshel-Goldfeld works on any [non-abelian group](https://en.wikipedia.org/wiki/Non-abelian_group). And lucky for us, the [Rubik's Cube group](https://en.wikipedia.org/wiki/Rubik%27s_Cube_group) is non-abelian :).

#### Step 2
In the Rubik's cube group, the operation is concatenation of the configurations (and then simplifying duplicates, inverses, etc.). Computing inverses is as simple as reversing the configuration and then negating. So `U D R' L'` becomes `L R D' U'`. See? Not so bad.

#### Step 3
I give you the two public keys, aBar and bBar. Since the public key is very small, you can brute force all of the private key (A or B) solutions, and then double check your work by looking at aBar or bBar.

#### Step 4
The final step is to calculate the shared key, or `A'B'AB`. When you do that, you get the flag (not in traditional format): `B D' R' D U F' R D L' D' R D B' L D' R' F U'`.
