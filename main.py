import analyzer
import smc_an
import json


command_dict = {}


def read_text(read_from, used_checker):
    if read_from == "1":
        file_name = input("Enter path\\file_name.format:\n")
        try:
            with open(file_name, 'r') as f:
                wf = open('check out.txt', 'w')
                wf.write('')
                wf.close()
                for line in f:
                    if used_checker == '1':
                        checker = smc_an.AppClass()
                        res = checker.check_string(line[:-1])
                    else:
                        res = analyzer.check(line[:-1])
                    with open('check out.txt', 'a') as wf:
                        if res[0]:
                            wf.write(line + ' is correct\n')
                            command_dict.setdefault(res[1], 0)
                            command_dict[res[1]] += 1
                        else:
                            wf.write(line + ' is incorrect\n')
        except IOError as e:
            print('No file found.')
    else:
        input_str = input("Enter commands:\n")
        while input_str != 'end':
            if used_checker == '1':
                checker = smc_an.AppClass()
                res = checker.check_string(input_str)
            else:
                res = analyzer.check(input_str)
            if res[0]:
                print(input_str, " is correct")
                command_dict.setdefault(res[1], 0)
                command_dict[res[1]] += 1
            else:
                print(input_str, "is incorrect")
            input_str = input()


def write_res(write_to):
    if write_to == "1":
        with open("out.json", 'w') as f:
            json.dump(command_dict, f)
    else:
        print(command_dict)


if __name__ == "__main__":
    used_checker = input("Enter:\n1 to smc\n2 to use regex\n")
    while used_checker not in ["1", "2"]:
        used_checker = input("Error symbol, try again:\n")
    read_from = input("Enter:\n1 to read from file\n2 to read from console\n")
    while read_from not in ["1", "2"]:
        read_from = input("Error symbol, try again:\n")
    write_to = input("Enter:\n1 to write into file\n2 to write in console\n")
    while write_to not in ["1", "2"]:
        write_to = input("Error symbol, try again:\n")
    read_text(read_from, used_checker)
    write_res(write_to)

