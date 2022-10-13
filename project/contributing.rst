##################################################
Contributing to Observatory Controls Documentation
##################################################

Below are instructions and guidelines on contributing to the `Rubin Observatory Controls Documentation <https://obs-controls.lsst.io>`__.
This documentation is built with `Sphinx <https://www.sphinx-doc.org/en/master/>`__ and published to `<https://obs-controls.lsst.io>`__.

This documentation is open source.
Rubin welcomes contributions that make this documentation more useful and accurate.

Keep in mind that everyone participating in this project is expected respectful to others. 
The `Team Culture and Conduct Standards <https://developer.lsst.io/team/code-of-conduct.html>`__ provides an example of what is expected when participating to Rubin documentation.

.. _Contributing-Issue:

Raising an issue
================

If you spot an issue with the documentation, the best thing to do is `raise a GitHub issue in the observatory-controls-docs repo <https://github.com/lsst-ts/observatory-controls-docs/issues/new>`__.
Include any relevant URLs with your issue description.


.. _Contributing-PR:

Creating a Pull Request
=======================

You can contribute directly to the `Rubin Observatory Controls Documentation <https://obs-controls.lsst.io>`__ repo by creating a pull request.
If you are intending to make a substantial change, it is a good idea to create a GitHub issue first with your proposal.
LSST cannot accept contributions that are not aligned with our strategy and roadmap.

These sections can help you create a successful pull request:

  * :ref:`Contributing-Building-the-Docs`
  * :ref:`Contributing-Doc-Style-Guide`

.. _Contributing-Building-the-Docs:

Building the Documentation Locally
==================================

These are the basic steps to clone and build the docs:

#. Clone the GitHub repository:

   .. code-block:: bash

      git clone https://github.com/lsst-ts/observatory-controls-docs
      cd observatory-controls-docs

#. Create a Python virtual environment (with `venv <https://docs.python.org/3/tutorial/venv.html>`__, for example):

   .. code-block:: bash

      python3 -m venv .venv
      source .venv/bin/activate

   .. note::
      Activate this virtual environment in another shell by re-running the ``source`` command.

#. Install the Python dependencies:

   .. code-block:: bash

      python -m pip install --upgrade pip
      python -m pip install -r requirements.txt

#. You are now able to edit the cloned repository.
   The remaining items below are commands used to build and validate the documentation. These commands must be executed from the top-level directory.

#. Build the site:

   .. code-block:: bash

      make html

   .. note::
      Open ``_build/html/index.html`` in a browser to review it.

#. Validate the documentation build:

   .. code-block:: bash

      make linkcheck

   .. note::
      If some links are behind a login, you might need to ignore them.
      Look at the ``linkcheck_ignore`` variable in ``conf.py`` for examples of how to do this.

#. Completely clear the build:

   .. code-block:: bash

      make clean


.. _Contributing-Deployment:

Deployment
==========

Whenever you push to the GitHub repository, the site is built for the corresponding branch.
Find your build at https://obs-controls.lsst.io/v/. 
You can push to a branch you've created at any time.

The ``main`` branch is always published as https://obs-controls.lsst.io. 
Only authorized individuals can merge to ``main`` (may be delegated).
To incorporate your suggestions, create a :ref:`pull request <contributing-pr>`.

Approval Process
----------------

#. Verify the content with all authors and contributors.

#. Create a PR.

#. Request the following to review the PR:

   * Patrick Ingraham
   * Any applicable Product Owner

#. Respond to the comments received during the review process.

#. After all reviewers approve, the submitter will squash commits and merge to main.

.. _Contributing-Doc-Style-Guide:

Documentation Style Guide
=========================

.. _Contributing-New-to-reST:

New to reStrcturedText and Sphinx
---------------------------------

Check out these resources and guides. Sources files are available to compare raw reST and HTML outputs.

  * `reStructuredText Introductory and Tutorial Material <https://docutils.sourceforge.io/rst.html>`__ and references therein.

  * `reStructuredText Primer <https://docutils.sourceforge.io/docs/user/rst/quickstart.html>`__

  * `reStructuredText Quick Reference <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`__

  * `reStructuredText Primer from Sphinx <https://www.sphinx-doc.org/en/1.8/usage/restructuredtext/basics.html>`_

  * `reStructuredText Style Guide for Rubin Observatory Data Management Developers <https://developer.lsst.io/restructuredtext/style.html>`__

