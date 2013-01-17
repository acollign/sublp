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
from os import path
from os import getcwd

PROJECT_FILECONTENT_TEMPLATE = '{"folders":[{"path": "%p"}]}\n'
PROJET_FILENAME_TEMPLATE = "{0}.sublime-project"

class BaseCommand(object):

	def __init__(self, name):
		self.args = None
		self.name = name

	def run(self, ctx):
		args = ctx["args"]
		progname = ctx["progname"]
		parser = argparse.ArgumentParser(prog="{0} {1}".format(progname, self.name))
		BaseCommand.add_common_args(parser)
		parser.add_argument("-p", "--project", type=str, help="the sublime text project file name")

		self.args = parser.parse_args(args)
		print self.args

	@classmethod
	def add_common_args(self, parser):
		parser.add_argument("-f", "--folder", type=str, help="the project folder")

class InitCommand(BaseCommand):

	def __init__(self):
		super(InitCommand, self).__init__("init")

	def run(self, ctx):

		super(InitCommand, self).run(ctx)

		projectRootPath = getcwd()

		if self.args.folder:
			projectRootPath = path.abspath(self.args.folder)

		projectFileName = None
		if self.args.project:
			projectName = self.args.project
			projectFileName = PROJET_FILENAME_TEMPLATE.format(self.args.project)
		else:
			projectName = path.basename(projectRootPath)
			projectFileName = PROJET_FILENAME_TEMPLATE.format(projectName)

		projectFile = None
		try:
			projectFile = open(projectFileName, "w")	
			content = PROJECT_FILECONTENT_TEMPLATE.replace("%p", projectRootPath)
			projectFile.write(content)

		except Exception, e:
			print "Failed to create the project due to {0}.".format(e)

		finally:
			if projectFile :
				projectFile.close()

			print "{0} project has been created.".format(projectName)

registry = {'init' : InitCommand()}