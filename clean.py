import re

INPUT_FILE = "mysub2.txt"
OUTPUT_FILE = "mysub2.txt"   # اگر میخوای همون فایل جایگزین بشه
KEYWORD = "&path="

def get_key(line):
    return re.split(KEYWORD, line)[0]

def remove_duplicates():
    seen = set()
    result = []

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        key = get_key(line)

        if key not in seen:
            seen.add(key)
            result.append(line)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for line in result:
            f.write(line + "\n")

if __name__ == "__main__":
    remove_duplicates()
