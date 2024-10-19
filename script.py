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

def writetofile(file_path, headers, index):
    with open(file_path, "r") as file:
        file_content = file.readlines()
        file_content.insert(index+10, f"<h1>{headers[index]}</h1>\n")

    with open("./articles-html/10.14.24.html", "w") as file:
        file.writelines(file_content)

headers, paragraphs = input_parse("./articles-text/test-article.txt")

for count, item in enumerate(headers):
    writetofile("./articles-html/10.14.24.html", headers, count)




