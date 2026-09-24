import requests

"""
Ce programme récupère les données météorologiques de trois villes
(Mérignac, Saint-Geours-de-Maremne et Toulouse) depuis l'API OpenWeather.

Pour chaque ville et pour chacun des cinq jours de prévision,
le programme recherche les températures minimales et maximales
et affiche la température minimale et maximale de la journée.
"""

# Récupération des données de prévisions météorologiques à 5 jours des trois villes

# Données de Mérignac
response_01 = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast?q=Mérignac&appid=23a4f11a83abb1b76a3a69c94f7bc24c&units=metric"
    )

# Données de Saint-Geours-de-Maremne
reponse_02 = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast?q=Saint-Geours-de-Maremne&appid=23a4f11a83abb1b76a3a69c94f7bc24c&units=metric"
    )

# Données de Toulouse
reponse_03 = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast?q=Toulouse&appid=23a4f11a83abb1b76a3a69c94f7bc24c&units=metric"
    )

# Conversion de la réponse JSON de l'API pour les trois villes en dictionnaire Python.
data_mrg = response_01.json()   # Pour Mérignac
data_sgm = reponse_02.json()    # Pour Saint-Geours-de-Maremne
data_tls = reponse_03.json()    # Pour Toulouse

# Affichage de toutes les prévisions pour les trois villes
"""
print(data_mrg["list"])
print(data_sgm["list"])
print(data_tls["list"])
"""
print()

# Liste des cinq dates pour lesquelles nous voulons afficher les prévisions météorologiques.
dates = [
    "2026-09-24",
    "2026-09-25",
    "2026-09-26",
    "2026-09-27",
    "2026-09-28",
]

# Dictionnaire permettant d'associer chaque ville aux données météo récupérées depuis l'API.
city_dict = {
    "Mérignac": data_mrg,
    "Saint-Geours-de-Maremne": data_sgm,
    "Toulouse": data_tls
}

# Liste des villes que nous voulons traiter.
cities = ["Mérignac", "Saint-Geours-de-Maremne", "Toulouse"]

for city in cities: # On parcourt chaque ville de la liste "cities".

    data = city_dict[city] # On récupère les données météo correspondantes à la ville actuelle.
                           # Par ex, si city vaut "Toulouse", data contient les données de data_tls

    print("================================")
    print(city)                                 # Affichage du nom de la ville actuelle
    print("================================")

    for date in dates:  # On parcourt chacune des cinq dates

        temperatures_min = []  # On crée une liste qui va contenir toutes les températures
                               # min trouvées pour la date actuelle

        temperatures_max = []  # On crée une liste qui va contenir toutes les températures
                               # max trouvées pour la date actuelle

        for forecast in data["list"]:  # On parcourt toutes les prévisions météo présentes dans data["list"]
            # L'API fournit plusieurs prévisions pour une même journée, toutes les 3h.

            if forecast["dt_txt"].startswith(date):  # On vérifie si la prévision correspond à la date actuelle

                # Affichage de chaque prévision avec heure, temp min et max
                """
                print(
                    forecast["dt_txt"],
                    "Min :", forecast["main"]["temp_min"],
                    "Max :", forecast["main"]["temp_max"]
                )
                """
                # On ajoute la temp min de cette prévision dans la liste temperatures_min
                temperatures_min.append(
                    forecast["main"]["temp_min"]
                )

                # On ajoute la temp max de cette prévision dans la liste temperatures_max
                temperatures_max.append(
                    forecast["main"]["temp_max"]
                )
