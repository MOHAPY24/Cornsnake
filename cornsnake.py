#!/usr/bin/env python3

import time
import json
import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers import PythonLexer
from io import StringIO






raw_terminal_mode = False
safety = True
saved_code = ""
active_transpiling = False

try:
    if "--unsafe" in sys.argv:
        safety = False
    else:
        safety = True
except:
    pass

try:
    if "--raw_terminal" in sys.argv:
        raw_terminal_mode = True
    else:
        raw_terminal_mode = False
except:
    pass

try:
    if "--active_transpiling" in sys.argv:
        active_transpiling = True
    else:
        active_transpiling = False
except:
    pass

ir = {

    "IR": {
        "code_ran": saved_code,
        "total_chars_code": len(saved_code),
        "last_command": None,
        "output": ""
    },

    "metadata": {
        "repl_name": "Cornsnake1",
        "repl_version": "1.0.0",
        "python_version": sys.version,
        "safety": safety,
        "raw_terminal": raw_terminal_mode,
        "os_name": os.name,
        "active_transpiling": active_transpiling,
        "current_time": time.time()

    }
}


if raw_terminal_mode != True:
    print("Cornsnake1 Python REPL")
    print("2025 Copyright Mohammed Abdelaal under the MIT License")
    print("This is a work in progress")
    os.system("python3 --version")

ptr = 0

while True:
    command = prompt(">> ", lexer=PygmentsLexer(PythonLexer), mouse_support=True)
    if ":quit" in command.lower():
        break
    elif ptr >= 20:
        if os.name == "nt":
            os.system("cls")
            if raw_terminal_mode != True:
                print("Cornsnake1 Python REPL.")
                print("2025 Copyright Mohammed Abdelaal under the MIT License.")
                print("This is a work in progress.")
                os.system("python3 --version")
        elif os.name != "nt":
            if raw_terminal_mode != True:
                os.system("clear")
                print("Cornsnake1 Python REPL.")
                print("2025 Copyright Mohammed Abdelaal under the MIT License.")
                print("This is a work in progress.")
                os.system("python3 --version")
        ptr = 0

    elif ":clear_code" in command.lower():
        saved_code = ""
    elif ":transpile" in command.lower():
        f = open("transpiled.py", "w")
        f.write(saved_code)
        f.close()
    elif ":code_history" in command.lower():
        print(saved_code)
    elif ":clear_screen" in command.lower():
        if os.name == "nt":
            os.system("cls")
            if raw_terminal_mode != True:
                print("Cornsnake1 Python REPL.")
                print("2025 Copyright Mohammed Abdelaal under the MIT License.")
                print("This is a work in progress.")
                os.system("python3 --version")
        else:
            if raw_terminal_mode != True:
                os.system("clear")
                print("Cornsnake1 Python REPL.")
                print("2025 Copyright Mohammed Abdelaal under the MIT License.")
                print("This is a work in progress.")
                os.system("python3 --version")

    
    elif ":run_code" in command.lower():
        print(exec(compile(command, "<string>", "exec")))
        ir["IR"]["code_ran"] = saved_code
        ir["IR"]["total_chars_code"] = len(saved_code)
        ir["IR"]["last_command"] = command
        captured_output = redirected_output.getvalue()
        ir["IR"]["output"] += captured_output
        sys.stdout = old_stdout
        print(captured_output)


    else:

        if "sudo" in command.lower() and safety == True:
            raise RuntimeError("Dangerous command 'sudo' in input found, use --unsafe flag to use on your own will.")
        
        saved_code += command + " \n"

        if active_transpiling != False:
            f = open("transpiled.py", "w")
            f.write(saved_code)
            f.close()
            
        if "+" in command or "-" in command or "*" in command or "/" in command:
            old_stdout = sys.stdout
            redirected_output = StringIO()
            sys.stdout =  redirected_output
            try:
                ir["IR"]["code_ran"] = saved_code
                ir["IR"]["total_chars_code"] = len(saved_code)
                ir["IR"]["last_command"] = command
                print(eval(compile(command, "<string>", "eval")))
                captured_output = redirected_output.getvalue()
                ir["IR"]["output"] += captured_output
                sys.stdout = old_stdout
                print(captured_output)
            except:
                raise
        
        else:
            old_stdout = sys.stdout
            redirected_output = StringIO()
            sys.stdout =  redirected_output
            try:
                print(exec(compile(command, "<string>", "exec")))
                ir["IR"]["code_ran"] = saved_code
                ir["IR"]["total_chars_code"] = len(saved_code)
                ir["IR"]["last_command"] = command
                captured_output = redirected_output.getvalue()
                ir["IR"]["output"] += captured_output
                sys.stdout = old_stdout
                print(captured_output)
            except:
                raise

    ptr += 1

j = open("irserial.json", "w")

j.write(json.dumps(ir, indent=2))
j.close()
    
