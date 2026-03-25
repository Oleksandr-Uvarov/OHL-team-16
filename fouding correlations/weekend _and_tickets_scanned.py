import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
match = pd.read_csv("data/gold_match.csv")
tickets = pd.read_csv("data/gold_match_tickets.csv")
context = pd.read_csv("data/gold_match_context.csv")

# Fusionner les datasets
df = match.merge(tickets, on="match_id")
df = df.merge(context, on="match_id")

# Analyse weekend vs spectateurs
result = df.groupby("is_weekend")["tickets_scanned"].mean()

print("Moyenne de spectateurs :")
print(result)

# Graphique
plt.figure()
result.plot(kind="bar")
plt.xlabel("Weekend (0 = semaine, 1 = weekend)")
plt.ylabel("Spectateurs moyens")
plt.title("Impact du weekend sur les spectateurs")

# Sauvegarder le graphique en image
plt.savefig("graph_weekend.png")

# Afficher le graphique
plt.show()