.. This is a template top-level index file for a directory in the procedure's arm of the documentation

.. This is the label that can be used as for cross referencing in the given area
.. Recommended format is "Directory Name"-"Title Name"  -- Spaces should be replaced by hypens
.. _Control-System-Architecture:

############################
Control System Architecture
############################

The LSST Control Software contains the overall control aspects of the survey and the telescope including the computers, network, communication and software infrastructure.
It contains all work required to design, code, test and integrate, in the lab and in the field, the high level coordination software.
The details of the design are contained in the change-controlled document `LSE-150 (Control System Architecture) <https://ls.st/lse-150>`__.

From the stand-point of the user, the architecture permits the capability to have full control at multiple levels, from automated scheduled observing, to control of the individual components.
However, for ease of use, :ref:`high-level packages <System-Architecture-Control-Packages>` have been created to perform standard operations that involve the synchronization of multiple components (e.g. slewing to a new target).

Users can also interact with individual components, which are controlled via :ref:`CSCs <Control-Packages-General-CSC-Overview>`.

These are generally grouped according to their association with a specific telescope.



.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    */index
..    *

There exist multiple components for which documentation is not yet available including: the EFD, configuration management, deployment, and the scriptQueue.

..  Any Figures should be stored in the same directory as this file.
    To add images, add the image file (png, svg or jpeg preferred) to the same directory as this .rst file.
    The reST syntax for adding the image is:
    .. figure:: /filename.ext
        :name: fig-label
        :target: http://target.link/url
        Caption text.
