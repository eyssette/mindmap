import re
import sys

def remove_yaml_header(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Recherche de l'en-tête YAML
    yaml_header_regex = r'^---\n.*?\n---\n+'
    content = re.sub(yaml_header_regex, '', content, flags=re.DOTALL)
    
    return content

def remove_html_comments(content):
    # Suppression des commentaires HTML
    comment_regex = r'<!--.*?-->'
    content = re.sub(comment_regex, '', content, flags=re.DOTALL)
    
    return content


def replace_br_tags(content):
    # Remplacement des balises <br> ou <br/> ou "\\" par un espace
    br_regex = r'<br\s?/?>'
    content = re.sub(br_regex, ' ', content, flags=re.IGNORECASE)
    content = re.sub(r' ?\\\\ ?',' ',content)
    return content

def replace_spaces(content):
    # Remplacement des doubles (et +) espaces par un espace simple
    content = re.sub(r'  +', ' ', content)
    # Remplacement des triples (et +) retours à la ligne par un double retour à la ligne
    content = re.sub(r'\n\n\n+', '\n\n', content)
    # Suppression des retours à la ligne au début du fichier
    content = re.sub(r'^\n+', '', content)
    
    return content

def replace_bold_and_italics(content):
    content = re.sub(r"\*\*(.*?)\*\*", r"\1", content)
    content = re.sub(r"\*(.*?)\*", r"\1", content)
    content = re.sub(r"_(.*?)_", r"\1", content)
    content = re.sub(r"__(.*?)__", r"\1", content)

    return content

def process_file(file_path):
    # Suppression de l'en-tête YAML
    content = remove_yaml_header(file_path)

    # Suppression des commentaires HTML
    content = remove_html_comments(content)
    
    # Remplacement des balises <br> ou <br/> par un espace
    content = replace_br_tags(content)
    
    # Remplacement des espaces inutiles
    content = replace_spaces(content)
    
    # Remplacement du gras et des italiques

    content = replace_bold_and_italics(content)

    return content

# Vérification des arguments en ligne de commande
if len(sys.argv) != 2:
    print("Usage: python md-raw.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

# Traitement du fichier Markdown
content = process_file(input_file)

# Création du fichier RAW

output_file = input_file.rsplit('.', 1)[0] + '-RAW.md'

with open(output_file, 'w') as file:
	file.write(content.rstrip())