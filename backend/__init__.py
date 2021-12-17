import os
import re


__title__ = "CRM"
__author__ = "Mohamed Rageh"
__name__ = "CRM"

# Synonyms.
TITLE = __title__

try:
    with open(".env") as file:
        content = file.read()
except IOError:
    content = ""

for line in content.splitlines():
    match = re.match(r"\A([A-Za-z_0-9]+)=(.*)\Z", line)

    if match:
        k, v = match.group(1), match.group(2)
        print(k, v)

        single = re.match(r"\A'(.*)'\Z", v)

        if single:
            v = single.group(1)

        double = re.match(r'\A"(.*)"\Z', v)

        if double:
            v = re.sub(r"\\(.)", r"\1", double.group(1))

        os.environ.setdefault(k, v)
