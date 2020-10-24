# Piotr Kołodziejczyk

from collections import defaultdict
from functools import reduce
from sys import argv
from math import floor, sqrt


def read_tga(filename):
    with open(filename, "br") as f:
        header = list(map(int, f.read(18)))
        width = header[13]*256+header[12]
        height = header[15]*256+header[14]
        bitmap = [None for _ in range(width*height)]
        for pixl in range(width*height):
            bitmap[pixl] = tuple(list(map(int, f.read(3))))
        return bitmap, bytes(header)


def create_codebook(bitmap, codebook_length, epsilon):
    c0 = bitmap_avg(bitmap)
    codebook = [c0]
    avg_dist = avg_distortion_c0(c0, bitmap, len(bitmap))

    while len(codebook) < codebook_length:
        codebook, avg_dist = split_codebook(bitmap, codebook, epsilon, avg_dist)

    return codebook


def avg_distortion_c0(c0, data, size):
    return reduce(lambda s, d: s + d / size, (euclid(c0, vec) for vec in data), 0.0)


def mse(original, new):
    return (1 / len(original)) * sum(
        [(euclid(original[i], new[i])) for i in range(len(original))]
    )


def snr(x, mserr):
    return ((1 / len(x)) * sum(sum(xij**2 for xij in xi) for xi in x)) / mserr


def new_vector(c, e):
    return [x * (1.0 + e) for x in c]


def split_codebook(bitmap, codebook, epsilon, initial_avg_dist):
    length = len(bitmap)

    new_vectors = []
    for c in codebook:
        new_vectors.append(new_vector(c, epsilon))
        new_vectors.append(new_vector(c, -epsilon))
    codebook = new_vectors

    codebook_length = len(codebook)

    avg_dist = 0
    err = epsilon + 1
    iteration = 0
    while err > epsilon:
        closest_c_list = [None] * length
        vecs_near_c = defaultdict(list)
        vec_idxs_near_c = defaultdict(list)
        for i, vec in enumerate(bitmap):
            min_dist = None
            closest_c_index = None
            for i_c, c in enumerate(codebook):
                d = euclid(vec, c)
                if min_dist is None or d < min_dist:
                    min_dist = d
                    closest_c_list[i] = c
                    closest_c_index = i_c
            vecs_near_c[closest_c_index].append(vec)
            vec_idxs_near_c[closest_c_index].append(i)

        for i_c in range(codebook_length):
            vecs = vecs_near_c.get(i_c) or []
            num_vecs_near_c = len(vecs)
            if num_vecs_near_c > 0:
                new_c = bitmap_avg(vecs)
                codebook[i_c] = new_c
                for i in vec_idxs_near_c[i_c]:
                    closest_c_list[i] = new_c

        prev_avg_dist = avg_dist if avg_dist > 0 else initial_avg_dist
        avg_dist = avg_distortion_c_list(closest_c_list, bitmap, length)

        err = (prev_avg_dist - avg_dist) / prev_avg_dist

        iteration += 1

    return codebook, avg_dist


def avg_distortion_c_list(c_list, data, size):
    return reduce(
        lambda s, d: s + d / size,
        (euclid(c_i, data[i]) for i, c_i in enumerate(c_list)),
        0.0,
    )


def euclid(x, y):
    return sum((x_i - y_i) ** 2 for x_i, y_i in zip(x,y))


def bitmap_avg(bitmap):
    r = 0
    g = 0
    b = 0
    l = len(bitmap)
    for el in bitmap:
        r += el[0]
        g += el[1]
        b += el[2]
    return (r/l, g/l, b/l)


def quantify(bitmap, codebook):
    new_bitmap = []
    for pixel in bitmap:
        diffs = [euclid(pixel, x) for x in codebook]
        new_bitmap.append(codebook[diffs.index(min(diffs))])
    return new_bitmap


def rgb_floor(vectors):
    out = []
    for v in vectors:
        out.append(tuple(map(floor, v)))
    return out


def main():
    if len(argv) != 4:
        print("<in> <out> <colors>")
        return
    image, header = read_tga(argv[1])
    codebook = create_codebook(image, 2 ** int(argv[3]), 0.001)
    bitmap = rgb_floor(quantify(image, codebook))
    payload = bitmap_to_bytes(bitmap)

    mserr = mse(image, bitmap)
    snratio = snr(image, mserr)
    print(f"MSERR: {mserr}")
    print(f"SNR: {snratio}")

    with open(argv[2], "wb") as f:
        f.write(header + payload)


def bitmap_to_bytes(bitmap):
    payload = []
    for x in bitmap:
        for i in x:
            payload.append(i)
    return bytes(payload)


if __name__ == "__main__":
    main()