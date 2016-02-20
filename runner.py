import argparse
from src.otter import Otter


def parse_units(args):
    unittests = []
    for arg in args['unittests']:
        splitarg = arg.split('.')
        unittests.append({
            "module": "{}.{}".format(splitarg[0], splitarg[1]),
            "class": splitarg[2]
        })
    return unittests

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Otter is a basic unit test\
                                  framework.")
    parser.add_argument(
        'unittests',
        metavar='UnitTest',
        type=str,
        nargs='?'
    )
    parser.add_argument(
        '--format',
        help="Default: table; Decides whether to use table or csv for output.",
        required=False
    )
    args = vars(parser.parse_args())
    if args['unittests'] is None:
        import web_gui
        web_gui.start_service()
    else:
        otter = Otter(parse_units(args))
        otter.run()
