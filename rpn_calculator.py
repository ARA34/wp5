"""
Contains classes and functionality for calultor.
"""


class RPN():
    """
    Class to handle calculator objects
    """
    def __init__(self, u_in=None):
        self.u_in = u_in
        self.num_stack = None
        self.op_stack = None
        self.valid_ops = ["+", "*", "-", "/"]
        self.res = None

    def compute(self, a, b, c):
        """
        Handles the raw algebreic computation functions
        """
        # a,b ints
        # c operator
        if c == "+":
            return a + b
        elif c == "-":
            return a - b
        elif c == "*":
            return a * b
        elif c == "/":
            try:
                return a/b
            except ZeroDivisionError:
                print("cant divide by zero")

    def rpn(self) -> None:
        """
        Calculates result and sets it as res attribute
        """
        total = 0
        self.in_to_stack(self.u_in)
        num_stack = self.num_stack
        op_stack = self.op_stack
        num_stack = [eval(i) for i in num_stack]

        # ensures the operators are at the bottom
        try:
            total = 0
            num_stack.reverse()
            op_stack.insert(0, "+")
            for s in range(len(num_stack)):
                total = self.compute(total,
                                     num_stack[s],
                                     op_stack[s])
            self.res = total

        except Exception as ex:
            print(f"Error: {ex}")

    def in_to_stack(self, u_in: str) -> None:
        """
        Converts a raw string into number stack and operator stack
        and sets both to class attributes
        """
        split_in = u_in.split()
        operators = list(filter(lambda n: n in self.valid_ops,
                                split_in))
        numbers = list(filter(lambda n: n not in operators,
                              split_in))
        self.num_stack = numbers
        self.op_stack = operators
