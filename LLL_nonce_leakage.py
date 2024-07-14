# -*- coding: utf-8 -*-
"""
@author: iceland
@credit: KV, pianist-coder
"""
###################################################################################
import random
import math
import secp256k1 as ice
import time
from gmpy2 import mpq
###################################################################################
N = ice.N
fix_bits = 56
out_file_name = 'pseudo_sig_rsz.txt'
kbits = 256 - fix_bits
###################################################################################

def reduction(input_vectors, tolerance):
    def gramschmidt_orthogonalization(vectors):
        num_vectors = len(vectors)
        basis = [None] * num_vectors
        for i in range(num_vectors):
            basis[i] = vectors[i].copy()
            for j in range(i):
                projection = sum(vectors[i][k] * basis[j][k] for k in range(len(vectors[i]))) / \
                             sum(basis[j][k] * basis[j][k] for k in range(len(basis[j])))
                for k in range(len(vectors[i])):
                    basis[i][k] -= projection * basis[j][k]
        return basis

    def update_orthogonal_vectors(orthogonalized, basis_vectors, index):
        j = index - 1
        while j >= 0:
            mu_kj = sum(x * y for x, y in zip(orthogonalized[j], basis_vectors[index])) / sum(x ** 2 for x in orthogonalized[j])
            if abs(mu_kj) > 0.5:
                basis_vectors[index] = [v - round(mu_kj) * basis_vectors[j][k] for k, v in enumerate(basis_vectors[index])]
            j -= 1
        return basis_vectors

    num_vectors = len(input_vectors)
    basis_vectors = [None] * num_vectors
    basis_vectors = [[mpq(x) for x in vec] for vec in input_vectors]
    orthogonalized = gramschmidt_orthogonalization(basis_vectors)
    index = 1
    while index < num_vectors:
        basis_vectors = update_orthogonal_vectors(orthogonalized, basis_vectors, index)
        lhs_dot_lhs = sum(x ** 2 for x in orthogonalized[index - 1])
        projection_coefficient = sum(x * y for x, y in zip(orthogonalized[index - 1], basis_vectors[index])) / lhs_dot_lhs
        dot_product = sum(x ** 2 for x in orthogonalized[index])
        if dot_product >= (tolerance - projection_coefficient ** 2) * lhs_dot_lhs:
            index += 1
        else:
            basis_vectors[index], basis_vectors[index - 1] = basis_vectors[index - 1], basis_vectors[index]
            orthogonalized = gramschmidt_orthogonalization(basis_vectors)
            index = max(index - 1, 1)
    return [[int(x) for x in b] for b in basis_vectors]

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

def minimum_sigs_required(num_bits: int) -> int:
    return math.ceil(1.03 * 4 / 3 * 256 / num_bits)

def identity_plus2(u, elem=1):
    result = [[0] * (u + 2) for _ in range(u)]
    for i in range(u):
        result[i][i] = elem
    return result

if __name__ == '__main__':

    n = 1 + minimum_sigs_required(fix_bits)
    print(f'\n Fixed Nonce bits = {fix_bits}           Minimum Signature Required = {n}')
    secret = random.randint(1, N)
    pub = ice.scalar_multiplication(secret)
    print('###############################################################################')
    print(f'secret: {hex(secret)[2:]}')
    print(f'Pubkey: {pub.hex()}')
    print('###############################################################################')

    fixed_k_prefix = random.randrange(2**kbits, N)
    z = [random.randrange(1, N) for i in range(n)]
    nonces = [random.randrange(1, 2**kbits) + fixed_k_prefix for i in range(n)]
    sigs_r = [getx(ice.scalar_multiplication(nonces[i])) for i in range(n)]
    mod_inv_nonces = [modinv(nonces[i]) for i in range(n)]
    sigs_s = [(z[i] + secret * sigs_r[i]) * mod_inv_nonces[i] % N for i in range(n)]
    sinv = [modinv(s) for s in sigs_s]
    write_rsz_file(sigs_r, sigs_s, z, pub)
    matrix = identity_plus2(n - 1, N)
    row, row2 = [], []
    [zn, rn, sn] = [z[-1], sigs_r[-1], sigs_s[-1]]
    rnsn_inv = rn * modinv(sn)
    znsn_inv = zn * modinv(sn)

    for i in range(n-1):
        row.append((sigs_r[i] * modinv(sigs_s[i])) - rnsn_inv)
        row2.append((z[i] * modinv(sigs_s[i])) - znsn_inv)

    row.append((2**kbits) / N)
    row.append(0)
    row2.append(0)
    row2.append(2**kbits)

    matrix.append(row)
    matrix.append(row2)

    print(' Original Matrix')
    print(matrix)

    start = time.time()
    new_matrix = reduction(matrix, 0.35)

    print('\n\n Reduced Matrix')
    print(new_matrix)
###################################################################################
    for row in new_matrix:
        potential_nonce_diff = row[0]
        sigs_s_0 = sigs_s[0]
        zn_times_sigs_s_0 = zn * sigs_s_0
        sn_times_z_0 = sn * z[0]
        sn_times_sigs_s_0_times_potential_nonce_diff = sn * sigs_s_0 * potential_nonce_diff
        denominator = (rn * sigs_s_0) - (sigs_r[0] * sn)
        denominator_inv = modinv(denominator)
        potential_priv_key = (sn_times_z_0 - zn_times_sigs_s_0 - sn_times_sigs_s_0_times_potential_nonce_diff) * denominator_inv % N

        if ice.scalar_multiplication(potential_priv_key) == pub:
            print('-'*79)
            print(f' Found private key = {hex(potential_priv_key)[2:]}')
            print('-'*79)
###################################################################################
    end = time.time()
    print(f"time = {end - start:.2f} sec")