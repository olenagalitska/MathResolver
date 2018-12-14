"""Main module of the project. Getting input from user and validating it."""


def who_is(expr):
    import re
    if re.match(
            r'([-+]?[0-9]*\.?[0-9]+)\s\*\sx\^2\s[+-]\s([-+]?[0-9]*\.?[0-9]+)\s\*\sx\s[+-]\s([-+]?[0-9]*\.?[0-9]+)\s=\s0',
            expr):
        return 'quadratic equation.', 'quadr_eq'
    elif re.match(
            r'\(\s+.+\s+\)\s+x\s+[+*/-]\s+\(\s+.+\s+\)\s+a\s+[><]=?\s+\(\s+.+\s+\)\s+:\s\[\s-?[0-9]*\s,\s-?[0-9]*\s\]',
            expr):
        return 'inequality with parameter.', 'param_ineq'
    elif re.match(r'\(\s+.+\s+\)\s+x\s+[><]=?\s+.+', expr):
        return 'inequality.', 'ineq'
    else:
        return 'expression with result.', 'expr'


def do_work():

    # get user input
    expression = input("Enter mathematical expression.\n"
                       "Put ' ' around every operation and operand.\n"
                       "You can use mathematical functions with ONE argument like 'sqrt ( 4 )'.\n"
                       "For simple ineq use '( expr ) x > expr' syntax.\n"
                       "For ineq with parameter: "
                       "( expr_x) x ( operation ) ( expr_a ) a >==< ( expr ) : [ min , max ].\n"
                       "For quadratic equations use syntax 'a * x^2 + b * x + c = 0',"
                       "where a, b, c are actual numbers.\n\n"
                       "To read from file enter 'FILE'.\n\n")

    print(expression)

    # if user wants to read expression from file
    if expression == 'FILE':
        file = open('input.txt', 'r')
        expression = file.read()
        file.close()

    # classify input expression
    description = who_is(expression)[0]
    type_id = who_is(expression)[1]
    print('Expression is', description)

    # import algorithms and solutions packages needed for input expression
    exec("import module_manager")
    exec("import algorithms." + type_id + " as algo_package")
    exec("import solutions." + type_id + " as solution_package")
    exec("solution = module_manager.find_solution(solution_package, expression)")
    exec("if solution is None: algo_package.solve(expression)")


if __name__ == "__main__":
    do_work()
