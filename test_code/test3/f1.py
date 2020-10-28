import random
import time
import math
# reprezentacja wektora 'bitowa' (0-1) : każda składowa po 20 bitów, 3 na część całkowitą i 17 na ułamkową - dokładność 10^-5

SIZE = 20

def yang(eps, x):
    res = 0
    for i in range(5):
        res += eps[i]*abs(x[i])**(i+1)
    return res


def bin_to_dec(bin):
    dec = int(bin[:3], 2)
    for i, b in enumerate(bin[3:]):
        dec += int(b)/2**(i+1)
    return dec


def bin_to_dec_tuple(bin):
    res = []
    for binary in bin:
        dec = int(binary[:3], 2)
        for i, b in enumerate(binary[3:]):
            dec += int(b)/2**(i+1)
        res.append(dec)
    return res


def dec_to_bin(dec):
    binary = [bin(int(dec))[2:].zfill(3)]
    dec -= int(dec)
    for _ in range(SIZE-3):
        dec *= 2
        if dec >= 1:
            binary.append('1')
            dec -= 1
        else:
            binary.append('0')
    return ''.join(binary)


def mutation(vector):
    temp = vector.copy()
    for j, el in enumerate(temp):
        t = list(el)
        for i, _ in enumerate(t):
            if random.random() <= 1/SIZE:
                if t[i] == '0':
                    t[i] = '1'
                else:
                    t[i] = '0'
        temp[j] = t
    return [''.join(x_i) for x_i in temp]


def twopoint_crossover(parent_a, parent_b):
    p_a = parent_a.copy()
    p_b = parent_b.copy()

    for k in range(5):
        c = random.randint(0, SIZE)
        d = random.randint(0, SIZE)

        p_a_k = list(p_a[k])
        p_b_k = list(p_b[k])

        if c > d:
            c, d = d, c
        if c != d:
            for i in range(c, d):
                p_a_k[i], p_b_k[i] = p_b_k[i], p_a_k[i]
        p_a[k], p_b[k] = p_a_k, p_b_k
    return [''.join(x_i) for x_i in p_a], [''.join(x_i) for x_i in p_b]


def fitness(eps, x):
    return 1/yang(eps,[bin_to_dec(x_i) for x_i in x])


def tournament_selection(eps, population, tournament_size):
    p = population.copy()

    best = random.choice(p)
    for _ in range(2, tournament_size):
        next_one = random.choice(p)
        if fitness(eps, next_one) > fitness(eps, best):
            best = next_one
    return best

def ga(f, x, eps, popsize, max_time):
    start = time.time()
    P = []
    x_bin = [''.join([dec_to_bin(x_i)]) for x_i in x]
    P.append(x_bin)
    for _ in range(popsize-1):
        P.append(mutation(x_bin))
    best = None
    while time.time() - start < max_time:
        for p_i in P:
            if best is None or fitness(eps, p_i) > fitness(eps, best):
                best = p_i
                last_best = time.time()
        Q = []
        for _ in range(popsize//2):
            p_a = tournament_selection(eps, P, 4)
            p_b = tournament_selection(eps, P, 4)
            ch_a, ch_b = twopoint_crossover(p_a, p_b)
            Q.append(mutation(ch_a))
            Q.append(mutation(ch_b))
        P = Q
        if time.time() - last_best > math.log(max_time):
            break
    best_out = bin_to_dec_tuple(best)
    return best_out, yang(eps, best_out)


if __name__ == "__main__":
    in_data = input().split()
    max_time = int(in_data[0])
    x = tuple(map(int, in_data[1:6]))
    eps = tuple(map(float, in_data[6:]))
    x_min, f_x = ga(yang, x, eps, 10, max_time)
    print(*x_min, f_x)
