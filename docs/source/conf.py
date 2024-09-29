import os
import sys
import django


sys.path.insert(0, os.path.abspath("../../"))
os.environ["DJANGO_SETTINGS_MODULE"] = "starter.settings"
django.setup()

project = 'Starter '
copyright = "2024"
author = "Godfrey Ndung'u"
release = '0.1.0'

extensions = ["sphinx.ext.autodoc",
              "sphinx.ext.todo",
              "sphinx.ext.coverage",
              "sphinx.ext.viewcode",
              "sphinx.ext.napoleon",
              "sphinx.ext.inheritance_diagram",
              ]

templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"

html_builder = ["sphinx", "-b", "html",
                "-d", "docs/source", "-D", "language=en"]

coverage_show_missing_items = True

html_css_files = [
    'css/style.css',
]
