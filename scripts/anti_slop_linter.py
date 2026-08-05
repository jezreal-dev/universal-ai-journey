import os, re

repo_path = '/home/jmomoh/universal-ai-journey'
slop_words = ['delve', 'tapestry', 'game-changer', 'seamless', 'elevate', 'empower', 'robust', 'dynamic', 'unlock', 'pivotal', 'harness', 'spearhead', 'groundbreaking', 'realm']
slop_pattern = re.compile(r'\b(' + '|'.join(slop_words) + r')\b', re.IGNORECASE)

matches = []
for root, dirs, files in os.walk(repo_path):
    if '.git' in root or '.venv' in root or 'scratch' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith('.md') and f != 'STARTING_PROMPT.md' and not f.endswith('source_lecture.md'):
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as file:
                lines = file.readlines()
                for line_idx, line in enumerate(lines, 1):
                    for match in slop_pattern.finditer(line):
                        matches.append((os.path.relpath(fpath, repo_path), line_idx, match.group(0)))

print(f"Anti-Slop Linter Audit (Generated Documentation): {len(matches)} matches found.")
if matches:
    for m in matches:
        print(f"  - {m[0]}:{m[1]} -> \"{m[2]}\"")
else:
    print("✅ PASSED! 0 slop words found across all generated documentation!")
