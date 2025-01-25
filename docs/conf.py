import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'Content Goblin'
author = 'Your Name or Team'
release = '1.0'

# General configuration
extensions = []
templates_path = ['_templates']
exclude_patterns = []

# HTML output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
