import os
import markdown
import yaml
from feedgen.feed import FeedGenerator
from datetime import datetime

docs_folder = "src/docs"
blog_domain = "blog.nassim.com.br"


def extract_metadata(content):
    metadata = {}
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            front_matter = content[3:end].strip()
            metadata = yaml.safe_load(front_matter)
            content = content[end + 3 :].strip()
    return metadata, content


def extract_excerpt(content):
    if "<!-- more -->" in content:
        excerpt = content.split("<!-- more -->")[0]
    else:
        excerpt = content[:150]
    # Remove markdown headers from excerpt
    excerpt_lines = excerpt.split("\n")
    clean_excerpt = []
    for line in excerpt_lines:
        if not line.startswith("#"):
            clean_excerpt.append(line)
    return markdown.markdown("\n".join(clean_excerpt))


def generate_rss():
    fg = FeedGenerator()
    fg.title("Nassim - Blog")
    fg.link(href=f"https://{blog_domain}")
    fg.description("Blog Description")
    fg.language("en")

    posts_dir = os.path.join(docs_folder, "posts")

    for filename in os.listdir(posts_dir):
        if filename.endswith(".md"):
            filepath = os.path.join(posts_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                metadata, post_content = extract_metadata(content)
                html_content = markdown.markdown(post_content)

                title = metadata.get("title", "No Title")
                description = metadata.get("description", extract_excerpt(post_content))
                pub_date = metadata.get("date", datetime.now())
                categories = metadata.get("categories", [])

                fe = fg.add_entry()
                fe.title(title)
                fe.link(
                    href=f'https://{blog_domain}/posts/{filename.replace(".md", "")}'
                )
                fe.description(description)
                fe.pubDate(pub_date.strftime("%a, %d %b %Y %H:%M:%S +0000"))
                for category in categories:
                    fe.category(term=category)

    fg.rss_file(os.path.join(docs_folder, "rss.xml"))


if __name__ == "__main__":
    generate_rss()
