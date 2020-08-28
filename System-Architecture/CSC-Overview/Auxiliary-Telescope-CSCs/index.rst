.. This is a template top-level index file for a directory in the procedure's arm of the documentation

.. This is the label that can be used as for cross referencing in the given area
.. Recommended format is "Directory Name"-"Title Name"  -- Spaces should be replaced by hyphens
.. _CSC-Overview-Auxiliary-Telescope-CSCs:

########################
Auxiliary Telescope CSCs
########################

.. warning::
    This page is under heavy development and is subject to change.

As mentioned in the :ref:`Control-Packages-General-CSC-Overview`, it is convenient to group CSCs into one of three categories, one of which is the Auxiliary Telescope (AuxTel or AT).
All CSCs associated with the AuxTel receive an ``AT`` prefix to their name, such as the ATHexapod or ATDome.
CSCs in this group are strictly associated with the operation and calibration of the AuxTel and cannot be moved between systems.

Although a full list of AuxTel CSCs, indicated by the ``AT`` prefix, are found in the `Master CSC Table <https://ts-xml.lsst.io/#master-csc-table>`__, which is auto-generated from the XML code which defines the ICDs, it is generally most useful to associate the CSCs by the control-package it is associated with, as it done below.

Links are provided to the user guide when available. Interface information for each CSC can be found in the `ts-xml guide <https://ts-xml.lsst.io/>`__.


Auxiliary Telescope Control System (ATCS)
=========================================

The :ref:`ATCS class <Control-Packages-AuxTel-ATCS>` is a high-level control package that provides a user-friendly interface to operating the telescope and dome related CSCs on the Auxiliary Telescope.

The following AT CSCs are associated with that class, but also controllable individually if required:

`ATDome <https://ts-atdome.lsst.io>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    * The `ATDome CSC <https://ts-atdome.lsst.io>`__ controls the dome enclosure, including the shutter and rotation (azimuth) position.

`ATDomeTrajectory <https://ts-atdometrajectory.lsst.io>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    * The `ATDomeTrajectory CSC <https://ts-atdometrajectory.lsst.io>`__ controls how and when the dome moves relative to the telescope position. It essentially monitors the telescope position and trajectory and sends commands to the ATDome CSC when appropriate to do so.

ATPtg
^^^^^

    * The AT pointing component CSC converts the celestial position to mount coordinates (altitude and azimuth) and includes an analytical model of the mount to increase pointing and tracking accuracy. It sends position commands to the AT mount control system (ATMCS).

`ATMCS <https://ts-atmcs.lsst.io/>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    * The AT mount control system performs the servo control of the telescope mount motors and encoders.
        During standard on-sky operations, it receives its position, velocity and time (PVT vector) for target tracking from the pointing component (ATPtg).

`ATPneumatics <https://ts-atpneumatics.lsst.io>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    * The ATPneumatics system is used to control the actuators beneath the mirror such that the proper shape is held as a function of elevation. It also controls the mirror covers and vents.


`ATHexapod <https://ts-athexapod.lsst.io>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    * The ATHexapod CSC is used to control the PI hexapod that supports the secondary mirror. It is used to focus and maintain collimation of the optics. It is primarily controlled by the AT Active Optics System (ATAOS).

.. `ATAOS <https://ts-ataos.lsst.io>`__

ATAOS
^^^^^

    * The AT Active Optics System (ATAOS) is used to maintain collimation and focus of the telescope as a function of position, temperature and instrument setup.

LSST Auxiliary Telescope Imager and Slitless Spectrograph (LATISS)
==================================================================

CSCs associated with LATISS are best control via the :ref:`LATISS class <Control-Packages-AuxTel-LATISS>`, which is a high-level control package.
Not only does the class handle the spectrograph setup, but it also handles image taking and ensures the headers get populated appropriately.

The following AT CSCs are associated with that class, but also controllable individually if required:


ATSpectrograph
^^^^^^^^^^^^^^

    * The ATSpectrograph CSC controls the setup of the spectrograph grating and filter.


ATCamera
^^^^^^^^

    * The ATCamera controls the image taking aspects, including control of the shutter. It also communicates with the ATDAQ (which is a camera component but not a CSC).

ATHeaderService
^^^^^^^^^^^^^^^

    * The ATHeaderService accumulates metadata before and during an exposure, then assembles a header file and publishes it to the large file annex.

ATArchiver
^^^^^^^^^^

    * The ATArchiver pulls the image from the ATDAQ, pulls the header from the ATHeaderService and assembles the final fits image.


Auxiliary Telescope Calibration System (ATCalSys)
=================================================

The :ref:`ATCalSys class <Control-Packages-AuxTel-ATCalSys>` is currently under development and will be the primary way to setup the observatory for calibrations.
This will included selecting light sources, wavelengths, and enabling/disabling the cooling system.

The following AT CSCs will be associated with the class, but also controllable individually if required:

ATWhiteLight
^^^^^^^^^^^^

    * The ATWhiteLight CSC controls the high-power quartz-halogen lamp that feeds the monochromator. It also controls the cooling system that must be operating while the lamp is in use.


ATMonochromator
^^^^^^^^^^^^^^^

    * The ATMonochromator CSC controls the Horiba monochromator which is used to select the appropriate wavelength and bandpass for a given flat field.


`FiberSpectrograph <https://ts-fiberspectrograph.lsst.io>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    * The fiberSpectrograph CSC controls a commercial fiber-fed spectrograph that is used to measure the spectral energy distribution exiting the monochromator and being projected to the screen.
    * Because the same spectrometers are used in the main telescope, it is in fact a member of the :ref:`System Level CSCs <CSC-Overview-System-Level-CSCs>` but listed here for completeness.

Electrometer
^^^^^^^^^^^^

    * The electrometer CSC is used to measure the charge accumulated by a Hamamatsu S2251 photodiode. This diode is used to measure the brightness of the exitant light of the monochromator during a flat field exposure.
    * Because the same electrometers are used in the main telescope, it is in fact a member of the :ref:`System Level CSCs <CSC-Overview-System-Level-CSCs>` but listed here for completeness.

