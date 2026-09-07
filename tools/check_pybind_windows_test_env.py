#!/usr/bin/env python3
import sys
import re
from pathlib import Path

def main():
    cmake_path = Path('src/python_pybind11/CMakeLists.txt')
    content = cmake_path.read_text()

    # Simple regex to see if we do `list(APPEND ... "PATH=...")`
    matches = re.findall(r'list\s*\(\s*APPEND\s+[^"]*"PATH=([^"]*)"\s*\)', content)
    if matches:
        print(f"Success: Found PATH modification in ENVIRONMENT properties for Windows: {matches}")
        sys.exit(0)

    print("Error: Did not find PATH modification in ENVIRONMENT properties for Windows")
    sys.exit(1)

if __name__ == '__main__':
    main()
