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

from sys import argv
from os import path
from os import getcwd

PROJECT_FILECONTENT_TEMPLATE = '{"folders":[{"path": "%p"}]}\n'
PROJET_FILENAME_TEMPLATE = "{0}.sublime-project"

projectRootPath = getcwd()

if len(argv) > 1:
	projectRootPath = path.abspath(argv[1])

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
