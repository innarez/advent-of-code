def read_file(filename):
    with open(filename, mode="r") as file:
        return [line.rstrip("\n") for line in file.readlines()]
    
def findXWord(filename):
    matches = 0
    letters = read_file(filename)
    MAX_ROW = len(letters)
    MAX_COL = len(letters[0])
    valid_matches = {"MMSS", "SSMM", "MSMS", "SMSM"}

    for r in range(1, MAX_ROW - 1):
        for c in range(1, MAX_COL - 1):
            if letters[r][c] == "A":
                top_left = letters[r-1][c-1]
                top_right = letters[r-1][c+1]
                bottom_left = letters[r+1][c-1]
                bottom_right = letters[r+1][c+1]

                result = top_left + top_right + bottom_left + bottom_right

                if result in valid_matches:
                    matches += 1

    return matches

if __name__ == "__main__":
    wordCount = findXWord("wordSearch.txt")
    print(f"x-mas word count: {wordCount}")
