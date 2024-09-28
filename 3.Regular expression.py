import re
# Define file path
file_path = r'D:\1 ust\5001 Introduction to Computational and Modeling Tools\HW1\blocklist.xml'

# Define regular expression
blockid_pattern = re.compile(r'<emItem blockID="i\d{3,4}"')
email_pattern = re.compile(r'id="(?<![\\/\^ ])[^\\/\^ ]+[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|nz)"')

with open(file_path, 'r') as file:
    for line in file:
        if blockid_pattern.search(line):
            print(f"符合条件的 blockID 行：{line}")

        if email_pattern.search(line):
            print(f"符合条件的电子邮件地址行：{line}")
