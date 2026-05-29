"""Script para adicionar comentários de instalação acima de imports externos.
Procura por imports de: pygame, requests, plotly, matplotlib, pytest, django
Adiciona uma linha de comentário: "# Requisitos: pip install <pacote>" antes da linha de import.
"""
import re
from pathlib import Path

repo_root = Path(__file__).resolve().parents[1]
patterns = {
    'pygame': re.compile(r'^\s*import\s+pygame', re.M),
    'requests': re.compile(r'^\s*import\s+requests', re.M),
    'plotly': re.compile(r'^\s*import\s+plotly(?:\.|\s|$)|^\s*import\s+plotly\.express|^\s*from\s+plotly', re.M),
    'matplotlib': re.compile(r'^\s*import\s+matplotlib\.pyplot|^\s*import\s+matplotlib', re.M),
    'pytest': re.compile(r'^\s*import\s+pytest', re.M),
    'django': re.compile(r'^\s*import\s+django|^\s*from\s+django', re.M),
}

pkg_map = {
    'pygame': 'pygame',
    'requests': 'requests',
    'plotly': 'plotly',
    'matplotlib': 'matplotlib',
    'pytest': 'pytest',
    'django': 'django',
}

files = list(repo_root.rglob('*.py'))
modified = []
for file in files:
    try:
        text = file.read_text(encoding='utf-8')
    except Exception:
        continue
    original = text
    lines = text.splitlines()
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        added = False
        for key, pat in patterns.items():
            if pat.match(line):
                # check previous 2 lines for existing comment to avoid duplicates
                prev_block = '\n'.join(lines[max(0, i-3):i])
                install_comment = f"# Requisitos: pip install {pkg_map[key]}"
                if install_comment not in prev_block:
                    new_lines.append(install_comment)
                    new_lines.append(f"# Import: {line.strip()}")
                    added = True
                break
        new_lines.append(line)
        i += 1
    new_text = '\n'.join(new_lines) + ('\n' if original.endswith('\n') else '')
    if new_text != original:
        file.write_text(new_text, encoding='utf-8')
        modified.append(str(file.relative_to(repo_root)))

print('Arquivos modificados:', len(modified))
for m in modified:
    print('-', m)
