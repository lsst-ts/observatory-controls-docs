====================
General CSC Overview
====================

.. warning::
    This page is under heavy development and is subject to change.


The purpose of this page is to provide a general CSC overview.
Here's a brief summary of terms and definitions:
* A CSC is a Commandable SAL Component.
* The Service Abstraction Layer is a DDS based messaging middleware for communicating with the components of the telescope.
* DDS, Data Distribution Service, is a standardized message protocol.
In order to facilitate flexible DDS communication between various components
written in different languages, a higher-level interface (SAL) was created to provide a solution.
It abstracts the software communication of the hardware component written in a particular language
such as C++, LabVIEW and Java by using DDS messages sent over the network.
This allows for components to be commanded by other languages(that support 
the DDS protocol) regardless of the source's language.
CSCs are divided between the Main Telescope, Auxiliary Telescope and overall
observatory system.

The first section describes the purpose and definition of control packages.
The next section describes the control architecture of the observatory.
The final section describes the control interfaces of the observatory.

.. contents:: Overview
    :local:

Control Packages & Classes
==========================

A control package is a high-level grouping of CSCs.
The idea is to create some coordinated control systems for the telescope that are related to
a particular purpose.  
A couple of these purposes are control of the low-level telescope and control of the entire observatory.
These packages become the telescope control system (TSC) and observatory's control system (OSC).
Another layer of packages are the telescope's imaging system and its calibration system.
These systems can be then used by the provided scripting system in
order to perform coordinated functionality of the observatory.
The control packages deal with performing actions with the observatory
such as rotating and moving the dome or telescope mount.
An official lsst-ts git repository has been created to store these packages.
As a result of the continuing development of the functionality of these
packages, they must have integration and unit tests written in order to be
considered safe for official observatory use.

.. so I am not sure what we are trying to descibe here.  The section is called Control Packages
.. and Classes, so I assume we are trying to define Classes?  Classes are essentially scripts that
.. have gone through riggerous testing (as utilities) and contain functionality that can be used 
.. by more than one script.
..
Another level of packages will deal with helping to perform observing duties and
integrating with the Science Platform.
The observing duties packages are located in the lsst-ts git repo. 
The science platform packages are located in the lsst-dm repo.
This level is considered a testing grounds for these utilities which could be
promoted to a official control package.

Description of Control Architecture
===================================

The control architecture for the telescope is a decentralized system of
individual software components that use a DDS message based framework to
communicate with one another.
CSCs can also subscribe to other CSCs in order to control or receive
pertinent information.
Internally, a software development kit(SDK) has been written to provide an
abstraction layer over the raw DDS format.
The SDK is called the Service Abstraction Layer(SAL) which provides
functionality for generating the libraries necessary for creating CSCs.
SAL uses Adlink's OpenSplice DDS library as the core DDS implementer and
then creates a high level abstraction for creating and reading DDS messages.

As required, CSCs have a configuration system for handling various settings
and options.
The configuration system uses a YAML based schema inside of git configuration
repositories that are divided according to the telescope that are used on 
(i.e. main telescope MT, auxiliary telescope AT).
Changing a configuration of a CSC requires that the CSC is in the standby state when the
``start`` command is sent to it.  The ``start`` command contains a ``settingsToApply`` parameter which contains a string of
the label of a configuration.
In order to find this label, an event ``settingVersions`` is published when the
CSC transitions to the standby state.
Inside of the event, an attribute ``recommendedSettings`` gives a list of name of
configurations that are recommended for use.
Finding configuration repositories is found by using the following format
``ts_config_{system}`` inside of the lsst-ts github organization.

Control Interfaces
==================

The control interface for the telescope components is a modified Model-View-Controller pattern
where the model handles the state machine, the view handles displaying of
information and the controller implements handling the functionality of the
component.
Salobj, a python wrapper around SAL and DDS, implements both the state machine
handling and SAL DDS handling for a component.
As such, the actual separation between model and controller is abstracted into
the notion of a CSC.
This is why salobj CSCs look slightly different from a surface level overview
to other CSCs.

The core communication methodology for the middleware architecture is called
publish-subscribe.
The idea is that a component publishes responses and a listener will
subscribe to the component.
The listener is also called the commandee because it can send commands to the
component.
The DDS protocol uses a one to many publish/subscribe model where one component 
can publish while many components can subscribe.

Components can subscribe to commands and publish events and telemetry.
Each of these things are considered a topic and each topic handles one particular function.
A topic can contain items which describe a particular attribute of a topic.
A quick note on the last statement, SAL requires at least one item per topic, but that
item is standardized by the Telescope and Site Software team and should not be
relevant to an operator.
DDS is a minimum-service protocol which means that there is a quality of
service (QoS) attribute which determines the effort the protocol will go through 
to send a message.  

Each of the command, event and telemetry topics are sent across the
network when the CSC either issues a command or is receiving an acknowledgment or topic.
Generically, topics are created and have their attributes set as needed during
the life cycle of a CSC.
To an operator, the items attribute will be extremely relevant,as this will
divulge the actual data about a topic.

To create a command, a command topic object is generated and the parameters of
the command become items inside of the topic.
The items are then set inside of the topic and published to the network by the
DDS system.
When issuing a command, the topic is sent and the controller of the
CSC handles the command and then returns an acknowledgement of a command
received.
The next step is for the CSC to perform the command to send an
in-progress indication.
When the CSC is done performing the command successfully, it will publish
that the command is done.
However, a command can also fail during this process due to hardware or software failure.
The CSC will send a failure indication if this happens.

Another type of issue can be a lack of acknowledgement due to network related reasons.
The most likely culprit is the network is too busy for the topic to be
received at that time.
These codes can indicate success, failure or non-acknowledgement.
If a command status is not received at any point during this communication,
then the command is considered to have been not acknowledged.
A CSC can wait for a command to complete before moving on to other tasks,
which is known as a blocking command.
But, a CSC can also switch to doing other tasks while it waits for a
command to complete.

Events are published by the CSC and indicate a change in the component.
These event topics are received by the listener, which can then be handled for
further processing.

Telemetry is the on-going data stream generated by the CSC.  It is published at a set rate.

Each CSC has a state machine that contain a standard set of states.  These set
of states are known as summary states.
The state machine is reactive which means that it responds to changes within its
the system.  It also responds to outside commands for changes in state.
Here are the following summary states, which every CSC must have according to
requirements.

offline
    This state is meant for CSCs that have a separate non-SAL command
    interface.
    These CSCs are considered closed to commands and do not publish
    any events or telemetry.
standby
    In this state a CSC is open to being commanded and is publishing heartbeats.
disabled
    A CSC, if it is controlling hardware, will be connected in this state.
    It will start acquiring data in this state, if available.
    However, it is still not ready for its primary performing function.
enabled
    A CSC is ready for performing its primary function in this state.
fault
    There is a problem with the CSC that causes it to be unable to 
    perform its intended function.

As part of the enabled state, some CSCs implement substates which
provide more details about the current status of a CSC.
In SAL terms, these are known as detailed states.
Each CSC has a generic set of commands that it can support.
Some CSCs do not implement
certain generic commands as they may not be necessary or possible.
Probably, the most pertinent of the generic commands are the state transitions
which control the summary state.

enterControl
    This command takes the component from the offline to the standby state.
start
    This command takes the component from the standby to the disabled state.
    Also sends the configuration information, if available, to the component.
enable
    This command takes the component from the disabled to the enabled state.
disable
    This command takes the component from the enabled to the disabled state.
standBy
    This command takes the component from the disabled to the standby state.
exitControl
    This command takes the component from the standby to the offline state.
    
.. it would be good to list the generic events as well.

Sources
=======
* `CSC Development <https://confluence.lsstcorp.org/pages/viewpage.action?spaceKey=LTS&title=CSC+Development>`_
* `TSTN-017 <https://tstn-017.lsst.io/>`_
* `LSE-150 <https://docushare.lsst.org/docushare/dsweb/Get/LSE-150/>`_
* `LSE-70 <https://docushare.lsst.org/docushare/dsweb/Get/LSE-70>`_
* `LSE-209 <https://docushare.lsst.org/docushare/dsweb/Get/LSE-209>`_
* `LTS-306 <https://docushare.lsst.org/docushare/dsweb/Get/LTS-306>`_
* `LSE-307 <https://docushare.lsst.org/docushare/dsweb/Get/LSE-307>`_
