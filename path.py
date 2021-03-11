import sys
import os

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write('this is a new line')
else:
    print('the file is already exists{}'.format(filename))
    sys.exit(1)
