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