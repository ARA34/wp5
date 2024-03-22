"""
Contains all functionality for program to run,
including file handling.
"""
import sys
from pathlib import Path
import rpn_calculator


def main():
    """
    Main function with main functionality
    """
    # python3 wp5.py instructions.rpn result.txt
    inst_name = sys.argv[1]
    res_name = sys.argv[2]

    curr_path = Path(".").resolve()
    inst_path = curr_path / str(inst_name)
    encoding = "utf-8"
    with open(inst_path, "r", encoding=encoding) as file:
        contents = file.read()
    calculator_obj = rpn_calculator.RPN(u_in=contents)
    calculator_obj.rpn()  # result is set

    result_path = curr_path / str(res_name)
    if not result_path.exists():
        result_path.touch()
    with open(result_path, "w", encoding=encoding) as target_file:
        target_file.write(str(calculator_obj.res))


if __name__ == "__main__":
    main()
