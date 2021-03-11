import re


def rearrange_name(name):
    result = re.search(r"^([\w .]*),([\w .]*)$", name)
    print('{}{}'.format(name[0],name[1])


rearrange_name('love')