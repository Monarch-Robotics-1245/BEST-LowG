import os
import re
import unittest

# Define the regex patterns for camelCase and SCREAMING_SNAKE_CASE
CAMEL_CASE_PATTERN = re.compile(r'^[a-z]+(?:[A-Z][a-z]*)*$')
SCREAMING_SNAKE_CASE_PATTERN = re.compile(r'^[A-Z]+(?:_[A-Z]+)*$')

# Regex pattern to find variable assignments
VARIABLE_ASSIGNMENT_PATTERN = re.compile(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=')

class TestVariableNamingConventions(unittest.TestCase):

    def test_variable_naming(self):
        src_folder = '../../src'  # Adjust path to your src folder
        all_files = self.find_variables_in_src_folder(src_folder)

        for file_path, variables in all_files.items():
            for var in variables:
                # Check if the variable name is either camelCase or SCREAMING_SNAKE_CASE
                if not (CAMEL_CASE_PATTERN.match(var) or SCREAMING_SNAKE_CASE_PATTERN.match(var)):
                    self.fail(f"Variable '{var}' in file {file_path} does not follow camelCase or SCREAMING_SNAKE_CASE conventions.")

    def find_variables_in_src_folder(self, src_folder):
        all_variables = {}
        for root, _, files in os.walk(src_folder):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    variables = self.find_variables_in_file(file_path)
                    all_variables[file_path] = variables
        return all_variables

    def find_variables_in_file(self, file_path):
        variables = []
        with open(file_path, 'r') as f:
            lines = f.readlines()

        for line in lines:
            # Find all variable assignments
            found_vars = re.findall(VARIABLE_ASSIGNMENT_PATTERN, line)
            variables.extend(found_vars)

        return variables


if __name__ == '__main__':
    unittest.main()
