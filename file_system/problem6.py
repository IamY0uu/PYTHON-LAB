#  copy a file's (this.txt) content in another file (copy.txt) 
with open("this.txt") as f:
    content = f.read()
with open("copy.txt", "w") as f:
    f.write(f"copied content: {content}")

    