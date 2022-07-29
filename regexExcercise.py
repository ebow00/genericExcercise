import re
"""
Our definition of a secure filename is:
- The filename must start with an English letters or a number (a-zA-Z0-9).
- The filename can **only** contain English letters, numbers and symbols among these four: `-_()`.
- The filename must end with a proper file extension among `.jpg`, `.jpeg`, `.png` and `.gif`
"""


def is_filename_safe(filename):
    # you only need to change the regular expression (regex) below
    regex = '^[0-9a-zA-Z][0-9a-zA-Z-_()]*(\.jpg|\.jpeg|\.png|\.gif)$'
    return re.match(regex, filename) is not None

filenames = ['booba.jpg', 'booba.jpeg', 'booba.jpeg', 'booba.png', 'booba.gif', '0.jpg', '01.opp', '.jpg', '', 'sdf', '34543', 'test-.ggif']

for filename in filenames:
    print(is_filename_safe(filename))
