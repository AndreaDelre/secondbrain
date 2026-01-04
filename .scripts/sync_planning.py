#!/usr/bin/env python3
"""Sync the "## Planning" sections between two markdown files.

Usage:
  python3 .scripts/sync_planning.py [file1] [file2] [--dry-run]

By default files are `./_TODO.md` and `./Mini Inbox/_TODO.md`.
The script backs up the original files to `.bak` files before writing.
"""
import argparse
import shutil
import re
from pathlib import Path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str):
    path.write_text(text, encoding="utf-8")


def extract_planning_section(text: str):
    lines = text.splitlines()
    header_idx = None
    # capture the header level (e.g. '##') so we can include deeper sub-headers (###, ####)
    # accept 'Planning' followed by optional punctuation or text (e.g. '## Planning:', '## Planning (Done)')
    header_re = re.compile(r"^(#{1,6})\\s*Planning\b.*$", re.IGNORECASE)
    planning_level = None
    for i, line in enumerate(lines):
        m = header_re.match(line.strip())
        if m:
            header_idx = i
            planning_level = len(m.group(1))
            break
    if header_idx is None:
        return None  # no Planning section

    # find end: next header with level <= planning_level (stop at same-or-higher level)
    end_idx = len(lines)
    for j in range(header_idx + 1, len(lines)):
        m2 = re.match(r"^\\s*(#{1,6})\\s+", lines[j])
        if m2 and len(m2.group(1)) <= planning_level:
            end_idx = j
            break

    before = "\n".join(lines[:header_idx])
    header_line = lines[header_idx]
    section = lines[header_idx + 1:end_idx]
    after = "\n".join(lines[end_idx:])
    return {
        "before": before,
        "header": header_line,
        "section_lines": section,
        "after": after,
    }


def parse_tasks(lines):
    task_re = re.compile(r"^\s*[-*]\s*\[( |x|X)\]\s*(.+)$")
    tasks = []
    other = []
    for ln in lines:
        m = task_re.match(ln)
        if m:
            checked = m.group(1).lower() == 'x'
            text = m.group(2).strip()
            tasks.append((text, checked, ln))
        else:
            other.append(ln)
    return tasks, other


def normalize_task_text(t: str) -> str:
    return re.sub(r"\s+", " ", t.strip())


def merge_tasks(tasks_a, tasks_b):
    # tasks_*: list of (text, checked, orig_line)
    order = []
    merged = {}

    def add_from_list(tasks):
        for text, checked, _ in tasks:
            key = normalize_task_text(text)
            if key not in merged:
                merged[key] = {"text": text, "checked": checked}
                order.append(key)
            else:
                # if either side checked, mark checked
                merged[key]["checked"] = merged[key]["checked"] or checked

    add_from_list(tasks_a)
    add_from_list(tasks_b)

    merged_list = [(merged[k]["text"], merged[k]["checked"]) for k in order]
    return merged_list


def build_section(header_line: str, other_lines, merged_tasks):
    out = []
    out.append(header_line)
    out.append("")
    # include other_lines (non-task lines) if any, before tasks
    if other_lines:
        out.extend(other_lines)
        if other_lines[-1].strip() != "":
            out.append("")
    for text, checked in merged_tasks:
        mark = "x" if checked else " "
        out.append(f"- [{mark}] {text}")
    out.append("")
    return "\n".join(out)


def sync_files(path_a: Path, path_b: Path, dry_run=False, backup=True):
    txt_a = read_text(path_a)
    txt_b = read_text(path_b)

    sec_a = extract_planning_section(txt_a)
    sec_b = extract_planning_section(txt_b)

    if sec_a is None and sec_b is None:
        print("No 'Planning' section found in either file.")
        return 1

    # If one side missing, treat its section as empty
    if sec_a is None:
        sec_a = {"before": txt_a.strip(), "header": "## Planning", "section_lines": [], "after": ""}
    if sec_b is None:
        sec_b = {"before": txt_b.strip(), "header": "## Planning", "section_lines": [], "after": ""}

    tasks_a, other_a = parse_tasks(sec_a["section_lines"])
    tasks_b, other_b = parse_tasks(sec_b["section_lines"])

    merged = merge_tasks(tasks_a, tasks_b)

    new_section = build_section(sec_a["header"], other_a or other_b, merged)

    new_txt_a = (sec_a["before"].rstrip() + "\n\n" + new_section + sec_a["after"]) if sec_a["before"] else (new_section + sec_a["after"]) 
    new_txt_b = (sec_b["before"].rstrip() + "\n\n" + new_section + sec_b["after"]) if sec_b["before"] else (new_section + sec_b["after"]) 

    if dry_run:
        print("--- DRY RUN: merged Planning section ---")
        print(new_section)
        return 0

    # backups
    if backup:
        shutil.copy(path_a, path_a.with_suffix(path_a.suffix + ".bak"))
        shutil.copy(path_b, path_b.with_suffix(path_b.suffix + ".bak"))

    write_text(path_a, new_txt_a)
    write_text(path_b, new_txt_b)
    print(f"Updated {path_a} and {path_b} (backups created with .bak suffix)")
    return 0


def main():
    p = argparse.ArgumentParser(description="Sync '## Planning' sections between two markdown files")
    p.add_argument("file_a", nargs="?", default="_TODO.md")
    p.add_argument("file_b", nargs="?", default="Mini Inbox/_TODO.md")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--no-backup", dest="backup", action="store_false")
    args = p.parse_args()

    path_a = Path(args.file_a)
    path_b = Path(args.file_b)

    if not path_a.exists():
        print(f"File not found: {path_a}")
        return 2
    if not path_b.exists():
        print(f"File not found: {path_b}")
        return 2

    return sync_files(path_a, path_b, dry_run=args.dry_run, backup=args.backup)


if __name__ == "__main__":
    raise SystemExit(main())
