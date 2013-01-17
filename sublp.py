#!/usr/bin/env python

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import commands

PROGNAME = "sublp"

# args handling (command and common args)
parser = argparse.ArgumentParser()
commands.BaseCommand.add_common_args(parser)
parser.add_argument("command", choices=commands.registry.keys(), nargs=argparse.REMAINDER, help="the command to run")

args = parser.parse_args()

command_name = args.command[0]
command_args = args.command[1:]

ctx = {"args":command_args, "progname":PROGNAME}

commands.registry[command_name].run(ctx)