n = int(input("Masukkan nilai n: "))
r = int(input("Masukkan nilai r: "))

fakt_n = 1
for i in range(1, n + 1):
    fakt_n *= i

fakt_r = 1
for i in range(1, r + 1):
    fakt_r *= i

fakt_n_r = 1
for i in range(1, (n - r) + 1):
    fakt_n_r *= i

C = fakt_n // (fakt_r * fakt_n_r)
print("Kombinasi C(", n, ",", r, ") adalah", C)

