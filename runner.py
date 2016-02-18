import argparse
from src.otter import Otter


def parse_suites(args):
    suites = []
    for arg in args['suites']:
        splitarg = arg.split('.')
        suites.append({
            "module": "{}.{}".format(splitarg[0], splitarg[1]),
            "class": splitarg[2]
        })
    return suites

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Otter is a basic unit test\
                                  framework.")
    parser.add_argument(
        'suites',
        metavar='TestSuite',
        type=str,
        nargs='+'
    )
    parser.add_argument(
        '--format',
        help="Default: table; Decides whether to use table or csv for output.",
        required=False
    )
    args = vars(parser.parse_args())
    otter = Otter(parse_suites(args))
    otter.run()
