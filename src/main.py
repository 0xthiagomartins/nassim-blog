from datetime import datetime
import os
import yaml
from collections import defaultdict
import toml
import xml.etree.ElementTree as ET

docs_folder = "src/docs"


def load_authors():
    with open("src/authors.toml", "r") as file:
        authors_data = toml.load(file)
    return authors_data


class Footer:
    def __init__(self):
        self.content = "<div class='footer'>\n"

    def render_contacts(self, author):
        if "contacts" in author:
            contacts = author["contacts"]
            self.content += "  <p><strong>Contacts:</strong></p>\n"
            self.content += "  <ul>\n"
            for key, value in contacts.items():
                icon = ""
                link = value
                # TODO please thiago, update to payments have icons
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
                    case "x" | "twitter" | "X":
                        icon = "fab fa-twitter"
                        link = f"https://x.com/{value}"
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
                self.content += f"    <li><i class='{icon}'></i> <a href='{link}' target='_blank'>{key.capitalize()}: {value}</a></li>\n"
            self.content += "  </ul>\n"

    def render_donations(self, author):
        if "donations" in author:
            donations = author["donations"]
            self.content += "  <p><strong>Donations:</strong></p>\n"
            self.content += "  <ul>\n"
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

                self.content += f"    <li>{key.capitalize()}: {value}</li>\n"
            self.content += "  </ul>\n"


def define_env(env):
    authors = load_authors()

    @env.macro
    def footer(metadata):
        footer = Footer()

        if "authors" in metadata:
            footer.content += "<p><strong>Authors:</strong></p>\n<ul>\n"
            for author_id in metadata["authors"]:
                author = authors.get(author_id, {})
                footer.content += f"<li>{author.get('name', 'Unknown Author')}\n"
                footer.content += (
                    f"    <p>{author.get('description', 'No description')}</p>\n"
                )
                footer.content += f"    <img src='{author.get('avatar', '')}' alt='Avatar' style='width:50px; height:50px;'>\n"
                footer.content += "</li>\n"
                footer.content += "</ul>\n"
                footer.render_contacts(author)
                footer.render_donations(author)

            footer.content += f"  <p><strong>Date:</strong> {metadata['date']}</p>\n"
            footer.content += "</div>\n"

        return footer.content

    @env.macro
    def rss_feed():
        rss_path = os.path.join(docs_folder, "rss.xml")
        with open(rss_path, "r", encoding="utf-8") as f:
            rss_content = f.read()
            root = ET.fromstring(rss_content)
            items = root.findall(".//item")

            feed_html = "<h2>Blog RSS Feed</h2><ul>"
            for item in items:
                title = item.find("title").text
                link = item.find("link").text
                description = item.find("description").text
                pub_date = item.find("pubDate").text
                pub_date_parsed = datetime.strptime(
                    pub_date, "%a, %d %b %Y %H:%M:%S +0000"
                )
                pub_date_formatted = pub_date_parsed.strftime("%a, %d %b %Y")

                feed_html += f'<li><a href="{link}">{title}</a><br><small>{pub_date_formatted}</small><p>{description}</p></li>'
            feed_html += "</ul>"

            return feed_html
