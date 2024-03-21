.. This is a template top-level index file for a directory in the procedure's arm of the documentation

.. This is the label that can be used as for cross referencing in the given area
.. Recommended format is "Directory Name"-"Title Name"  -- Spaces should be replaced by hypens
.. _Observatory-Controls:

Rubin Observatory Controls Documentation
########################################

The LSST Control Software contains the overall control aspects of the survey and the telescope including the computers, network, communication and software infrastructure.
It contains all work required to design, code, test and integrate, in the lab and in the field, the high level coordination software.

.. warning::
    This page is under heavy development and is subject to change.


Control System Architecture
===========================

The Rubin control system is based on a reactive data-driven actor-based architecture that uses a multi cast Data Distribution Service (DDS) messaging protocol middleware.
The system consists of numerous individual components, called Controllable SAL Components (CSCs), which are generally grouped together and controlled via a higher-level control package which handles the sequencing and simplifies interactions for higher-level use-cases (e.g. slewing the telescope).
This section and the links there-in detail the architecture of the control system, the different control packages, and link to the documentation to the individual CSCs.


.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    System-Architecture/*
..    *

.. _Control-System-User-Interfaces:

Control System User Interfaces
==============================

Interacting with the observatory software and hardware can be performed through many different interfaces.

.. _Control-System-User-Interfaces-LOVE:

LSST Observing Visualization Environment (LOVE)
-----------------------------------------------
LOVE is the graphical display of the system status.
It will also have areas where the user can interact with the system, including a ``STOP`` button and an interface to the scriptQueue.

.. _Control-System-User-Interfaces-Nublado:

Nublado (Jupyter) Interface
---------------------------
Analogous to the notebook interface used with the `LSST Science Platform Notebook Aspect Documentation <https://nb.lsst.io>`__, there is a Nublado instance that is connected to the control network.
This enables users to interact with the system from a notebook environment which is useful for development purposes, but also has example notebooks to perform certain functions, such as collimation of the Auxiliary Telescope and some fault recovery procedures.

.. _Control-System-User-Interfaces-Script-Queue:

Script Queue
------------

The `ScriptQueue`_ is the main interface for users and operators to perform standard operation procedures.
It contains a set of `SAL Scripts`_ that users can schedule, organize and monitor their execution.

.. _ScriptQueue: https://ts-scriptqueue.lsst.io
.. _SAL Scripts: https://ts-salobj.lsst.io/sal_scripts.html

There are two ScriptQueues running in parallel in the system, one for the Main Telescope (``index=1``) and another for the Auxiliary Telescope (``index=2``).
Users can interface with them either using the :ref:`LOVE interface <Control-System-User-Interfaces-LOVE>` (preferred) or from :ref:`Jupyter notebooks in nublado <Control-System-User-Interfaces-Nublado>`.

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    Control-User-Interfaces/writing-sal-scripts.rst

.. _Control-System-User-Interfaces-Watcher:

Watcher
-------

The `Watcher`_ is an alarm system that is responsible for monitoring the observatory status.
The alarms sent by the `Watcher`_ are displayed in the :ref:`LOVE interface <Control-System-User-Interfaces-LOVE>` where users have the option to acknowledge it and take actions to mitigate any problems.

.. _Watcher: https://ts-watcher.lsst.io

See the `Watcher`_ documentation for more information about handling alarms and escalation.

.. _Control-System-User-Interfaces-Engineering-Facility-Database:

Engineering Facility Database
-----------------------------

The Engineering Facility Database (EFD) contains all information that is communicated via the control network, such as commands, events, telemetry and even small files.
Interacting with the database can be performed in multiple ways depending on your use-case. A python client has been built to query the database, which can also be used via the Nublado interface mentioned above.
However, if a more visual user-friendly interface is required, users should consider using Chronograf, which works well for specific use-cases.

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    Control-User-Interfaces/EFD.rst

.. _Control-System-User-Interfaces-LSST-Camera-Image-Visualization:

LSST Camera Image Visualization
-------------------------------
Due to the large size and complexity of assembling a single LSST image, a visualization tool is being developed to enable observers to view and interact with them as they roll off the telescope. This tool is still under heavy development.


.. _Obs-Ops-Operational-Tutorials:

System Development Guidelines and Policies
==================================================================

The CSC interface definitions are data objects and they are stored in the `ts_xml <https://github.com/lsst-ts/ts_xml>`_ repository.
This is where CSCs and their APIs are defined.
The Service Abstraction Layer (SAL) is an utility that consumes the XML to produce language specific libraries that enable communication over the DDS network.
The procedures for maintaining these definitions are defined in the `ts_xml <https://github.com/lsst-ts/ts_xml>`_ repository itself.
As each CSC is developed under the guidelines of the specific team doing the work, there is no single resource to look at to define CSC development.
However, there are certain system level policies that govern the development processes.

System-Level Policies
---------------------
:ref:`XML_Units`

Team Specific Development Guidelines
------------------------------------
`TSSW Developers Guide <https://tssw-developer.lsst.io>`_.

System Testing, Deployments, and Upgrades
==================================================================

Procedures for system testing, software build, deployment and upgrades at the summit and at TTS are compiled here.

.. toctree::
    :maxdepth: 2
    :glob:
    :titlesonly:

    System-Testing-Deployments-and-Upgrades/index

:ref:`Troubleshooting`
======================
Software user manuals are often packaged and released with the code such that the documentation is available at the same time new features are released.
Because issues often arise with software that is already released, this section focuses on current issues and their workarounds.

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    Troubleshooting/*

.. _Project-Documentation-Information:

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
