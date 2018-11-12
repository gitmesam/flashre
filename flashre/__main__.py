# Copyright (C) 2018 Guillaume Valadon <guillaume@valadon.net>

"""
The main glue
"""


import argparse

from flashre.demo import demo_register
from flashre.dump import dump_register
from flashre.emulate import emulate_register
from flashre.flags import flags_register
from flashre.hints import hints_register
from flashre.naming import naming_register
from flashre.telnet import telnet_register
from flashre.update import update_register
from flashre.xref import xref_register


if __name__ == "__main__":
    # Allow sub-parsers
    parser = argparse.ArgumentParser(description="Toshiba Flashair RE tools")
    subparser = parser.add_subparsers()

    # Register sub-commands
    demo_register(subparser)
    dump_register(subparser)
    emulate_register(subparser)
    flags_register(subparser)
    hints_register(subparser)
    naming_register(subparser)
    telnet_register(subparser)
    update_register(subparser)
    xref_register(subparser)
    args = parser.parse_args()

    # Call the sub-command
    args.func(args)
