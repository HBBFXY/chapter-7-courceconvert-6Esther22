import keyword
with open("random_int.py", "r") as source_file:
    content = source_file.read()
processed_lines = []
for line in content.splitlines():  
    words = line.split()  
    processed_words = []
    for word in words:
        if not keyword.iskeyword(word):
            word = word.upper()
        processed_words.append(word)
    processed_line = " ".join(processed_words)
    processed_lines.append(processed_line)
processed_content = "\n".join(processed_lines)
with open("random_int_converted.py", "w") as target_file:
    target_file.write(processed_content)
print("文件转换完成！新文件为 random_int_converted.py")
