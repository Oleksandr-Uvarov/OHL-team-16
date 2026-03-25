import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
match = pd.read_csv("data/gold_match.csv")
tickets = pd.read_csv("data/gold_match_tickets.csv")
context = pd.read_csv("data/gold_match_context.csv")

# Fusionner
df = match.merge(tickets, on="match_id")
df = df.merge(context, on="match_id")

# Température vs spectateurs
plt.figure()
plt.scatter(df["weather_temp_mean_c"], df["tickets_scanned"])
plt.xlabel("Température moyenne (°C)")
plt.ylabel("Nombre de spectateurs")
plt.title("Température vs spectateurs")
plt.show()

#  Pluie vs spectateurs

plt.figure()
plt.scatter(df["weather_rain_mm"], df["tickets_scanned"])
plt.xlabel("Pluie (mm)")
plt.ylabel("Nombre de spectateurs")
plt.title("Pluie vs spectateurs")
plt.show()

#Avec / sans pluie (bar chart)

df["rain"] = (df["weather_rain_mm"] > 0).astype(int)
group = df.groupby("rain")["tickets_scanned"].mean()

plt.figure()
group.plot(kind="bar")
plt.xlabel("Pluie (0 = non, 1 = oui)")
plt.ylabel("Spectateurs moyens")
plt.title("Impact de la pluie sur les spectateurs")
plt.show()