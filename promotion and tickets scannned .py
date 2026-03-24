import pandas as pd

# Charger les données
match = pd.read_csv("data/gold_match.csv")
tickets = pd.read_csv("data/gold_match_tickets.csv")
context = pd.read_csv("data/gold_match_context.csv")
df = match.merge(tickets, on="match_id")
df = df.merge(context, on="match_id")
print("Colonnes disponibles :")
print(df.columns)

# Vérifier les valeurs de promotion
print("\n Répartition des promotions :")
print(df["has_promotion"].value_counts())

# Calculer la moyenne de spectateurs avec/sans promotion
result = df.groupby("has_promotion")["tickets_scanned"].mean()

print("\n Moyenne de spectateurs :")
print(result)

# Interprétation
if 1 in result.index and 0 in result.index:
    if result[1] > result[0]:
        print("\n Les promotions semblent augmenter le nombre de spectateurs.")
    else:
        print("\n Les promotions ne semblent pas augmenter le nombre de spectateurs.")
else:
    print("\n Pas assez de données pour comparer.")