import os
import sys
sys.path.insert(0, os.path.abspath('../../../../opencb-testing'))
print(sys.path)

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'opencb-docs'
copyright = '2024, octakitten'
author = 'octakitten'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'autoapi.extension'
]

autoapi_dirs = ['../../../../opencb-testing/opencb']

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = ['_build', '_templates']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
