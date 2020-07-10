.. This is a template top-level index file for a directory in the procedure's arm of the documentation

.. This is the label that can be used as for cross referencing in the given area
.. Recommended format is "Directory Name"-"Title Name"  -- Spaces should be replaced by hypens
.. _System-Architecture-Control-Packages:


################
Control Packages
################

A control package (sometimes referred to as a control class) consists of a high-level class that can be called by a user to perform coordinated sequencing of CSCs.
It also provides low-level access to :ref:`CSCs <Control-Packages-General-CSC-Overview>` should it be required.
Another way to think about these packages is that they perform coordinated actions of multiple CSCs from a single command.
Examples of use-cases where control packages are useful is for things like slewing the telescope, shutting down for the night, or performing focus offsets.
More detailed information is found with the documentation that is built with the `ts_observatory_control package <https://ts-observatory-control.lsst.io>`__.
The source code for the packages are found in the `ts_observatory_control <https://github.com/lsst-ts/ts_observatory_control/tree/master>`__ repository on github.

The packages can be called from notebooks, and/or used by CSCs or scripts executed by the scriptQueue.
As a result of the continuing development of the functionality of these packages, they must have integration and unit tests written in order to be considered safe for official observatory use.
Users looking to develop or expand the functionality from what is in these packages must follow the `Notebooks, Observing Scripts and Utilities Development Cycle <https://tstn-010.lsst.io>`__

The control classes themselves are divided into multiple catetories, but generally can be separated by if they control aspects of the :ref:`Main <Control-Packages-MainTel>` or :ref:`Auxiliary <Control-Packages-AuxTel>` Telescopes.

More information regarding CSCs are found in the :ref:`CSC Overview section <Control-Packages-General-CSC-Overview>` and the sub-pages.


.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    */index
..    *


.. _Control-Packages-AuxTel:

Auxiliary Telescope Control Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _Control-Packages-AuxTel-ATCS:

ATCS
----
The ATCS is used to perform actions related to the telescope and dome motions.
It nests the functionality of the ATMCS, ATAOS, ATPneumatics, `ATHexapod <https://ts-athexapod.lsst.io>`__, ATDome, and ATDomeTrajectory CSCs.
This class contains multiple high-level methods to perform activities such as: opening/closing the observatory, slewing to and tracking targets and performing many types of pointing offsets.

For more detailed descriptions see the methods summary in the `ATCS User Manual Documentation <https://ts-observatory-control.lsst.io/py-api/lsst.ts.observatory.control.ATCS.html#lsst.ts.observatory.control.ATCS>`__

.. _Control-Packages-AuxTel-LATISS:

LATISS
------
The LATISS control package contains methods to perform setup of the spectrograph and taking various types of images (flats, darks, bias, science etc).
It nests the functionality of the ATSpectrograph, ATCamera, ATArchiver, and ATHeaderService CSCs.

For more detailed descriptions see the methods summary in the `LATISS User Manual Documentation <https://ts-observatory-control.lsst.io/py-api/lsst.ts.observatory.control.LATISS.html#lsst.ts.observatory.control.LATISS>`__

.. _Control-Packages-AuxTel-ATCalSys:

ATCalSys
--------
The Auxiliary Telescope Calibration System control package is still under-development.


.. _Control-Packages-MainTel:

Main Telescope Control Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
These packages are still under development and have not been tagged for release.






..  Any Figures should be stored in the same directory as this file.
    To add images, add the image file (png, svg or jpeg preferred) to the same directory as this .rst file.
    The reST syntax for adding the image is:
    .. figure:: /filename.ext
        :name: fig-label
        :target: http://target.link/url
        Caption text.
