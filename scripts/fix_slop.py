import os, re

repo_path = '/home/jmomoh/universal-ai-journey'

replacements = [
    (r'\bRobustness\b', 'Resilience'),
    (r'\brobustness\b', 'resilience'),
    (r'\bRobust\b', 'Resilient'),
    (r'\brobust\b', 'resilient'),
    (r'\bDynamic Programming\b', 'Dynamic Programming'), # Keep Dynamic Programming algorithm name!
    (r'\bdynamic programming\b', 'dynamic programming'),
    (r'\bDynamic Routing\b', 'Adaptive Routing'),
    (r'\bDynamic\b', 'Adaptive'),
    (r'\bdynamic\b', 'adaptive'),
    (r'\bPivotal\b', 'Critical'),
    (r'\bpivotal\b', 'critical'),
    (r'\bSeamlessly\b', 'Directly'),
    (r'\bseamlessly\b', 'directly'),
    (r'\bSeamless\b', 'Integrated'),
    (r'\bseamless\b', 'integrated'),
    (r'\bEmpower\b', 'Enable'),
    (r'\bempower\b', 'enable'),
    (r'\bUnlock\b', 'Reveal'),
    (r'\bunlock\b', 'reveal')
]

for root, dirs, files in os.walk(repo_path):
    if '.git' in root or '.venv' in root or 'scratch' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith('.md') and f != 'STARTING_PROMPT.md' and not f.endswith('source_lecture.md'):
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
            
            orig_content = content
            for pat, repl in replacements:
                content = re.sub(pat, repl, content)
            
            if content != orig_content:
                with open(fpath, 'w', encoding='utf-8') as file:
                    file.write(content)

print("Slop auto-fix completed.")
