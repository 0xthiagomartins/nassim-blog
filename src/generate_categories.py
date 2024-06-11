import os
import yaml
from collections import defaultdict

POSTS_DIR = "posts"
CATEGORIES_DIR = "categories"
ROOT_DIR = "src/docs"


# Function to read YAML front matter from a markdown file
def read_front_matter(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        if f.readline().strip() != "---":
            return {}
        lines = []
        for line in f:
            if line.strip() == "---":
                break
            lines.append(line.strip())
        return yaml.safe_load("\n".join(lines))


# Create categories directory if not exists
os.makedirs(os.path.join(ROOT_DIR, CATEGORIES_DIR), exist_ok=True)

# Dictionary to store posts by category
categories = defaultdict(list)

# Scan posts and collect categories
for root, _, files in os.walk(os.path.join(ROOT_DIR, POSTS_DIR)):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            front_matter = read_front_matter(file_path)
            if "categories" in front_matter:
                for category in front_matter["categories"]:
                    categories[category].append(file_path.replace(POSTS_DIR + "/", ""))

# Generate index.md for each category
for category, posts in categories.items():
    category_dir = os.path.join(ROOT_DIR, CATEGORIES_DIR, category)
    os.makedirs(category_dir, exist_ok=True)
    with open(os.path.join(category_dir, "index.md"), "w", encoding="utf-8") as f:
        f.write(f"# {category}\n\n")
        f.write("{{ rss_feed(category=" + f'"{category}"' + ") }}")
