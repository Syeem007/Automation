import re

log_file_path = r"C:\Users\Syeem\PycharmProjects\pythonProject1\sys.log"
pattern = r"ticky: INFO: ([\w ]*) "
results=[]
with open(log_file_path, 'r') as file:
    for match in re.findall(pattern,'file'):
        if type(match) is str:
            results.append(match)
        else:
            results.append("Error")

