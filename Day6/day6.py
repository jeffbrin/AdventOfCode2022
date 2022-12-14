recentCharacters = ""
with open("input.txt", 'r') as file:
    stream = file.read()

def is_unique(string: str) -> bool:
    for c in string:
        if string.count(c) > 1:
            return False

    return True

found = False
for i, c in enumerate(stream):
    
    if len(recentCharacters) == 4:
        recentCharacters = recentCharacters[1:]
    
    recentCharacters += c
    if is_unique(recentCharacters) and len(recentCharacters) == 4:
        found = True
        break

if found:
    print(i + 1)
else:
    print("No marker found.")