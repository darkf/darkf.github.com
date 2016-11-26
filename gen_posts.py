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
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="../style.css"/>
</head>
<body>
<div id="content">
	<a href="http://darkf.github.io">&lt;</a> <span id="time">published %(authored)s %(lastmodified)s</span>
	<br/><br/>
	<h2>%(title)s</h2>
	<hr/>
	"""

POST = """
</div>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-40278551-2', 'auto');
  ga('send', 'pageview');
</script>
</body>
</html>"""

posts = json.load(open("posts.json", "r"))

for post in posts:
	date = datetime.date.fromtimestamp(post["authored"]).strftime(DATE_FORMAT)
	filename = post["filename"]
	print 'Generating "%s" (%s)' % (post["title"], date)

	with open(os.path.join("posts", filename), "r") as postsrc:
		with open(os.path.join("posts", splitext(filename)[0]+".html"), "w") as g:
			lastmodified = "last modified " + datetime.date.fromtimestamp(post["lastmodified"]).strftime(DATE_FORMAT) if "lastmodified" in post else ""
			pre = PRE % {"title": post["title"], "authored": date, "lastmodified": lastmodified}
			body = pre + markdown(postsrc.read().decode('utf-8')) + POST
			g.write(body.encode('utf-8'))