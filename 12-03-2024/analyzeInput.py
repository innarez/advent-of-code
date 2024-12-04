import re

def read_file(filename):
    with open(filename, mode = 'r') as file:
      lines = file.readlines()
    return "".join(line.strip() for line in lines) 

def calculate_product(filename):
    code = read_file(filename)
    exp = r"mul\((\d{1,3}),(\d{1,3})\)"
    p = 0

    clean_multiplication = re.findall(exp, code)
    for nums in clean_multiplication:
        p += (int(nums[0]) * int(nums[1]))
    return p     

def calculate_improved_product(filename):
    code = read_file(filename)
    exp = r"mul\((\d{1,3}),(\d{1,3})\)|do\((.*?)\)|don't\((.*?)\)"
    matches = [match.group() for match in re.finditer(exp, code)]
    sum = 0

    do = True
    for match in matches:
        if match.startswith("don't"):
            do = False
        elif match.startswith("do"):
            do = True
        elif match.startswith("mul") and do:
            start1 = match.find("(")
            start2 = match.find(",")
            end = match.find(")")
            sum += (int(match[start1+1:start2]) * int(match[start2+1:end]))
    return sum

if __name__ == "__main__":    
    product = calculate_product("instructions.txt")
    print(f"The sum of the products: {product}")

    improved_product = calculate_improved_product("instructions.txt")
    print(f"The improved sum of products: {improved_product}")