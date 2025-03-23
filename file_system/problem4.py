# replace a word from file by updating it
with open("replace.txt") as f:
    content = f.read()  # File read karni hai

# Replace "Donkey" with "Elephant"
lc = content.lower()
updated_content = lc.replace("donkey", "elePHONT")

with open("replace.txt", "w") as f:
    f.write(updated_content)  # Updated content overwrite karna

print("Replaced 'Donkey' with 'elePHONT' successfully!")

        