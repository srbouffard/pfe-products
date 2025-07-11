# docs/conf.py

# -- Project information -----------------------------------------------------
project = 'Platform Engineering Products'
copyright = '2025, PFE Team'
author = 'PFE Team'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx_rtd_theme',  # Adds the Read the Docs theme
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']