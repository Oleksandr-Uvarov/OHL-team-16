import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = "Times New Roman"

# Charger données
articles = pd.read_csv("data/gold_belga_press_articles.csv", on_bad_lines='skip')

# Nettoyage
articles = articles.dropna(subset=["title", "lead"])
articles = articles.drop_duplicates()

# Texte
articles["text"] = articles["title"] + " " + articles["lead"]

# Mots
positive_words = ["win", "victory", "success", "good", "great", "excellent", "strong", "growth"]
negative_words = ["loss", "fail", "bad", "crisis", "problem", "injury", "decline", "poor"]

# Fonction sentiment
def get_sentiment(text):
    text = text.lower()
    pos = sum(text.count(word) for word in positive_words)
    neg = sum(text.count(word) for word in negative_words)

    if pos > neg:
        return "positive"
    elif neg > pos:
        return "negative"
    else:
        return "neutral"

# Appliquer
articles["sentiment"] = articles["text"].apply(get_sentiment)

# Date
articles["date"] = pd.to_datetime(articles["date"])


matches = articles[articles["match_id"].notna()][["match_id", "date"]].drop_duplicates()
matches = matches.sort_values("date").reset_index(drop=True)

results = []

for i in range(len(matches) - 1):
    start_date = matches.loc[i, "date"]
    end_date = matches.loc[i + 1, "date"]

    subset = articles[
        (articles["date"] > start_date) &
        (articles["date"] < end_date)
    ].copy()

    subset["period"] = f"{start_date.date()} -> {end_date.date()}"
    results.append(subset)

# Fusion
articles_between = pd.concat(results)

# Grouper par période
data = articles_between.groupby(["period", "sentiment"]).size().unstack(fill_value=0)

# Couleurs
colors = ["#D9534F", "#4A90E2", "#CFCFCF"]

# Graphique
data.plot(kind="bar", stacked=True, figsize=(12,6), color=colors)

plt.title("Sentiment des articles ENTRE chaque match")
plt.xlabel("Périodes entre matchs")
plt.ylabel("Nombre d'articles")

plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

print("\nTableau des sentiments par période :\n")
print(data.to_string())
print(len(data))