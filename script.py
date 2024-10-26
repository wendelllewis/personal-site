def input_parse(file_path):
    lines = []

    with open(file_path, "r") as file:
        for line_number, line in enumerate(file, start=1):
            stripped_line = line.strip()
            lines.append(stripped_line)
        for i, element in enumerate(lines):
            if element.startswith('##'):
                lines[i] = '<h1>' + element[2:] + '</h1>'
            elif element.startswith('#'):
                lines[i] = '<p>' + element[1:] + '</p>'
            elif element.startswith('@'):
                lines[i] = '<img src="' + element[1:] + '">'
    return lines
def writetofile(file_path, code):
    with open(file_path, "r") as file:
        file_content = file.readlines()
    for count, line in enumerate(code):
        file_content.insert(count + 10, line + '\n')
        file_content.insert(count + 11, '\n')
    with open("./articles-html/10.14.24.html", "w") as file:
        file.writelines(file_content)

input_name = input('input name?')
output_name = input('output name?')

input_path = f"./articles-text/{input_name}.txt"
output_path = f'./articles-html/{output_name}.html'

article_text = input_parse(input_path)
writetofile(output_path, article_text)









# input_name = input('input name?')
# output_name = input('output name?')

# input_path = f"./articles-text/{input_name}.txt"
# output_path = f'./articles-html/{output_name}.html'

# headers, paragraphs, images = input_parse(input_path)
# writetofile(output_path, headers, paragraphs, images)




