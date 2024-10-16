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

file_path ='./articles-text/test-article.txt'
headers, paragraphs = input_parse(file_path)
header1, header2, header3, header4, header5 = headers
p1, p2, p3, p4, p5 = paragraphs

print(header1)
print(header2)
print(header3)
print(header4)
print(header5)

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)

