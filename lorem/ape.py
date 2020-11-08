import difflib
with open('lorem1.txt') as f1:
    f1_text = f1.read()
with open('lorem2.txt') as f2:
    f2_text = f2.read()
# Find and print the diff:


changes = [ data for data in difflib.ndiff(f1_text, f2_text) if data.startswith('+') or data.startswith('- ')]

print(changes, end="")

flag = ""

for i in changes:
    flag += i[len(i) - 1]
print(flag)
