######################
Control System Upgrade
######################

This documentation outlines the upgrade process for the control system software interface.
Since the control system is tightly coupled with the interface specification (XML), the communication backplane (Kafka) and the abstraction layer (SAL), this documentation focuses on upgrades to those dependencies.
Instructions for building base artifacts and component containers are covered elsewhere (see :ref:`TSSW-Build-System-Introduction` and `Cycle Build <https://ts-cycle-build.lsst.io>`_).

Deployment steps are described in a general way, with site-specific differences highlighted as needed. Please read this guide in advance, as you'll need to set up credentials and code beforehand.
Control system upgrades follow a cycle model, similar to Data Management’s six-month development cycles.
However, in the case of the control system, a cycle build happens roughly every two months, though the cadence can vary- often extending longer, but on occasion the period between cycles can be shorter.

In addition to full cycle upgrades, we now support incremental upgrades, which happen in between cycles. These smaller updates apply a limited set of changes and can be requested as needed, as long as the associated XML modifications do not break schema compatibility.
Throughout this documentation, there will be sections specific to the case of an incremental upgrade, as these are handled slightly differently from full cycle upgrades. Keep in mind that this process is still undergoing formalization and so it is likely that the documentation will change as we refine the process.

Upgrades are labeled using the format Cycle N for full upgrades, where N is the next revision in the cycle sequence. For incremental upgrades, we use Cycle N, Revision M, where M denotes the incremental revision within that cycle.

When referencing deployment sites, we use the following shorthand for the various test stands:

* TTS: Tucson test stand
* BTS: Base (La Serena) test stand

We refer to Cerro Pachon as the Summit when talking about it as a deployment site.

.. _Control-System-Upgrade-Getting-Ready:

Getting the Dependencies Ready
==============================

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    Getting-Ready/*

Pre-Deployment Activities
=========================

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    Pre-Deployment-Activities/*

Deployment Activities
=====================

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    Deployment-Activities/*

Camera software
===============

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    Camera-Systems/*
