#!/usr/bin/python3
from argparse import RawTextHelpFormatter
from src.otter import Otter
import argparse
import sys


def parse_units(args):
    unittests = []
    print(args)
    for arg in args['unittests']:
        print(arg)
        splitarg = arg.split('.')
        unittests.append({
            "module": "{}.{}".format(splitarg[0], splitarg[1]),
            "class": splitarg[2]
        })
    return unittests

if __name__ == "__main__":
    req_ver = (3, 4)
    cur_ver = sys.version_info
    if cur_ver >= req_ver:
        parser_desc = "Otter is a basic unit test framework for Python 3.4+."
        parser = argparse.ArgumentParser(description=parser_desc,
                                         formatter_class=RawTextHelpFormatter)
        parser.add_argument(
            '-c',
            dest='unittests',
            metavar='UnitTest',
            help="Enter a list of Python classes in import format.\n\
            (e.g. test.assert_test.AssertTest)",
            action='store',
            type=str,
            nargs='+',
            default=None
        )
        parser.add_argument(
            '-f',
            metavar='Format',
            help="Default: table; Decides whether to use table or csv for\n\
            output.",
            required=False
        )
        parser.add_argument(
            '-w',
            '--webui',
            dest='use_gui',
            action='store_true',
            help="Launch a webservice that can be reached via a browser.",
            default=False
        )
        args = vars(parser.parse_args())
        if args['use_gui'] is True:
            import web_gui
            web_gui.start_service()
            pass
        elif not args['unittests'] is None:
            otter = Otter(parse_units(args))
            otter.run()
            otter.print_results()
        else:
            parser.parse_args(['-h'])

    else:
        print("Your Python interpreter is too old. Version {}.{} is required.\
              Please consider upgrading.".format(req_ver[0], req_ver[1]))
