import json, datetime, re, shutil

# Migrate from old custom static blog generator posts to Jekyll style posts

LINK_RE = re.compile(r'"([^"]+\.png)"')

def rewrite_links(content):
    images = LINK_RE.findall(content)

    # Copy images over to assets/ while we're at it
    for image in images:
        print("Copying", image, "to assets")
        shutil.copyfile("posts/" + image, "assets/" + image)

    return LINK_RE.sub(r'"{{ "/assets/\1" | absolute_url }}"', content)

for post in json.load(open("posts.json", "r")):
    date = datetime.datetime.fromtimestamp(post["authored"])
    date_fmt = date.strftime("%Y-%m-%d")
    filename = "%s-%s" % (date_fmt, post["filename"])
    # filename = post["filename"]

    print(filename)

    with open("posts/" + post["filename"], "r") as fp:
        with open("_posts/" + filename, "w") as newfp:
            newfp.writelines(["---\n"
                             ,"layout: post\n"
                             ,"title: \"" + post["title"] + "\"\n"
                             ,"date: " + date_fmt + "\n"
                             ,"---\n\n"])
            newfp.write(rewrite_links(fp.read()))
