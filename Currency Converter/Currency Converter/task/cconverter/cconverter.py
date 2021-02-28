# write your code here!
rates = {"RUB": 2.98, "ARS": 0.82, "HNL": 0.17, "AUD": 1.9622, "MAD": 0.208}
conicoins = float(input())

for x in rates:
    print(f"I will get {rates[x] * conicoins:.2f} {x} from the sale of {conicoins} conicoins.")
