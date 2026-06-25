import numpy as np
import scipy.stats as stats
import pandas as pd

dados = np.array([
98.60,98.60,98.00,98.00,99.00,98.40,98.40,98.40,98.40,98.60,98.60,98.80,98.60,97.00,
97.00,98.80,97.60,97.70,98.80,98.00,98.00,98.30,98.50,97.30,98.70,97.40,98.90,98.60,
99.50,97.50,97.30,97.60,88.20,99.60,98.70,99.40,98.20,98.00,98.60,98.60,97.20,98.40,
98.60,98.20,98.00,97.80,98.00,98.40,98.60,98.60,97.80,99.00,96.50,97.60,98.00,96.90,
97.60,97.10,97.90,98.40,97.30,98.00,97.50,97.60,98.20,98.50,98.80,98.70,97.80,98.00,
97.10,97.40,99.40,98.40,98.60,98.40,98.50,98.60,98.30,98.70,98.80,99.10,98.60,97.90,
98.80,98.00,98.70,98.50,98.90,98.40,98.60,97.10,97.90,98.80,98.70,97.60,98.20,99.20,
97.80,98.00,98.40,97.80,98.40,97.40,98.00,97.00
])

n = len(dados)

k = int(1 + 3.3 * np.log10(n))
bins = np.linspace(dados.min(), dados.max(), k + 1)

freq, edges = np.histogram(dados, bins=bins)
mid = (edges[:-1] + edges[1:]) / 2
fa_acum = np.cumsum(freq)

tabela = pd.DataFrame({
    "Classe": [f"{edges[i]:.2f} - {edges[i+1]:.2f}" for i in range(len(freq))],
    "fi": freq,
    "xi": mid,
    "Fi": fa_acum
})

media = np.mean(dados)
mediana = np.median(dados)
moda = stats.mode(dados, keepdims=True).mode[0]

Q1 = np.percentile(dados, 25)
Q3 = np.percentile(dados, 75)

variancia = np.var(dados, ddof=1)
desvio = np.std(dados, ddof=1)
cv = (desvio / media) * 100

IQR = Q3 - Q1
lim_inf = Q1 - 1.5 * IQR
lim_sup = Q3 + 1.5 * IQR
outliers = dados[(dados < lim_inf) | (dados > lim_sup)]

media_g = np.sum(freq * mid) / n

classe_mediana = np.where(fa_acum >= n / 2)[0][0]
L = edges[classe_mediana]
F = fa_acum[classe_mediana - 1] if classe_mediana > 0 else 0
f = freq[classe_mediana]
h = edges[1] - edges[0]

mediana_g = L + ((n/2 - F) / f) * h

classe_modal = np.argmax(freq)
Lmo = edges[classe_modal]
f1 = freq[classe_modal]
f0 = freq[classe_modal - 1] if classe_modal > 0 else 0
f2 = freq[classe_modal + 1] if classe_modal < len(freq) - 1 else 0

moda_g = Lmo + ((f1 - f0) / ((f1 - f0) + (f1 - f2))) * h

def quartil_g(q):
    pos = q * n
    classe = np.where(fa_acum >= pos)[0][0]
    L = edges[classe]
    F = fa_acum[classe - 1] if classe > 0 else 0
    f = freq[classe]
    return L + ((pos - F) / f) * h

Q1_g = quartil_g(0.25)
Q3_g = quartil_g(0.75)

variancia_g = np.sum(freq * (mid - media_g) ** 2) / (n - 1)
desvio_g = np.sqrt(variancia_g)
cv_g = (desvio_g / media_g) * 100

assimetria = stats.skew(dados)
curtose = stats.kurtosis(dados)

print("\n~~~~~ (a) ~~~~~")
print(tabela)

print("\n~~~~~ (b) ~~~~~")
print(f"Média: {media:.5f}")
print(f"Mediana: {mediana:.5f}")
print(f"Moda: {moda:.5f}")

print("\n~~~~~ (c) ~~~~~")
print(f"Média agrupada: {media_g:.5f}")
print(f"Mediana agrupada: {mediana_g:.5f}")
print(f"Moda agrupada: {moda_g:.5f}")

print("\n~~~~~ (d) ~~~~~")
print(f"Q1: {Q1:.5f}")
print(f"Q3: {Q3:.5f}")

print("\n~~~~~ (e) ~~~~~")
print(f"Q1 agrupado: {Q1_g:.5f}")
print(f"Q3 agrupado: {Q3_g:.5f}")

print("\n~~~~~ (f) ~~~~~")
print("Outliers:", outliers)

print("\n~~~~~ (g) ~~~~~")
print(f"Variância: {variancia:.5f}")
print(f"Desvio padrão: {desvio:.5f}")
print(f"CV: {cv:.5f}")

print("\n~~~~~ (h) ~~~~~")
print(f"Variância agrupada: {variancia_g:.5f}")
print(f"Desvio padrão agrupado: {desvio_g:.5f}")
print(f"CV agrupado: {cv_g:.5f}")

print("\n~~~~~ (i) ~~~~~")
print(f"Assimetria: {assimetria:.5f}")
print(f"Curtose: {curtose:.5f}")