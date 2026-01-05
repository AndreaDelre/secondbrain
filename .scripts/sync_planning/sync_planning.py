import re
import os
import argparse
import difflib
import sys

# --- CONFIGURATION ---
FILE_MAIN = "./_TODO.md"
FILE_MINI = "./MiniInbox/_TODO.md"

# Couleurs pour le terminal
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def read_file(filepath):
    if not os.path.exists(filepath):
        print(f"{Colors.FAIL}Erreur : Le fichier {filepath} n'existe pas.{Colors.ENDC}")
        return None
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def extract_planning_block(content):
    pattern = r"(?ms)^(## Planning.*?)(^## |\Z)"
    match = re.search(pattern, content)
    if match:
        full_block = match.group(1)
        next_section_start = match.group(2)
        start_idx = match.start(1)
        end_idx = match.end(1)
        return content[:start_idx], full_block, content[end_idx:]
    else:
        return content, None, ""

def parse_structure(block_content):
    lines = block_content.split('\n')
    structure = []
    current_subheader = None
    current_tasks = []
    
    task_pattern = re.compile(r"^\s*-\s*\[([ xX])\]\s*(.*)")
    subheader_pattern = re.compile(r"^###\s+(.*)")

    for line in lines:
        line = line.strip()
        if not line or line == "## Planning": continue

        subheader_match = subheader_pattern.match(line)
        task_match = task_pattern.match(line)

        if subheader_match:
            if current_subheader is not None:
                structure.append((current_subheader, current_tasks))
            current_subheader = line
            current_tasks = []
        elif task_match:
            is_checked = task_match.group(1).lower() == 'x'
            task_text = task_match.group(2).strip()
            current_tasks.append({'text': task_text, 'checked': is_checked})
        
    if current_subheader is not None:
        structure.append((current_subheader, current_tasks))
        
    return structure

def merge_data(struct_a, struct_b):
    merged_sections = []
    dict_b = {title: tasks for title, tasks in struct_b}
    processed_titles_b = set()

    for title_a, tasks_a in struct_a:
        tasks_b = dict_b.get(title_a, [])
        processed_titles_b.add(title_a)
        merged_sections.append((title_a, merge_tasks(tasks_a, tasks_b)))
    
    for title_b, tasks_b in struct_b:
        if title_b not in processed_titles_b:
            merged_sections.append((title_b, tasks_b))
            
    return merged_sections

def merge_tasks(tasks_a, tasks_b):
    merged = []
    task_map = {}
    
    for t in tasks_a: task_map[t['text']] = t['checked']
    for t in tasks_b:
        if t['text'] in task_map:
            if t['checked']: task_map[t['text']] = True
        else:
            task_map[t['text']] = t['checked']
    
    processed_texts = set()
    all_tasks_source = tasks_a + tasks_b
    
    for t in all_tasks_source:
        if t['text'] not in processed_texts:
            is_checked = task_map[t['text']]
            mark = "x" if is_checked else " "
            merged.append(f"- [{mark}] {t['text']}")
            processed_texts.add(t['text'])
            
    return merged

def rebuild_block(merged_structure):
    output = ["## Planning"]
    for title, tasks in merged_structure:
        output.append(title)
        output.extend(tasks)
    return "\n".join(output) + "\n"

def show_diff(filename, old_content, new_content):
    """Affiche les différences entre l'ancien et le nouveau contenu."""
    diff = difflib.unified_diff(
        old_content.splitlines(),
        new_content.splitlines(),
        fromfile=f"Ancien {filename}",
        tofile=f"Nouveau {filename}",
        lineterm=""
    )
    
    print(f"\n{Colors.HEADER}=== Aperçu des changements pour : {filename} ==={Colors.ENDC}")
    has_changes = False
    for line in diff:
        has_changes = True
        if line.startswith('+') and not line.startswith('+++'):
            print(f"{Colors.OKGREEN}{line}{Colors.ENDC}")
        elif line.startswith('-') and not line.startswith('---'):
            print(f"{Colors.FAIL}{line}{Colors.ENDC}")
        elif line.startswith('^'):
            print(f"{Colors.OKBLUE}{line}{Colors.ENDC}")
        else:
            print(line)
    
    if not has_changes:
        print(f"{Colors.OKBLUE}Aucun changement détecté.{Colors.ENDC}")

def main():
    # Gestion des arguments
    parser = argparse.ArgumentParser(description="Synchronise la section Planning entre deux fichiers Markdown.")
    parser.add_argument("-p", "--preview", action="store_true", help="Mode Aperçu : Affiche les changements sans modifier les fichiers.")
    args = parser.parse_args()

    content_main = read_file(FILE_MAIN)
    content_mini = read_file(FILE_MINI)

    if not content_main or not content_mini: return

    # Extraction et traitement
    pre_main, block_main, post_main = extract_planning_block(content_main)
    pre_mini, block_mini, post_mini = extract_planning_block(content_mini)

    if block_main is None:
        print("Pas de section Planning dans le fichier principal.")
        return
    if block_mini is None:
        block_mini = "## Planning\n"
        pre_mini = content_mini + "\n"
        post_mini = ""

    struct_main = parse_structure(block_main)
    struct_mini = parse_structure(block_mini)
    merged_struct = merge_data(struct_main, struct_mini)
    new_block = rebuild_block(merged_struct)

    new_content_main = pre_main + new_block + post_main
    new_content_mini = pre_mini + new_block + post_mini

    # --- LOGIQUE D'ÉCRITURE OU PREVIEW ---
    
    if args.preview:
        show_diff(FILE_MAIN, content_main, new_content_main)
        show_diff(FILE_MINI, content_mini, new_content_mini)
        print(f"\n{Colors.WARNING}>>> Mode Preview terminé. Aucune modification appliquée. <<<{Colors.ENDC}")
        print("Pour appliquer, relancez sans l'option --preview")
    else:
        # Mode écriture réelle
        if new_content_main != content_main:
            write_file(FILE_MAIN, new_content_main)
            print(f"{Colors.OKGREEN}[OK] {FILE_MAIN} mis à jour.{Colors.ENDC}")
        else:
            print(f"{Colors.OKBLUE}[--] {FILE_MAIN} inchangé.{Colors.ENDC}")

        if new_content_mini != content_mini:
            write_file(FILE_MINI, new_content_mini)
            print(f"{Colors.OKGREEN}[OK] {FILE_MINI} mis à jour.{Colors.ENDC}")
        else:
            print(f"{Colors.OKBLUE}[--] {FILE_MINI} inchangé.{Colors.ENDC}")

if __name__ == "__main__":
    main()