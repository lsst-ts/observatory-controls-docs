import sys

import lsst_sphinx_bootstrap_theme


# Work around Sphinx bug related to large and highly-nested source files
sys.setrecursionlimit(2000)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "documenteer.sphinxext",
    "sphinx-prompt",
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Rubin Observatory Controls Documentation"
copyright = "2020 Association of Universities for Research in Astronomy (AURA), Inc."
author = "Rubin Observatory"

version = "Current"
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    "_build",
    "README.rst",
    ".venv",
    "venv",
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# The reST default role cross-links Python (used for this markup: `text`)
default_role = "py:obj"

# Intersphinx
intersphinx_mapping = {
    "obs-ops": ("https://obs-ops.lsst.io", None)
    # 'python': ('https://docs.python.org/3/', None),
}

# Add substitions or link targets that you want on every page.
rst_epilog = """

"""

# -- Options for linkcheck builder ----------------------------------------

linkcheck_retries = 2
linkcheck_timeout = 5  # seconds
linkcheck_ignore = [
    r"^http://localhost",
    r"^https://jira.lsstcorp.org/browse/DM-24808",
    r"^https://ts-atcamera.lsst.io",
    r"^https://ts-athexapod.lsst.io",
    r"^https://ts-atmcs.lsst.io",
    r"^https://ts-atmonochromator",
    r"^https://ts-atpneumatics.lsst.io",
    r"^https://ts-atptg.lsst.io",
    r"^https://ts-atspectrograph.lsst.io",
    r"^https://ts-electrometer.lsst.io",
    r"^https://ts-standardscripts.lsst.io",
    r"^ls.st",  # TLS cert on ls.st is invalid and may cause issues
    r"http://love.tu.lsst.org",
    r"http://love01.cp.lsst.org/*",
    r"http://love1.tu.lsst.org",
    r"https://anaconda.org",
    r"https://chronograf-base-efd.lsst.codes",
    r"https://chronograf-summit-efd.lsst.codes",
    r"https://lsst-chronograf-int-efd.ncsa.illinois.edu",
    r"https://rancher.cp.lsst.org",
    r"https://rancher.ls.lsst.org",
    r"https://rancher.tu.lsst.org",
    r"https://summit-lsp.lsst.codes/*",
    r"https://tssw-ci.lsst.org/",
    r"https://tucson-teststand.lsst.codes/*",
    r"https://www.jenkins.io/doc/book/glossary/#agent",
    r"https://www.jenkins.io/doc/book/glossary/#controller",
    r"https://www.jenkins.io/doc/book/glossary/#pipeline",
    r"https://www.jenkins.io/doc/book/glossary/#project",
    r"http://ccs.lsst.org",
    r"https://foreman.cp.lsst.org",
    r"https://foreman.tu.lsst.org",
    r"https://foreman.ls.lsst.org",
]

# -- Options for HTML output ----------------------------------------------

templates_path = ["_templates", lsst_sphinx_bootstrap_theme.get_html_templates_path()]

html_theme = "lsst_sphinx_bootstrap_theme"
html_theme_path = [lsst_sphinx_bootstrap_theme.get_html_theme_path()]


html_context = {
    # Enable "Edit in GitHub" link
    "display_github": True,
    # https://{{ github_host|default("github.com") }}/{{ github_user }}/
    #     {{ github_repo }}/blob/
    #     {{ github_version }}{{ conf_py_path }}{{ pagename }}{{ suffix }}
    "github_user": "lsst-ts",
    "github_repo": "observatory-controls-docs",
    "conf_py_path": "",
    # TRAVIS_BRANCH is available in CI, but master is a safe default
    "github_version": "master" + "/",
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {"logotext": project}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = project

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False
