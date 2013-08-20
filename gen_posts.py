import sys, os, datetime, time, json
from os.path import splitext, basename
from markdown import markdown

if not os.path.exists("posts.json"):
	print "You need a `posts.json` file!"
	sys.exit(1)

DATE_FORMAT = "%B %d, %Y"
TODAY = datetime.date.fromtimestamp(int(time.time()))

PRE = """<!doctype html>
<html>
<head>
  <title>%(title)s</title>
  <link rel="stylesheet" type="text/css" href="../style.css"/>
</head>
<body>
<div id="content">
	<a href="http://darkf.github.io">&lt;</a> <span id="time">published %(authored)s</span>
	<br/><br/>
	<h2>%(title)s</h2>
	<hr/>
	"""

POST = """
</div>
</body>
</html>"""

posts = json.load(open("posts.json", "r"))

for post in posts:
	date = datetime.date.fromtimestamp(post["authored"]).strftime(DATE_FORMAT)
	filename = post["filename"]
	print 'Generating "%s" (%s)' % (post["title"], date)

	with open(os.path.join("posts", filename), "r") as postsrc:
		with open(os.path.join("posts", splitext(filename)[0]+".html"), "w") as g:
			pre = PRE % {"title": post["title"], "authored": date}
			g.write(pre+markdown(postsrc.read())+POST)