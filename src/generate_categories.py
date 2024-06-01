import os
import yaml
from collections import defaultdict

# Path to the posts directory
POSTS_DIR = "src"

# Path to the categories directory
CATEGORIES_DIR = "src/categories"


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
os.makedirs(CATEGORIES_DIR, exist_ok=True)

# Dictionary to store posts by category
categories = defaultdict(list)

# Scan posts and collect categories
for root, _, files in os.walk(POSTS_DIR):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            front_matter = read_front_matter(file_path)
            if "categories" in front_matter:
                for category in front_matter["categories"]:
                    categories[category].append(file_path.replace(POSTS_DIR + "/", ""))

# Generate index.md for each category
for category, posts in categories.items():
    category_dir = os.path.join(CATEGORIES_DIR, category)
    os.makedirs(category_dir, exist_ok=True)
    with open(os.path.join(category_dir, "index.md"), "w", encoding="utf-8") as f:
        f.write(f"# {category}\n\n")
        for post in posts:
            f.write(f"- [{post.split('/')[-1].replace('.md', '')}]({post})\n")
