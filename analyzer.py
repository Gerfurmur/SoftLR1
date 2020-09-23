import re


def check(string):
    if len(string) > 80:
        return False
    res = re.match(r"[a-zA-Z]+ *( +-[a-zA-Z]+)*( +[a-zA-Z]+)* *\n?$", string)
    if res != None:
        if string == res.group(0):
            com_name = re.match(r"[a-zA-Z]+", string).group(0)
            return True, com_name
    return False, None

