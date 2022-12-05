import datetime
import re
import time
import os
import sys
import secrets
#var = None

def run_command(command, args, *values):
    value = values
    if len(values) == 1:
        value = values[0]
        
    if command == "print":
        #if args == var:
        #    return var
        #else:
        return args
    elif command == "date":
        if args == "now":
            return str(datetime.date.today())
    elif command == "input":
        inputv = input(args)
    elif command == "error":
        raise Exception(args)
    elif command == "system":
        os.system(args)
    else:
        raise Exception("Command Undefined!")

if __name__ == "__main__":
    pattern = r"wam.(?P<command>\w+)\(['\"](?P<input>.+)['\"]\)"
    with open('main.wam') as f:
        for line in f.readlines():
            matches = re.match(pattern, line)
            if matches:
                params = matches.groupdict()
                output = run_command(params['command'], params['input'])
                print(output)
#                print(f"{params.get('command')}: {params.get('input')}")
