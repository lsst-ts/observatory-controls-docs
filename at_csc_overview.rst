================================
Auxiliary Telescope CSC Overview
================================

.. warning::
    This page is under heavy development and is subject to change.
    Also may be inaccurate.

Subsystem
    In this context, a subsystem is considered a logical grouping of CSCs.

This page provides a broad overview of the AuxTel CSCs.
This page is meant for operators and developers who are looking for 
information on the software components that make up the Auxiliary Telescope.

* Purpose of page
* State who the audience is.

Overview
========
* Paragraph describing Auxiliary Telescope software
* only deals with CSCs
* Assume primary audience is operators
* Assume surface knowledge of middleware

The Auxiliary Telescope software stack uses a DDS based communication framework to command these components.
The software consists of logical groupings of subsystems which are listed below.
Then each individual CSC is listed below the summary of each subsystem.

Subsystems
----------
* Full name of subsystem
* Summarize Purpose
* Summarize functionality
* List CSCs

ATTCS
^^^^^
:LSST the Docs: https://ts-standardscripts.lsst.io
:Name: The Auxiliary Telescope Control System.

The ATTCS's purpose is to provide control to the Auxiliary Telescope.

Functionally, this is how the telescope's tracking and motion control is commanded.

ATDome
    :LSST the Docs: https://ts-atdome.lsst.io
    
    * Summarize functionality

    The ATDome's functionality is to provide a way to open and close the shutter of the dome.
ATDomeTrajectory
    :LSST the Docs: https://ts-atdometrajectory.lsst.io
    
    The ATDomeTrajectory's functionality is to command the dome to rotate.
ATPtg
    :LSST the Docs: https://ts-atptg.lsst.io
    
    The pointing component's functionality is to send azimuth and elevation commands to the Motion Control System.
ATMCS
    :LSST the Docs: https://ts-atmcs.lsst.io
    
    The motion control system's functionality is to command the positioning of the telescope.

ATCalSys
^^^^^^^^
:LSST the Docs: https://ts-standardscripts.lsst.io
:Name: The Auxiliary Telescope Calibration System.

The ATCalSys's purpose provides calibration control to the telescope.

This is how the telescope's mirror and fine-tuning position is handled.

ATMonochromator
    :LSST the Docs: https://ts-atmonochromator.lsst.io
    
    Provides control over narrow-band controllable wavelength output.
ATHexapod
    :LSST the Docs: https://ts-athexapod.lsst.io
    
    Provides fine grained correction over telescope position.
ATPneumatics
    :LSST the Docs: https://ts-atpneumatics.lsst.io
    
    Provides control over mirror pressure.
FiberSpectrograph
    :LSST the Docs: https://ts-fiberspectrograph.lsst.io
    
    Measures wavelength of the various light sources.
Electrometer
    :LSST the Docs: https://ts-electrometer.lsst.io
    
    Measures photons.

LATISS
^^^^^^
:LSST the Docs: https://ts-standardscripts.lsst.io
:Name: The Atmospheric Transmission and Slitless Spectrograph.

LATISS's purpose is to provide control to the camera.

ATCamera
    :LSST the Docs: https://ts-atcamera.lsst.io
    
    Provides imaging.
ATSpectrograph
    :LSST the Docs: https://ts-atspectrograph.lsst.io
    
    Measures spectra.

