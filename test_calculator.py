"""
Testing functions of the rpn_calculator module.
"""
import rpn_calculator as rpn


def test_1():
    """
    Testing one variation
    """
    n1 = rpn.RPN(u_in="2 3 5 + *")
    n1.rpn()
    assert n1.res == 16


def test_2():
    """
    Testing another variation
    """
    n2 = rpn.RPN(u_in="2 2 4 2 + + *")
    n2.rpn()
    assert n2.res == 16


def test_stack_attributes():
    """
    Testing that stack attributes are set
    """
    n3 = rpn.RPN(u_in="2 3 5 + *")
    n3.in_to_stack(n3.u_in)
    assert n3.num_stack and n3.op_stack is not None
