import subprocess, sys
from src import generate_categories, generate_rss


def run_mkdocs(port):
    command = ["mkdocs", "serve", "-f", "src/mkdocs.yml", "-a", f"0.0.0.0:{port}"]
    subprocess.run(command)


if __name__ == "__main__":
    generate_rss.generate_rss()
    if len(sys.argv) != 2:
        port = 8000
    else:
        port = sys.argv[1]
    run_mkdocs(port)
