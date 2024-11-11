import json

def is_uuid(value):
    """Vérifie si une chaîne ressemble à un UUID"""
    if not isinstance(value, str):
        return False
    # Vérifie le format UUID (8-4-4-4-12 caractères)
    parts = value.split('-')
    if len(parts) != 5:
        return False
    if len(parts[0]) != 8 or len(parts[1]) != 4 or len(parts[2]) != 4 or len(parts[3]) != 4 or len(parts[4]) != 12:
        return False
    return True

def extract_and_replace_uuids(obj, prefix):
    if isinstance(obj, dict):
        # Parcourir toutes les clés de l'objet
        for key, value in obj.items():
            # Si la valeur est une chaîne et ressemble à un UUID
            if isinstance(value, str) and is_uuid(value):
                if not value.startswith(prefix):
                    obj[key] = prefix + value
            # Si la valeur est un dictionnaire ou une liste, traitement récursif
            elif isinstance(value, (dict, list)):
                extract_and_replace_uuids(value, prefix)
                
    elif isinstance(obj, list):
        # Pour chaque élément de la liste
        for i, item in enumerate(obj):
            # Si l'élément est une chaîne et ressemble à un UUID
            if isinstance(item, str) and is_uuid(item):
                if not item.startswith(prefix):
                    obj[i] = prefix + item
            # Si l'élément est un dictionnaire ou une liste, traitement récursif
            elif isinstance(item, (dict, list)):
                extract_and_replace_uuids(item, prefix)
            
    return obj

# Demander le préfixe à l'utilisateur
prefix = input("Entrez le préfixe à ajouter aux UUIDs: ")

# Lire le fichier JSON
with open('exported_wizards.json', 'r') as f:
    data = json.load(f)

# Créer une copie et remplacer les UUIDs avec le préfixe
new_data = extract_and_replace_uuids(data.copy(), prefix)

# Sauvegarder le nouveau JSON
output_file = 'exported_wizards_with_prefix.json'
with open(output_file, 'w') as f:
    json.dump(new_data, f, indent=4)

print(f"\nNouveau fichier JSON créé: {output_file}")
print("Les UUIDs ont été préfixés avec:", prefix)