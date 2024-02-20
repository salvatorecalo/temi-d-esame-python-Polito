k = 10
x = float(input("inserisci lo spostamento iniziale: "))
v = 0
m = 1
delta_t = 0.01

print("la costante k della molla vale {k}")
print("lo spostamento iniziale vale {x}")
print("la velocità iniziale v vale {v}")
print("la massa m vale {m}")
print("l'intervallo delta_t è di {delta_t}")

while x >=0:
    F = -k*x
    a = F/m
    v = a * delta_t
    s = v * delta_t
    print(f"la forza di hooke vale: {F}")
    print(f"la velocità vale {v}")
    print(f"lo spostamento vale {s}")
    print(f"l'accelerazione vale {a}")
    x -= 0.01