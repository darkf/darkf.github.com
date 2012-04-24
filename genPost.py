import sys, os
from os.path import splitext, basename
from markdown import markdown

if len(sys.argv) != 3:
	print "usage: %s FILE TITLE" % sys.argv[0]

FILE = sys.argv[1]
TITLE = sys.argv[2]

PRE = """<!doctype html>
<html>
<head>
  <title>%s</title>
  <link rel="stylesheet" type="text/css" href="../style.css"/>
</head>
<body>
<div id="content">
	<h2>%s</h2>
	<hr/>
	""" % (TITLE, TITLE)

POST = """
</div>
</body>
</html>"""

with open(FILE, "r") as f:
	with open(os.path.join("posts", splitext(basename(FILE))[0]+".html"), "w") as g:
		g.write(PRE+markdown(f.read())+POST)