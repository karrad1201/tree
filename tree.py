import os


def generate_tree(startpath, ignore_patterns=None):
    if ignore_patterns is None:
        ignore_patterns = {'.git', '__pycache__', '.pyc', '.vscode', '.idea'}

    def should_ignore(path):
        return any(pattern in path for pattern in ignore_patterns)

    tree_lines = []

    for root, dirs, files in os.walk(startpath):
        # Фильтруем директории
        dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d))]
        files = [f for f in files if not should_ignore(os.path.join(root, f))]

        level = root.replace(startpath, '').count(os.sep)
        indent = '│   ' * (level - 1) + '├── ' if level > 0 else ''
        if level > 0:
            tree_lines.append(f'{indent}{os.path.basename(root)}/')

        subindent = '│   ' * level + '├── '
        for file in files:
            tree_lines.append(f'{subindent}{file}')

    return '\n'.join(tree_lines)


if __name__ == "__main__":
    structure = generate_tree('.')
    print(structure)
