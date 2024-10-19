def input_parse(file_path):
    headers = []
    paragraphs = []


    with open(file_path, "r") as file:
        for line_number, line in enumerate(file, start=1):
            stripped_line = line.strip()
            if stripped_line.startswith('##'):
                headers.append(stripped_line)
            elif stripped_line.startswith('#'):
                paragraphs.append(stripped_line)
    headers_final = [item[2:] for item in headers]
    paragraphs_final = [item[1:] for item in paragraphs]
    return headers_final, paragraphs_final

def replace_headers(file_path, header_content, index):
    with open(file_path, "r") as file:
        file_content = file.read()
        new_header = file_content.replace(f"[[ header{index} ]]", f"<h1>{header_content}</h1>")
    with open(file_path, "w") as file:
        file.write(new_header)

def replace_paragraphs(file_path, paragraph_content, index):
    with open(file_path, "r") as file:
        file_content = file.read()
        new_paragraph = file_content.replace(f"[[ paragraph{index} ]]", f"<p>{paragraph_content}</p>")
    with open(file_path, "w") as file:
        file.write(new_paragraph)

file_path ='./articles-text/test-article.txt'
headers, paragraphs = input_parse(file_path)

for count, item in enumerate(headers, start=1):
    replace_headers("./articles-html/10.14.24.html", headers[count-1], count)

for count, item in enumerate(paragraphs, start=1):
    replace_paragraphs("./articles-html/10.14.24.html", paragraphs[count-1], count)



