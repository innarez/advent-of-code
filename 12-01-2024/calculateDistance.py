import csv


def get_distance_lists(file_name):
    d1 = []
    d2 = []

    with open(file_name) as csvfile:
      reader = csv.reader(csvfile, delimiter=' ',)
      for row in reader:
          d1.append(int(row[0]))
          d2.append(int(row[3]))
    return d1, d2

def get_distances(file_name):
    d1, d2 = get_distance_lists(file_name)
    d1.sort()
    d2.sort()

    total_distance = 0

    for loc1, loc2 in zip(d1, d2):
        total_distance += abs(loc1 - loc2)
    
    return total_distance

def get_similarity_score(file_name):
    d1, d2 = get_distance_lists(file_name)
    loc_ids = {}

    for loc in d2:
        total = loc_ids.get(loc, 0) + 1
        loc_ids[loc] = total
    
    sim = 0
    for loc in d1:
        sim += loc_ids.get(loc, 0) * loc
    
    return sim

if __name__ == "__main__":
    file_name = "locationIds.csv"
    
    distance = get_distances(file_name)
    print(distance)

    similarity = get_similarity_score(file_name)
    print(similarity)
