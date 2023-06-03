import os


def read_file(file_name):
    lines = []
    try:
        with open(file_name, 'r') as f:
            for line in f:
                lines.append(line.strip())
    except FileNotFoundError:
        print("File not found. ")
        return None
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        return None
    return lines


def write_file(file_name, lines):
    try:
        with open(file_name, 'w') as f:
            for line in lines:
                f.write(line + '\n')
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        return False
    f.close()
    return True


def text_create(path, name, ext, msg):
    if not os.path.exists(path):
        os.makedirs(path)
    full_path = path + name + "." + ext
    file = open(full_path, 'w')
    file.write(msg)

