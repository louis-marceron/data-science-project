import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
df = pd.read_csv("data-clean/2022-clean/merged_dataset.csv")

# Grouper les données par localisation et compter le nombre d'accidents par lieu
accidents_par_lieu = df.groupby('Localisation').size().reset_index(name='Nombre d\'accidents')

# Trier les lieux par nombre d'accidents (du plus grand au plus petit)
accidents_par_lieu = accidents_par_lieu.sort_values(by='Nombre d\'accidents', ascending=False)

# Afficher les 10 premiers lieux avec le plus d'accidents
top_lieux = accidents_par_lieu.head(10)

# Créer un graphique à barres
plt.figure(figsize=(12, 6))
plt.bar(top_lieux['Localisation'], top_lieux['Nombre d\'accidents'], color='skyblue')
plt.title('Top 10 des lieux avec le plus d\'accidents en France')
plt.xlabel('Localisation')
plt.ylabel('Nombre d\'accidents')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Afficher le graphique
plt.show()
