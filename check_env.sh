#!/usr/bin/env bash
set -euo pipefail

# Couleurs ANSI pour sorties propres dans le terminal
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}==========================================${NC}"
echo -e "${BLUE} DIAGNOSTIC DE L'ENVIRONNEMENT MLOPS ${NC}"
echo -e "${BLUE}==========================================${NC}"

# 1. Gestion de la variable d'environnement
export APP_ENV="${APP_ENV:-local_development}"
echo -e "Environnement cible : ${GREEN}${APP_ENV}${NC}"

# 2. Vérification de Python 3
if command -v python3 &> /dev/null; then
	PY_VER=$(python3 --version)
	echo -e "[OK] Python installé : ${GREEN}${PY_VER}${NC}"
else
	echo -e "[ERREUR] Python 3 est introuvable !" >&2
	exit 1
fi

# 3. Vérification de Git
if command -v git &> /dev/null; then
	echo -e "[OK] Git installé : ${GREEN}$(git --version)${NC}"
else
	echo -e "[ERREUR] Git est introuvable !" >&2
	exit 1
fi

# 4. Vérification et création du dossier data/
if [ ! -d "data" ]; then
	echo "Dossier 'data/' manquant. Création automatique..."
	mkdir -p data/raw data/processed
fi

echo -e "${GREEN}>>> Succès : Environnement opérationnel pour le Jour 5 !${NC}"
