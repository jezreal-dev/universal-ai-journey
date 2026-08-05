import os

repo_path = '/home/jmomoh/universal-ai-journey'
legacy_dirs = ['01-intro-universal-ai', '02-python-part1', '03-python-part2', '04-data-analytics-ml', '05-supervised-unsupervised-learning']

for d in legacy_dirs:
    m_path = os.path.join(repo_path, 'modules', d)
    files = sorted(os.listdir(m_path))
    print(f"=== {d} ===")
    print(files)
