import json

def is_uuid(value):
    """Vérifie si une chaîne ressemble à un UUID (avec ou sans préfixe)"""
    if not isinstance(value, str):
        return False
    
    # Si la valeur contient un underscore, vérifier seulement la partie après
    if '_' in value:
        value = value.split('_')[-1]
        
    # Vérifie le format UUID (8-4-4-4-12 caractères)
    parts = value.split('-')
    if len(parts) != 5:
        return False
    if len(parts[0]) != 8 or len(parts[1]) != 4 or len(parts[2]) != 4 or len(parts[3]) != 4 or len(parts[4]) != 12:
        return False
    return True

def extract_and_replace_uuids(obj, prefix):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, str) and is_uuid(value):
                if '_' in value:
                    uuid_part = value.split('_')[-1]
                    obj[key] = f"{prefix}_{uuid_part}"
                else:
                    obj[key] = f"{prefix}_{value}"
            elif isinstance(value, (dict, list)):
                extract_and_replace_uuids(value, prefix)
                
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            if isinstance(item, str) and is_uuid(item):
                if '_' in item:
                    uuid_part = item.split('_')[-1]
                    obj[i] = f"{prefix}_{uuid_part}"
                else:
                    obj[i] = f"{prefix}_{item}"
            elif isinstance(item, (dict, list)):
                extract_and_replace_uuids(item, prefix)
            
    return obj

def sanitize_prefix(prefix):
    """Nettoie et valide le préfixe"""
    prefix = prefix.strip()
    prefix = prefix.strip('_')
    
    if not prefix:
        raise ValueError("Le préfixe ne peut pas être vide")
    
    if '_' in prefix:
        raise ValueError("Le préfixe ne peut pas contenir d'underscore")
        
    return prefix

# Demander le préfixe à l'utilisateur avec validation
while True:
    try:
        prefix = input("Entrez le préfixe à ajouter aux UUIDs: ")
        prefix = sanitize_prefix(prefix)
        break
    except ValueError as e:
        print(f"Erreur: {e}")
        print("Veuillez réessayer.")

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