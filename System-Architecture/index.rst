.. This is a template top-level index file for a directory in the procedure's arm of the documentation

.. This is the label that can be used as for cross referencing in the given area
.. Recommended format is "Directory Name"-"Title Name"  -- Spaces should be replaced by hypens
.. _Control-System-Architecture:

############################
Control System Architecture
############################

.. note::
    This is a template file that is associated with a template directory structure.
    This note will be deleted when the section is properly populated

Intro paragraph and link LSE-150.

Quick description of sub-fields (Control Packages, CSCs, EFD, Configuration, Deployment, scriptQueue?)


.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    */index
..    *

High-level description of architecture

..  Any Figures should be stored in the same directory as this file.
    To add images, add the image file (png, svg or jpeg preferred) to the same directory as this .rst file.
    The reST syntax for adding the image is:
    .. figure:: /filename.ext
        :name: fig-label
        :target: http://target.link/url
        Caption text.
