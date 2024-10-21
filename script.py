def input_parse(file_path):
    headers = []
    paragraphs = []
    images = []

    with open(file_path, "r") as file:
        for line_number, line in enumerate(file, start=1):
            stripped_line = line.strip()
            if stripped_line.startswith('##'):
                headers.append(stripped_line)
            elif stripped_line.startswith('#'):
                paragraphs.append(stripped_line)
            elif stripped_line.startswith('@'):
                images.append(stripped_line)
    headers_final = [item[2:] for item in headers]
    paragraphs_final = [item[1:] for item in paragraphs]
    images_final = [item[1:] for item in images]

    return headers_final, paragraphs_final

def writetofile(file_path, headers, paragraphs):
    with open(file_path, "r") as file:
        file_content = file.readlines()
    for count, header in enumerate(headers):
        file_content.insert(count * 2 + 9, f"<h1>{header}</h1>\n")
        if count < len(paragraphs):
            file_content.insert(count * 2 + 10, f"<p>{paragraphs[count]}</p>\n")
    with open("./articles-html/10.14.24.html", "w") as file:
        file.writelines(file_content)

input_name = input('input name?')
output_name = input('output name?')

input_path = f"./articles-text/{input_name}.txt"
output_path = f'./articles-html/{output_name}.html'

headers, paragraphs = input_parse(input_path)
writetofile(output_path, headers, paragraphs)




