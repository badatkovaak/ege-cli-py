import click as c
import src.tree_node as tn
import src.tree_solver as ts


@c.group(no_args_is_help=True)
def cli():
    pass


@cli.command()
@c.option('-d', '--depth')
def printTree(depth: int):
    c.echo(f"tree's depth is {depth}")


level_of_verbosity = {
    'f': 'full',
    'r': 'readable',
    'n': 'none'
}


@cli.command()
@c.option('-r', '--max_range', type=c.INT)
@c.option('-op', '--operations', prompt='Enter possible operations (separated by commas)')
@c.option('-v', '--verbose', type=c.Choice(level_of_verbosity.keys(), case_sensitive=False), required=0)
@c.option('-sv', '--start_values', type=c.INT, required=0)
@c.argument('max_val', default=0)
def solve_21(max_val: int, max_range: int, verbose: str, operations: str, start_values: int):
    mrange = max_range if max_range is not None else max_val
    values: list[int] = [start_values] if start_values is not None else []
    oper = operations.replace(' ', '').split(',')

    solutions: list[int] = []
    for i in range(1, mrange+1):
        values.append(i)
        tree = tn.constructTree(values, oper, 5)
        if ts.TreeSolver.solveTree(tree, max_val, ts.Mode.DnM):
            solutions.append(i)
        if verbose == 'r':
            print(tree)
        elif verbose == 'f':
            print(tree.__repr__(0, True))
        values.pop()
    c.echo(solutions)


@cli.command()
@c.option('-r', '--max_range', type=c.INT)
@c.option('-op', '--operations', prompt='Enter possible operations (separated by commas)')
@c.option('-v', '--verbose', type=c.Choice(level_of_verbosity.keys(), case_sensitive=False), required=0)
@c.option('-sv', '--start_values', type=c.INT, required=0)
@c.argument('max_val', default=0)
def solve_20(max_val: int, max_range: int, verbose: str, operations: str, start_values: int):
    mrange = max_range if max_range is not None else max_val
    values: list[int] = [start_values] if start_values is not None else []
    oper = operations.replace(' ', '').split(',')

    solutions: list[int] = []
    for i in range(1, mrange+1):
        values.append(i)
        tree = tn.constructTree(values, oper, 4)
        if ts.TreeSolver.solveTree(tree, max_val, ts.Mode.D):
            solutions.append(i)
        if verbose == 'r':
            print(tree)
        elif verbose == 'f':
            print(tree.__repr__(0, True))
        values.pop()
    c.echo(solutions)


if __name__ == '__main__':
    cli()
