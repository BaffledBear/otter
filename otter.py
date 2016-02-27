#!/usr/bin/python3
from argparse import RawTextHelpFormatter
from src.otter import Otter
import argparse
import sys


def parse_units(args):
    unittests = []
    for arg in args:
        splitarg = arg.split('.')
        unittests.append({
            "module": "{}.{}".format(splitarg[0], splitarg[1]),
            "class": splitarg[2]
        })
    return unittests


def get_output(type, otter):
    if type == "csv":
        return otter.get_csv_output()
    else:
        return otter.get_table()


if __name__ == "__main__":
    req_ver = (3, 4)
    cur_ver = sys.version_info
    if cur_ver >= req_ver:
        parser_desc = "Otter is a basic unit test framework for Python 3.4+."
        parser = argparse.ArgumentParser(description=parser_desc,
                                         formatter_class=RawTextHelpFormatter)
        ex_group = parser.add_mutually_exclusive_group(required=True)
        ex_group.add_argument(
            '-l',
            dest='unittests',
            metavar='UnitTest',
            help="Enter a list of Python classes in import format.\n\
            (e.g. test.assert_test.AssertTest)\n\n",
            action='store',
            type=str,
            nargs='+',
            default=None
        )
        ex_group.add_argument(
            '-i',
            dest='infile',
            metavar='Input File',
            help="Default: None; file containing a list of tests to run\n\
            separted by row.\n\n"
        )
        ex_group.add_argument(
            '-w',
            dest='use_gui',
            action='store_true',
            help="Launch a webservice that can be reached via a browser."
        )
        parser.add_argument(
            '-f',
            dest='format',
            metavar='Format',
            help="Default: table; Decides whether to use table or csv for\n\
            output.\n\n",
            required=False
        )
        parser.add_argument(
            '-o',
            dest='outfile',
            metavar='Filename',
            help="Default: print to screen; location of file to write results",
            required=False
        )
        args = vars(parser.parse_args())
        if args['use_gui'] is True:
            import web_gui
            web_gui.start_service()
            pass
        elif not args['infile'] is None:
            unittests = []
            try:
                file = open(args["infile"], 'r')
                for line in file:
                    unittests.append(line)
            except Exception as e:
                    print("Unable to open input file.", e)
            else:
                file.close()
        elif not args['unittests'] is None:
            unittests = args["unittests"]
        else:
            parser.parse_args(['-h'])

        otter = Otter(parse_units(unittests))
        otter.run()

        output = get_output(args["format"], otter)
        if not args["outfile"] is None:
            try:
                file = open(args["outfile"], 'w')
                file.write(output)
            except Exception as e:
                print("Unable to create file at given locaiton. ", e)
            else:
                file.close()
        else:
            print(output)

    else:
        print("Your Python interpreter is too old. Version {}.{} is required.\
              Please consider upgrading.".format(req_ver[0], req_ver[1]))
