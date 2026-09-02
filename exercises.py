"""
PRATIQUE : List & Dict Comprehension - Parsing de configs
Durée cible : 20 minutes (~4 min par exercice)
Fais chaque exercice, décommente le print, vérifie, puis passe au suivant.
"""

# ============================================================
# EXERCICE 1 (4 min) - Filtrer + transformer les clés
# ============================================================
config_brut = {
    "DB_HOST": "localhost",
    "DB_PORT": "5432",
    "DB_NAME": "myapp",
    "APP_DEBUG": "true",
    "APP_TIMEOUT": "30",
    "CACHE_TTL": "120",
}

# TODO: crée db_config en ne gardant que les clés qui commencent par "DB_",
# en retirant le préfixe "DB_" et en mettant la clé en minuscule.
# Résultat attendu: {'host': 'localhost', 'port': '5432', 'name': 'myapp'}

db_config = {key[3:].lower() : value for key, value in config_brut.items() if key.startswith("DB_")}  # <-- remplace par une dict comprehension

print(db_config)


# ============================================================
# EXERCICE 2 (4 min) - Conversion de types avec condition
# ============================================================
# TODO: crée config_typee où :
# - "true"/"false" (peu importe la casse) deviennent des bool Python
# - les chaînes numériques deviennent des int
# - le reste reste une string
# Astuce: écris une petite fonction convertir(v) puis utilise-la dans la comprehension.

def convertir(v: str):
    # TODO
    if v.lower() == "true":
        return True
    elif v.lower() == "false":
        return False
    elif v.isdigit():
        return int(v)
    else:
        return v

config_typee = {key:convertir(value) for key, value in config_brut.items()}  # <-- dict comprehension utilisant convertir()

print(config_typee)
# Attendu: {'DB_HOST': 'localhost', 'DB_PORT': 5432, 'DB_NAME': 'myapp',
#           'APP_DEBUG': True, 'APP_TIMEOUT': 30, 'CACHE_TTL': 120}


# ============================================================
# EXERCICE 3 (4 min) - Validation avec filtre + liste des erreurs
# ============================================================
config_avec_erreurs = {
    "timeout": "30",
    "retries": "abc",
    "max_size": "-1",
    "workers": "4",
}

# TODO 3a: crée config_valide (dict comprehension) qui ne garde que les valeurs
# qui sont des entiers positifs (>= 0), converties en int.
# Attendu: {'timeout': 30, 'workers': 4}

config_valide = {key : int(value) for key, value  in config_avec_erreurs.items() if value.isdigit() and int(value) >= 0}  # <-- dict comprehension avec filtre et conversion en int

# TODO 3b: crée erreurs (list comprehension) avec les clés invalides.
# Attendu: ['retries', 'max_size']

erreurs = [key for key, value in config_avec_erreurs.items() if not(value.isdigit()) or int(value) < 0]  # <-- list comprehension avec filtre

print(config_valide)
print(erreurs)


# ============================================================
# EXERCICE 4 (4 min) - Config imbriquée (clés à points)
# ============================================================
config_plat = {
    "db.host": "localhost",
    "db.port": "5432",
    "app.name": "MonApp",
    "app.debug": "true",
}

# TODO: crée config_imbrique, un dict de dicts groupé par section
# (la partie avant le premier point).
# Attendu: {'db': {'host': 'localhost', 'port': '5432'},
#           'app': {'name': 'MonApp', 'debug': 'true'}}
# Astuce: récupère d'abord l'ensemble des sections avec un set comprehension,
# puis construis le dict imbriqué avec une dict comprehension imbriquée.

sections = set(key.split(".")[0] for key in config_plat)       # <-- set comprehension
config_imbrique = {section: {k.split(".")[1]: v for k, v in config_plat.items() if k.startswith(f"{section}.")} for section in sections}   # <-- dict comprehension imbriquée

print(config_imbrique)


# ============================================================
# EXERCICE 5 (4 min) - BONUS WSL : normaliser des chemins
# ============================================================
config_chemins = {
    "log_path": "C:\\Users\\Moi\\logs",
    "data_path": "D:\\projets\\data",
    "linux_path": "/home/moi/config",
}

# TODO: crée config_wsl où chaque chemin Windows (contient ":\\")
# est converti en chemin WSL /mnt/<lettre minuscule>/...
# Les chemins déjà Unix restent inchangés.
# Attendu: {'log_path': '/mnt/c/Users/Moi/logs',
#           'data_path': '/mnt/d/projets/data',
#           'linux_path': '/home/moi/config'}

def win_vers_wsl(chemin: str) -> str:
    # TODO
    chemin = chemin.replace("\\", "/")
    if ":\\" in chemin:
        Lettre = chemin[0].lower()
        chemin =f"/mnt/{lettre}{chemin[2:]}"
    return chemin

config_wsl = {key: win_vers_wsl(value) for key,value in config_chemins.items()}  # <-- dict comprehension utilisant win_vers_wsl()

print(config_wsl)


# ============================================================
# Décommente à la fin pour tout vérifier d'un coup
# ============================================================
if __name__ == "__main__":
    print("1 - db_config:", db_config)
    print("2 - config_typee:", config_typee)
    print("3 - config_valide:", config_valide)
    print("3 - erreurs:", erreurs)
    print("4 - config_imbrique:", config_imbrique)
    print("5 - config_wsl:", config_wsl)