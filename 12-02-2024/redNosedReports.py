import csv

def get_reports(filename):
  with open(filename) as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")
    return [[int(r) for r in row if r] for row in reader]

def check_row(row):
    left = 0
    right = 1
    direction = 1 if row[left] < row[right] else -1
    while right < len(row):
      if abs(row[right] - row[left]) <= 3 and ((direction > 0 and row[left] < row[right]) or (direction < 0 and row[left] > row[right])):
         left += 1
         right +=1
      else:
         return False
    if right == len(row):
        return True
    return False

def check_safety_p1(filename):
    reports = get_reports(filename)
    safe = 0

    for r in reports:
      isSafe = check_row(r)
      if isSafe:
         safe += 1
    return safe

def check_safety_p2(filename):
    reports = get_reports(filename)
    safe = 0

    for r in reports:
      isSafe = check_row(r)
      
      if not isSafe:
        updatedRows = [r[:i] + r[i+1:] for i in range(len(r))]
        if not any(check_row(row) for row in updatedRows) is False:
          safe += 1
      else:
         safe += 1     
    return safe

if __name__ == "__main__":
    filename = "reports.txt"
    safe_reports = check_safety_p1(filename)
    print(f"safe reports: {safe_reports}")
    safe_reports2 = check_safety_p2(filename)
    print(f"safe reports 2: {safe_reports2}")