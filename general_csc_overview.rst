====================
General CSC Overview
====================

.. warning::
    This page is under heavy development and is subject to change.


The purpose of this page is to provide a general CSC overview.
A CSC is a Commandable SAL Component.
The Service Abstraction Layer is a DDS based messaging middleware for
communicating with the components of the telescope.
It abstracts the control of hardware written in a particular language such as
C++, Labview and Java by using DDS messages sent over the network.
This allows for components to be commanded by other languages(that support 
DDS) regardless of source language.

Control Packages & Classes
==========================

A control package is software that implements a wrapper around a hardware
control interface.
Packages are written in one of the following languages Java, C++, Python and Labview.
Each package is located in individual repositories.
A control class is a high level grouping of systems that make up the telescope
that are not found in separate indivdual repositories.
For example, the ATTCS is found in the ts_standardscripts repository as 
opposed to the ts_attcs repository.


Description of Control Architecture
===================================

* DDS based
* SAL
* Hardware
* Things


Control Interfaces
==================

Our control interfaces work by communicating with devices over one of many interfaces.
The vendor provides these interfaces for scripting and development purposes.
Most communicate with either serial or TCP/IP connection.
Some communicate over modbus.
