# Préfixeur d'UUID

Un script Python simple qui permet d'ajouter un préfixe à tous les UUIDs trouvés dans un fichier JSON.

## Description

Cette application permet de :
- Lire un fichier JSON contenant des UUIDs
- Ajouter un préfixe personnalisé à tous les UUIDs trouvés
- Sauvegarder le résultat dans un nouveau fichier JSON

## Prérequis

- Python 3.x
- Un fichier JSON source contenant des UUIDs (`exported_wizards.json`)

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers
2. Assurez-vous que votre fichier JSON source est dans le même répertoire que `app.py`

## Utilisation

1. Exécutez le script :
```bash
python app.py
```

2. Le script demandera le préfixe à ajouter, par exemple `Kimaiko_`

3. Le script créera un nouveau fichier JSON avec le préfixe ajouté, par exemple `exported_wizards_with_prefix.json`

