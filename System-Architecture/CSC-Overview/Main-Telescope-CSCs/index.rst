.. This is a template top-level index file for a directory in the procedure's arm of the documentation

.. This is the label that can be used as for cross referencing in the given area
.. Recommended format is "Directory Name"-"Title Name"  -- Spaces should be replaced by hyphens
.. _CSC-Overview-Main-Telescope-CSCs:

###################
Main Telescope CSCs
###################

.. warning::
    This page is under heavy development and is subject to change.

As mentioned in the :ref:`Control-Packages-General-CSC-Overview`, it is convenient to group CSCs into one of three categories, one of which is the Main Telescope (or MT).
All CSCs associated with the Main Telescope receive an ``MT`` prefix to their name, such as the MTMount or MTM1M3 [#f1]_.
CSCs in this group are strictly associated with the operation and calibration of the Main Telescope and cannot be moved between systems.

Although a full list of Main Telescope CSCs, indicated by the ``MT`` prefix are found in the `Master CSC Table <https://ts-xml.lsst.io/#master-csc-table>`__, which is auto-generated from the XML code which defines the ICDs, it is generally most useful to associate the CSCs by the control-package it is most often controlled from, as is done below.

Links are provided to the user guide when available. Interface information for each CSC can be found in the `ts-xml guide <https://ts-xml.lsst.io/>`__.
Due to the large number of CSCs, they are arranged according to their :ref:`high-level control class <System-Architecture-Control-Packages>`, when one exists.


Main Telescope Control System (MTCS)
====================================

.. _Dome: https://ts-dome.lsst.io/
.. _MTDomeTrajectory: https://ts-mtdometrajectory.lsst.io/
.. _MTMount: https://ts-mtmount.lsst.io/
.. _MTAOS: https://ts-mtaos.lsst.io/

The :ref:`Main <Control-Packages-MainTel>` is a high-level control package that provides a user-friendly interface to operating the telescope and dome related CSCs on the Main Telescope.

The following MT CSCs are associated with that class, yet may also ben controlled individually, if required:

`MTMount`_
^^^^^^^^^^

    * The MT mount control system performs the servo control of the telescope mount motors and encoders.
        This includes the camera cable wrap.

MTPtg
^^^^^

    * The MT pointing component CSC converts the celestial position to mount coordinates (altitude and azimuth) and    includes an analytical model of the mount to increase pointing and tracking accuracy.
      It sends position and velocity commands to the `MTMount`_.


Rotator
^^^^^^^

    * The Rotator CSC [#f2]_ controls the camera rotator, which is located between the camera hexapod and camera itself.
      It's primary use is to rotate the camera during observations to compenstate for field rotation that occurs in Alt-Az telescope mount designs.

Hexapod
^^^^^^^

    * The Hexapod CSC [#f2]_ controls both the M2 and Camera hexapods.
      These hexapods are used to position the M2 mirror and camera along the optical axis (boresight).
      These devices are commanded by the MTAlignment and MTAOS CSCs.

`Dome`_
^^^^^^^^

    * The `Dome`_ CSC [#f2]_ is responsible for the positioning of the main telescope dome and the light and windscreen.
      It also handles the positioning the louvers and opening and closing the dome shutter.
      The logic that determines the ideal positioning of the dome and trajectory is handled externally in the MTDomeTrajectory CSC.

`MTDomeTrajectory`_
^^^^^^^^^^^^^^^^^^^

    * The `MTDomeTrajectory`_ CSC controls how and when the dome moves relative to the telescope position. It essentially monitors the telescope position and trajectory and sends commands to the MTDome CSC when appropriate to do so.


MTAlignment
^^^^^^^^^^^

    * The MTAlignment CSC performs the initial alignment of the optics using the laser tracker.
      From this initial position further refinements are made via the `MTAOS`_.

`MTAOS`_ (Active Optics System)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    * The `MTAOS`_ is used to perform optical alignment, including the measurement of the wavefront error induced by the optical system.
      The MTAOS also calculates and sends corrections to the M1M3 and M2 mirror systems.

MTM1M3
^^^^^^

    * The MTM1M3 CSC controls the actuators and hard-points in the M1M3 mirror.

MTM1M3TS
^^^^^^^^

    * The MTM1M3TS CSC controls the thermal system in the M1M3 mirror cell.

MTM2
^^^^^

    * The MTM2 CSC controls the shape and thermal system for the M2 mirror.


.. rubric:: Footnotes

.. [#f1] This naming standard was adopted after a few CSCs had already been named and are in development by contractors. We are working to unify the naming scheme but a few exceptions to the rule still remain.
.. [#f2] This is an example of a CSC that has yet to be renamed to meet the naming convention standards.