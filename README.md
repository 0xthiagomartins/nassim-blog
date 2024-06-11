# Dev Setup

1. Create Virtual Environment: (Only one time)

   virtualenv venv

2. Start Virtualenv (Linux or MAC):

    source ./venv/bin/activate

3. Install mkdocs: (Only one time)

    pip install -r requirements.txt

4. Run server:

    python3 run.py

# Metadata for Blog Posts

Each blog post should include the following metadata at the top of the markdown file:

- `title`: The title of the blog post. Example: `title: "My First Blog Post"`
- `date`: The publication date of the blog post in `YYYY-MM-DD` format. Example: `date: 2024-06-01`
- `description`: A brief description or excerpt of the blog post. Example: `description: "This is a summary of my first blog post"`

You can use the `<!-- more -->` tag to mark the excerpt of your post. The content before this tag will be used as the description in the RSS feed.

Example of metadata in a markdown file:

```markdown
---
title: "My First Blog Post"
date: 2024-06-01
description: "This is a summary of my first blog post"
---

# My First Blog Post

This is the content of my first blog post.
<!-- more -->
This part of the content will not be included in the RSS feed description.