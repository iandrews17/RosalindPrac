def read_file_lines(file_path):
    with open(file_path) as f:
        return [l.strip() for l in f.readlines()]

def read_file_spaces(file_path):
    with open(file_path) as f:
        return f.read().split()