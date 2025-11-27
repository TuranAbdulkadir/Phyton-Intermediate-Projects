import markdown

text = """
# Hello World
This is **bold** text and *italic* text.
- List item 1
- List item 2
"""
html = markdown.markdown(text)
print(html)

with open("output.html", "w") as f:
    f.write(html)