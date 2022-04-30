#program to illustrate ElGamal encryption
import random
from math import pow

a = random.randint(2,10)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#generate a large random number
def generate_key(a):
    p = random.randint(pow(10, 20), a)
    while gcd(p, a) != 1:
        p = random.randint(pow(10, 20), a)
    return p

# Modular exponentiation
def mod_exp(b, e, m):
    if e == 0:
        return 1
    if e % 2 == 0:
        return mod_exp(b, e // 2, m) ** 2 % m
    else:
        return b * mod_exp(b, e - 1, m) % m

#Asymmetric encryption
def encrypt(msg, q, h, g):
    en_msg = []
 
    k = generate_key(q)# Private key for sender
    s = mod_exp(h, k, q)
    p = mod_exp(g, k, q)
     
    for i in range(0, len(msg)):
        en_msg.append(msg[i])
 
    print("g^k used : ", p)
    print("g^ak used : ", s)
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])
 
    return en_msg, p

def decrypt(en_msg, p, key, q):
    de_msg = []
    h = mod_exp(p, key, q)
    for i in range(0, len(en_msg)):
        de_msg.append(chr(en_msg[i] // h))
    
    return de_msg

def main():
 
    msg = 'Hello World'
    print("Original Message :", msg)
 
    q = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, q)
 
    key = generate_key(q)# Private key for receiver
    h = mod_exp(g, key, q)
    print("g used : ", g)
    print("g^a used : ", h)
 
    en_msg, p = encrypt(msg, q, h, g)
    dr_msg = decrypt(en_msg, p, key, q)
    dmsg = ''.join(dr_msg)
    print("Decrypted Message :", dmsg);
 
 
if __name__ == '__main__':
    main()

