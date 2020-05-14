.. This is a template top-level index file for a directory in the procedure's arm of the documentation

.. This is the label that can be used as for cross referencing in the given area
.. Recommended format is "Directory Name"-"Title Name"  -- Spaces should be replaced by hypens
.. _Observatory-Controls:

Rubin Observatory Controls Documentation
########################################

The LSST Control Software contains the overall control aspects of the survey and the telescope including the computers, network, communication and software infrastructure. It contains all work required to design, code, test and integrate, in the lab and in the field, the high level coordination software.



Control System Architecture
===========================

The Rubin control system is based on a reactive data-driven actor-based architecture that uses a multi cast Data Distribution Service (DDS) messaging protocol middleware.
The system consists of numerous individual components, which are generally grouped together and controlled via a higher-level control package which handles the sequencing and simplifies interactions for higher-level use-cases (e.g. slewing the telescope).


.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    System-Architecture/index
..    *


Control System User Interfaces
==============================

Interacting with the observatory software and hardware can be performed through many different interfaces.

LSST Observing Visualization Environment (LOVE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nublado (Jupyter) Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^

EFD and Chronograf
^^^^^^^^^^^^^^^^^^

LSST Camera Image Visualization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scheduler Visualization
^^^^^^^^^^^^^^^^^^^^^^^
OpSim?


Project Documentation Information
=================================

- Describes information regarding this documentation tree, including how to contribute.


.. toctree::
    :maxdepth: 2
    :glob:
    :titlesonly:

    project/index



..  Any Figures should be stored in the same directory as this file.
    To add images, add the image file (png, svg or jpeg preferred) to the same directory as this .rst file.
    The reST syntax for adding the image is:
    .. figure:: /filename.ext
        :name: fig-label
        :target: http://target.link/url
        Caption text.
