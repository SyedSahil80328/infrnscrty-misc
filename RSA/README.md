# RSA ALGORITHM

RSA, which stands for Rivest-Shamir-Adleman, is a widely-used asymmetric cryptographic algorithm that is crucial for secure communication and data transmission over insecure networks like the internet. Here's an expanded explanation of RSA:

1. **Asymmetric Cryptography**: RSA is based on asymmetric cryptography, which means it uses a pair of keys - a public key and a private key. These keys are mathematically related, but deriving one from the other is computationally infeasible.

2. **Key Generation**:
   - **Key Pair Generation**: To use RSA, one generates a key pair consisting of a public key and a private key. The public key can be freely distributed, while the private key must be kept secret.
   - **Prime Number Generation**: RSA relies on the difficulty of factoring large composite numbers into their prime factors. Generating the key pair involves selecting two large prime numbers, typically p and q, and computing their product, n.

3. **Key Components**:
   - **Public Key (e, n)**: This is generated from the two large primes (p and q) as part of the key generation process. It consists of the modulus, n, and an encryption exponent, e, which is typically a small prime such as 65537.
   - **Private Key (d, n)**: This is derived from the primes and the public exponent. It consists of the same modulus, n, and a decryption exponent, d, which is computed such that it satisfies the equation (e * d) mod φ(n) = 1, where φ(n) is Euler's totient function of n.

4. **Encryption**:
   - **Message Encryption**: To encrypt a message M using RSA, one raises it to the power of the public exponent, e, modulo n. The ciphertext C is then transmitted.
   - **Mathematical Representation**: C ≡ M^e (mod n)

5. **Decryption**:
   - **Message Decryption**: To decrypt the ciphertext C, the recipient uses their private key exponent, d, to raise C to the power of d modulo n, yielding the original message M.
   - **Mathematical Representation**: M ≡ C^d (mod n)

6. **Security**:
   - RSA's security relies on the difficulty of factoring large numbers, specifically the modulus, n, into its prime factors. The security of RSA depends on the length of the keys used; longer keys provide greater security against brute-force attacks.
   - Key management is crucial; the private key must be kept secret, and the public key must be distributed securely to ensure the integrity of the communication.

7. **Applications**:
   - RSA is widely used in secure communication protocols like SSL/TLS for securing web traffic, SSH for secure remote access, digital signatures for authentication, and encryption of sensitive data.
   - It is a fundamental component in many cryptographic systems and protocols, forming the basis for secure communication in various applications.

# Output

![RSA Execution](https://github.com/SyedSahil80328/information-security/blob/main/RSA/Output.png)
