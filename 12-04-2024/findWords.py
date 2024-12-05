def read_file(filename):
    with open(filename, mode="r") as file:
        return [line.rstrip("\n") for line in file.readlines()]

def check_right(letters, word, r, c, max):
    found = 0
    for k in word:
        if c >= max :
            break
        if k == letters[r][c]:
            found += 1
            c += 1
    return 1 if found == 4 else 0

def check_left(letters, word, r, c):
    found = 0
    for k in word:
        if c < 0:
            break
        if k == letters[r][c]:
            found += 1
            c -= 1
    return 1 if found == 4 else 0

def check_up(letters, word, r, c):
    found = 0
    for k in word:
        if r < 0:
            break
        if k == letters[r][c]:
            found += 1
            r -= 1
    return 1 if found == 4 else 0

def check_down(letters, word, r, c, max):
    found = 0
    for k in word:
        if r >= max :
            break
        if k == letters[r][c]:
            found += 1
            r += 1
    return 1 if found == 4 else 0

def check_top_left(letters, word, r, c):
    found = 0
    for k in word:
        if r < 0 or c < 0:
            break
        if k == letters[r][c]:
            found += 1
            r -= 1
            c -= 1
    return 1 if found == 4 else 0

def check_bottom_right(letters, word, r, c, max_r, max_c):
    found = 0
    for k in word:
        if r >= max_r or c >= max_c :
            break
        elif k == letters[r][c]:
            found += 1
            r += 1
            c +=1
    return 1 if found == 4 else 0

def check_bottom_left(letters, word, r, c, max_r):
    found = 0
    for k in word:
        if r >= max_r or c < 0:
            break
        elif k == letters[r][c]:
            found += 1
            r += 1
            c -= 1
    return 1 if found == 4 else 0
    
def check_top_right(letters, word, r, c, max_c):
    matches = 0
    found = 0
    for k in word:
        if c >= max_c  or r < 0:
            break
        elif k == letters[r][c]:
            found += 1
            r -= 1
            c +=1
    if found == 4:
        matches += 1
    return matches

def findWord(filename, word):
    matches = 0
    letters = read_file(filename)
    MAX_ROW = len(letters)
    MAX_COL = len(letters[0])

    for r in range(MAX_ROW):
        for c in range(MAX_COL):
            if letters[r][c] == "X":
                matches += check_right(letters, word, r, c, MAX_COL)
                matches += check_left(letters, word, r, c)
                matches += check_up(letters, word, r, c)
                matches += check_down(letters, word, r, c, MAX_ROW)
                matches += check_top_left(letters, word, r, c)
                matches += check_bottom_right(letters, word, r, c, MAX_ROW, MAX_COL)
                matches += check_bottom_left(letters, word, r, c, MAX_ROW)
                matches += check_top_right(letters, word, r, c, MAX_COL)

    return matches

if __name__ == "__main__":
    word = "XMAS"
    wordCount = findWord("wordSearch.txt", word)
    print(f"word count: {wordCount}")
