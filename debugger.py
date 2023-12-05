import re
import os

def check_vulnerable_functions(php_file):
    vulnerable_functions = ['execute_cmd', 'exec', 'system', 'passthru', 'shell_exec', 'eval', 'assert', 'popen']

    with open(php_file, 'r') as file:
        php_code = file.read()
        
        for func in vulnerable_functions:
            pattern = r'\b' + func + r'\s*\('  # Regular expression pattern to find function usage
            matches = re.findall(pattern, php_code)
            if matches:
                print(f"Vulnerable function '{func}' found in the PHP code.")
                with open(php_path, 'r') as php_file:
                    line_number = 0
                    for line in php_file:
                        line_number += 1
                        match = re.findall(pattern, line)
                        if match:
                            print(f"File: {php_path}, Line: {line_number}, Code: {line.strip()}")
            else:
                print(f"No '{func}' vulnerable function found on {php_path}.")

if __name__ == '__main__':
	# Replace 'path_to_php_files_directory' with the directory containing your PHP files
	php_path = input('Type the directory path of the PHP code to check: ')
	check_vulnerable_functions(php_path)
