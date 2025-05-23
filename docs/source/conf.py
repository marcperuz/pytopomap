# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

from sphinx_gallery.sorting import FileNameSortKey

import plotly.io as pio
pio.renderers.default = 'sphinx_gallery'

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pytopomap'
copyright = '2025, Marc Peruzzetto'
author = 'Marc Peruzzetto'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

sys.path.insert(0, os.path.abspath('../../src/'))
print(sys.path)

extensions = [
    'autoapi.extension',
    'sphinx.ext.autodoc',
    'sphinx_gallery.gen_gallery',
    'sphinx.ext.napoleon', # for Google/NumPy style docstrings
]

autoapi_dirs = ['../../src']

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# sphinx-gallery configuration
sphinx_gallery_conf = {
    # path to your example scripts
    'examples_dirs': ['../../examples'],
    # path to where to save gallery generated output
    'gallery_dirs': ['auto_gallery'],
    # specify that examples should be ordered according to filename
    'within_subsection_order': FileNameSortKey,
}

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

