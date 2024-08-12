"""This script is used to build the documentation.

Build multi-language documentation site.

Note:
    File   : build.py
    Author : Baiqi.Lu <ittuann@outlook.com>
    License: MIT License.

Example:
    $ python ./scripts/build.py
"""

import re
import shutil
import subprocess
from pathlib import Path

from config import cfg


def build_docs() -> None:
    """Build Multi-Language Documentation."""
    if cfg.SITE_PATH.exists():
        print(f"Removing existing site dir: {cfg.SITE_PATH}")
        shutil.rmtree(cfg.SITE_PATH)

    # Build the main documentation
    file = cfg.DOCS_PATH / "mkdocs.yml"
    print(f"Building the main documentation, with configuration file: {file}")
    subprocess.run(["mkdocs", "build", "-f", str(file)], check=True)
    print(f"Main site successfully built at: {cfg.SITE_PATH}")

    # Build other localized documentations
    for file in cfg.DOCS_PATH.glob("mkdocs.*.yml"):
        language_code = file.stem.split(".")[1]
        print(f"Building the {language_code} site with configuration file: {file}")
        subprocess.run(["mkdocs", "build", "-f", str(file)], check=True)
    print(f"Sub site successfully built at: {cfg.SITE_PATH}")


def update_404page_title(file_path: Path = cfg.SITE_PATH / "404.html") -> None:
    """Update the title of the 404 page."""
    new_title = "Awesome Intelligent Car Race - 404 Page Not Found"

    if not file_path.exists():
        raise FileNotFoundError(f"The specified 404.html {file_path} does not exist.")

    with open(file_path, encoding="utf-8") as file:
        content = file.read()

    if new_title in content:
        print("The title of the 404 page is already up-to-date.")

    # Replace the existing title with the new title
    updated_content = re.sub(r"<title>.*?</title>", f"<title>{new_title}</title>", content)

    # Write the updated content back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(updated_content)
    print("Successfully updated the title of the 404 page")


if __name__ == "__main__":
    build_docs()
    update_404page_title()

    print(
        """
        Serve multi-language site at http://localhost:8000 with:
            python -m http.server --directory site 8000 --bind localhost
        """
    )
