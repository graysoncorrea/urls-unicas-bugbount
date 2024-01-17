def unique_urls(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    unique_lines = []

    for line in lines:
        parameters = line.rsplit('=', 1)  # split on last '='
        unique_line = parameters[0]
        if unique_line not in unique_lines:
            unique_lines.append(unique_line)

    return unique_lines

filename = 'urls.txt'  # replace with your filename
unique_lines = unique_urls(filename)

for line in unique_lines:
    print(line)
