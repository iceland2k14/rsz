# -*- coding: utf-8 -*-
"""

@author: iceland
@credit: KV
"""

import olll
import random
import math
import secp256k1 as ice

G = ice.scalar_multiplication(1)
N = ice.N

# Secret key = x = (rns1 – r1sn)-1 (snm1 – s1mn – s1sn(k1 – kn))
# For most significant fix 128 bit leak at least 3 sig is required.
fix_bits = 128
out_file_name = 'pseudo_sig_rsz.txt'

kbits = 256 - fix_bits


#==============================================================================
def write_rsz_file(rr, ss, zz, pb):
    with open(out_file_name, 'w') as f:
        sz = len(rr)
        for i in range(sz):
            f.write('r      = ' + hex(rr[i])[2:].zfill(64) + '\n')
            f.write('s      = ' + hex(ss[i])[2:].zfill(64) + '\n')
            f.write('z      = ' + hex(zz[i])[2:].zfill(64) + '\n')
        f.write('pubkey = ' + pb.hex())
        
def modinv(v):
    return pow(v, N-2, N)

def getx(Q):
    return int(Q[1:33].hex(), 16)

def minimum_sigs_required(num_bits):
    return math.ceil(1.03 * 4 / 3 * 256 / num_bits)

def identity_plus2(u, elem=1):
    m=[[0 for x in range(u+2)] for y in range(u)]
    for i in range(0,u):
        m[i][i] = elem
    return m
#==============================================================================
n = 1 + minimum_sigs_required(fix_bits)
print(f'\n Fixed Nonce bits = {fix_bits}           Minimum Signature Required = {n}')


# example secret = 0x7cf5d79d200207963474c64e64bde80ff4cb3e225b6ac5b6e958522fdab60578
secret = random.randint(1,N)
pub = ice.scalar_multiplication(secret)
print('###############################################################################')
print(f'secret: {hex(secret)}')
print(f'Pubkey: {pub.hex()}')
print('###############################################################################')

fixed_k_prefix = random.randrange(2**kbits, N)

#S = ((Z + (X * R)) / K) % N
z = [random.randrange(1, N) for i in range(n)]
nonces = [random.randrange(1, 2**kbits) + fixed_k_prefix for i in range(n)]
sigs_r = [getx(ice.scalar_multiplication(nonces[i])) for i in range(n)]
sigs_s = [( (z[i] + secret * sigs_r[i]) * modinv(nonces[i]) )%N for i in range(n)]
sinv   = [modinv(sigs_s[i]) for i in range(n)]

write_rsz_file(sigs_r, sigs_s, z, pub)
###############################################################################
matrix = identity_plus2(n-1, N)

# Add last 2 rows
row, row2 = [], []
[zn, rn, sn] = [z[-1], sigs_r[-1], sigs_s[-1]]
rnsn_inv = rn * modinv(sn)
znsn_inv = zn * modinv(sn)


# 2nd to last row: [r1(s1^-1) - rn(sn^-1), ... , rn-1(sn-1^-1) - rn(sn^-1), 2^176/order, 0 ]
# last row: [m1(s1^-1) - mn(sn^-1), ... , mn-1(sn-1^-1) - mn(sn^-1), 0, 2^176]
for i in range(n-1):
    row.append((sigs_r[i] * modinv(sigs_s[i])) - rnsn_inv)
    row2.append((z[i] * modinv(sigs_s[i])) - znsn_inv)

# add last elements of last two rows, B = 2**(256-80) for yubikey
row.append((2**kbits) / N)
row.append(0)
row2.append(0)
row2.append(2**kbits)
 
matrix.append(row)
matrix.append(row2)

print(' Original Matrix')
print(matrix)
###############################################################################
new_matrix = olll.reduction(matrix, 0.75)
print('\n\n Reduced Matrix')
print(new_matrix)

for row in new_matrix:
    potential_nonce_diff = row[0]
#    print('k=', hex(potential_nonce_diff))
#    modinv(r3 * s1 - r1 *s3) * (s3 * m1 - s1 * m3 - s1 * s3 *(k1 - k3))
    potential_priv_key = (sn * z[0]) - (sigs_s[0] * zn) - (sigs_s[0] * sn * potential_nonce_diff)
    potential_priv_key *= modinv((rn * sigs_s[0]) - (sigs_r[0] * sn))
    potential_priv_key = potential_priv_key % N
#    print('PK=', hex(potential_priv_key))
 
    # check if we found private key by comparing its public key with actual public key
    if ice.scalar_multiplication(potential_priv_key) == pub:
        print('-'*75)
        print(f' found private key = {hex(potential_priv_key)}')
        print('-'*75)
###############################################################################