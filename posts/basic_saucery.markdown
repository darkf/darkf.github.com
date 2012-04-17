Today I decided to finally bootstrap a simple, statically generated blog on top of my [Github Pages](http://pages.github.com/) site.


Now, why don't I just use an existing package, such as [Jekyll](http://jekyllrb.com/)? Simple, it's still too complicated for my needs -- a basic, working blog.

That's why I decided to get stuff done and write a simple Python script using the [Python markdown library](http://freewisdom.org/projects/python-markdown/).
The code is self-explanatory, so I'll just post the code listing, which you can also find [here](../genPost.py):


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
    <h2>%s</h2>
    <hr/>
    """ % (TITLE, TITLE)
    
    POST = """
    </body>
    </html>"""
    
    with open(FILE, "r") as f:
    	with open(os.path.join("posts", splitext(basename(FILE))[0]+".html"), "w") as g:
    		g.write(PRE+markdown(f.read())+POST)


(Now all I need to do is write my own hacky Markdown parser and ditch this shoddy one.)