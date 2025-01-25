import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# Project information
project = 'Content Goblin'
author = 'Your Name or Team'
release = '1.0'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# HTML output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
