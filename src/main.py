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


def define_env(env):
    @env.macro
    def footer(metadata):
        footer_content = f"<div class='footer'>\n"
        footer_content += f"  <p><strong>Author:</strong> {metadata['author']}</p>\n"

        if "contacts" in metadata:
            contacts = metadata["contacts"]
            footer_content += "  <p><strong>Contacts:</strong></p>\n"
            footer_content += "  <ul>\n"
            for key, value in contacts.items():
                icon = ""
                link = value
                match key:
                    case "email":
                        icon = "fas fa-envelope"
                        link = f"mailto:{value}"
                    case "github":
                        icon = "fab fa-github"
                        link = f"https://github.com/{value}"
                    case "linkedin":
                        icon = "fab fa-linkedin"
                        link = f"https://linkedin.com/in/{value}"
                    case "telegram":
                        icon = "fab fa-telegram"
                        link = f"https://t.me/{value}"
                    case "twitter":
                        icon = "fab fa-twitter"
                        link = f"https://twitter.com/{value}"
                    case "instagram":
                        icon = "fab fa-instagram"
                        link = f"https://instagram.com/{value}"
                    case "youtube":
                        icon = "fab fa-youtube"
                        link = f"https://youtube.com/{value}"
                    case "medium":
                        icon = "fab fa-medium"
                        link = f"https://medium.com/@{value}"
                    case "whatsapp":
                        icon = "fab fa-whatsapp"
                        link = f"https://wa.me/{value}"

                footer_content += f"    <li><i class='{icon}'></i> <a href='{link}' target='_blank'>{key.capitalize()}: {value}</a></li>\n"
            footer_content += "  </ul>\n"

        if "donations" in metadata:
            donations = metadata["donations"]
            footer_content += "  <p><strong>Donations:</strong></p>\n"
            footer_content += "  <ul>\n"
            for key, value in donations.items():
                match key:
                    case "bitcoin":
                        link = f"bitcoin:{value}"
                    case "ethereum":
                        link = f"ethereum:{value}"
                    case "solana":
                        link = f"solana:{value}"
                    case "taraxa":
                        link = f"taraxa:{value}"
                    case "nano":
                        link = f"nano:{value}"

                footer_content += f"    <li>{key.capitalize()}: {value}</li>\n"
            footer_content += "  </ul>\n"

        footer_content += f"  <p><strong>Date:</strong> {metadata['date']}</p>\n"
        footer_content += "</div>\n"

        return footer_content
