# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# for local generation, refer to Taichi source repo
taichi_path = os.getenv('TAICHI_PATH', '.')
# sys.path.insert(0, os.path.abspath(taichi_path))

# -- Project information -----------------------------------------------------

project = 'taichi-api-docstring'
copyright = '2021, Taichi Graphics'
author = 'Taichi Graphics'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'autoapi.extension',
]

# Auto API setup
autoapi_type = 'python'
autoapi_dirs = [taichi_path, 'src']
autoapi_options = [
   'members',
   'undoc-members',
#  'private-members',
   'show-inheritance',
   'show-module-summary',
#  'special-members',
   'imported-members'
]

# filter out unncessary modules
autoapi_ignore = [
    '*examples*',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'bizstyle'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

master_doc = 'index'

html_sidebars = {
   '**': [
      'versions.html'
   ]
}

try:
   html_context
except NameError:
   html_context = dict()
html_context['display_lower_left'] = True

# SET CURRENT_VERSION
from git import Repo
repo = Repo(os.path.join(taichi_path, '../..'))

if 'current_version' in os.environ:
   # get the current_version env var set by buildDocs.sh
   current_version = os.environ['current_version']
else:
   # set this build's current version by looking at the branch
   current_version = repo.active_branch.name

# tell the theme which version we're currently on ('current_version' affects
# the lower-left rtd menu and 'version' affects the logo-area version)
html_context['current_version'] = current_version
html_context['version'] = current_version

# POPULATE LINKS TO OTHER VERSIONS
html_context['versions'] = list()

versions = [branch.name for branch in repo.tags]
versions = versions[len(versions)-1:]

html_context['versions'].append( ('master', '/') )
for version in versions:
   html_context['versions'].append( (version, '/' +version+ '/') )
