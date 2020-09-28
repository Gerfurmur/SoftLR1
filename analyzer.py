import re


def check(string):
    if len(string) > 80:
        return False
    res = re.match(r"([a-zA-Z]+)( +-[a-zA-Z]+)*( +[a-zA-Z]+)* *\n?$", string)
    if res != None:
        return True, res.group(1)
    return False, None

