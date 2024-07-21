def add_numbers(original_string):
    lines = original_string.split('\n')
    numbered_lines = []
    for i, line in enumerate(lines, start=1):
        numbered_lines.append(f"{i:2d} {line}")
    numbered_string = '\n'.join(numbered_lines)
    print(numbered_string)
