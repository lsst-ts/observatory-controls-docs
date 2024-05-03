.. This is a template top-level index file for a directory in the procedure's arm of the documentation

.. This is the label that can be used as for cross referencing in the given area
.. Recommended format is "Directory Name"-"Title Name"  -- Spaces should be replaced by hypens
.. _Control-Packages-General-CSC-Overview:

####################
General CSC Overview
####################

.. warning::
    This page is under heavy development and is subject to change.

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    Auxiliary-Telescope-CSCs/*
    Main-Telescope-CSCs/*
    System-Level-CSCs/*

The lowest level controllable entities of the Rubin Control system are the individual Commandable Sal Components, or CSCs.
CSCs are responsible for managing the incoming traffic of data and take appropriate actions.
This is often the controlling of a hardware system (e.g. M1M3, M2, Telescope mount etc), but can also be purely software (e.g. Optics Controller Reconstructor, DMCS
Interface, etc).
Due to the large numbers of CSCs, they're generally divided into three categories depending upon which telescope system they're used with.

* :ref:`Main Telescope CSCs<CSC-Overview-Main-Telescope-CSCs>`
* :ref:`Auxiliary Telescope CSCs<CSC-Overview-Auxiliary-Telescope-CSCs>`
* :ref:`System Level CSCs<CSC-Overview-System-Level-CSCs>`

A tabulated list all the CSCs along with their developer, product owner, documentation and repository location can be found in the  `CSC Table <https://ts-xml.lsst.io/#csc-table>`__.

CSCs are written primarily in Python, but also in C++, Java, and LabVIEW.
Communication between components uses the Data Distribution Service (DDS), a standardized message protocol.
The commands, events, and telemetry associated with each CSC are found under the CSC name in the `SAL Interfaces (ts_xml) <https://ts-xml.lsst.io/sal_interfaces/index.html>`__.

In order to facilitate flexible DDS communication between various components written in different languages, a higher-level interface, called the Service Abstraction Layer (SAL) was created to
provide a solution.
It abstracts the software communication of the hardware component written in a particular language such as C++, LabVIEW and Java by using DDS messages sent over the network.
This also allows for components to be commanded by other languages(that support the DDS protocol) regardless of the source's language.

Most CSCs are utilized via higher-level control packages that handle the sequencing of multiple components, which are discussed in the :ref:`Control Packages section<System-Architecture-Control-Packages>`.

The following sections describe the control architecture and interfaces of the observatory.

Description of CSC Control Architecture
=======================================

The :ref:`control architecture for the observatory <Control-System-Architecture>` is a decentralized system of individual software components that use a DDS message based framework to communicate with one another.
Not only do CSCs receive commands from a user or a :ref:`control package <System-Architecture-Control-Packages>`, but CSCs can also subscribe to other CSCs in order to control or receive pertinent information.
Internally, a software development kit (SDK) has been written to provide an abstraction layer over the raw DDS format.
The SDK is called the Service Abstraction Layer(SAL) which provides functionality for generating the libraries necessary for creating CSCs.
SAL uses Adlink's OpenSplice DDS library as the core DDS implementer and then creates a high level abstraction for creating and reading DDS messages.


State Machine Description
^^^^^^^^^^^^^^^^^^^^^^^^^

Each CSC has a state machine that contain a standard set of states.  These set of states are known as summary states.
The state machine is reactive which means that it responds to changes within its the system.
It also responds to outside commands for changes in state.
The low-level details of the state machine are contained in `LSE-209 <ls.st/lse-209>`__.
The following is a higher-level description of the summary states, which are common to every CSC and the most applicable information to the user.

``offline``
    This state is meant for CSCs that have a separate non-SAL command interface.
    These CSCs are considered closed to commands and do not publish any events or telemetry.

``standby``
    In this state a CSC is open to being commanded and is publishing heartbeats.
    However, it is only ready for transitioning to the different states.

``disabled``
    A CSC, if it is controlling hardware, will be connected in this state.
    It will start acquiring data in this state, if available.
    However, it is still not ready for its primary performing function.

``enabled``
    A CSC is ready for performing its primary function in this state.

``fault``
    There is a problem with the CSC that causes it to be unable to perform its intended function.


As part of the enabled state, some CSCs implement substates which provide more details about the current status of a CSC.
In SAL terms, these are known as detailed states.
Each CSC has a generic set of commands that it can support.
Some CSCs do not implement certain generic commands as they may not be necessary or possible.
Probably, the most pertinent of the generic commands are the state transitions which control the summary state.

``enterControl``
    This command transitions the component from the offline to the standby state.
``start``
    This command transitions the component from the standby to the disabled state.
    Also sends the configuration information, if available, to the component.
``enable``
    This command transitions the component from the disabled to the enabled state.
``disable``
    This command transitions the component from the enabled to the disabled state.
``standBy``
    This command transitions the component from the disabled to the standby state.
``exitControl``
    This command transitions the component from the standby to the offline state.


Each CSC also has a set of generic events.
Pertinent events include the following.

settingVersions
    Publishes configuration information about the current settings of the CSC.
errorCode
    Publishes a code and message about a CSC that had an error.
summaryState
    Publishes the summary state of the CSC.
logLevel
    Publishes the current logging level of the CSC log.
logMessage
    Publishes the latest log message from the CSC log.
settingsApplied
    Publishes the settings that were applied to the CSC.
heartbeat
    Publishes a message that indicates a CSC is alive.


CSC Configuration
^^^^^^^^^^^^^^^^^

As required, CSCs have a configuration system for handling various settings and options.
For salobj based CSCs, the configuration system uses a YAML based schema inside of git configuration repositories that are divided according to the telescope that are used on (i.e. main telescope MT, auxiliary telescope AT). Configuration details can be found in `tstn-017 <https://tstn-017.lsst.io>`__. Details on configuration specifics for individual CSCs can be found in their respective user manuals.
Changing a configuration of a CSC requires that the CSC is in the standby state.
The ``start`` command, which transitions a CSC from the ``standby`` to ``diabled`` state, contains a ``settingsToApply`` parameter which expects a string of the label of a configuration.
In order to find this label, an event ``settingVersions`` is published when the CSC transitions to the standby state.
Inside of the event, an attribute ``recommendedSettings`` gives a list of name of configurations that are recommended for use.
Finding configuration repositories is found by using the following format ``ts_config_{system}`` inside of the lsst-ts github organization.


CSC Control Interface
^^^^^^^^^^^^^^^^^^^^^

The control interface for the telescope components is a modified Model-View-Controller pattern where the model handles the state machine, the view handles displaying of information and the controller implements handling the functionality of the component.
`Salobj <https://ts-salobj.lsst.io>`__, a python wrapper around SAL and DDS, implements both the state machine handling and SAL DDS handling for a component.
As such, the actual separation between model and controller is abstracted into the notion of a CSC.
This is why `Salobj <https://ts-salobj.lsst.io>`__ CSCs look slightly different from a surface level overview compared to other CSCs.

The core communication methodology for the middleware architecture is called publish-subscribe.
The idea is that a component publishes responses and a listener will subscribe to the component.
The listener is also called the commandee because it can send commands to the component.
The DDS protocol uses a one to many publish/subscribe model where one component can publish while many components can subscribe.

Components can subscribe to commands as well as publish events and telemetry.
Each of these things are considered a topic and each topic handles one particular function.
A topic can contain items which describe a particular attribute of a topic.
A quick note on the last statement, SAL requires at least one item per topic, but that item is standardized by the Telescope and Site Software team and should not be relevant to an operator.
DDS is a minimum-service protocol which means that there is a quality of service (QoS) attribute which determines the effort the protocol will go through to send a message.

Each of the command, event and telemetry topics are sent across the network when the CSC either issues a command or is receiving an acknowledgment or topic.
Generically, topics are created and have their attributes set as needed during the life cycle of a CSC.
To an operator, the items attribute will be extremely relevant, as this will divulge the actual data about a topic.

To create a command, a command topic object is generated and the parameters of the command become items inside of the topic.
The items are then set inside of the topic and published to the network by the DDS system.
When issuing a command, the topic is sent and the controller of the CSC handles the command and then returns an acknowledgement of a command received.
The next step is for the CSC to perform the command to send an in-progress indication.
When the CSC is done performing the command successfully, it will publish that the command is done.
However, a command can also fail during this process due to hardware or software failure.
The CSC will send a failure indication if this happens, and may also transition to ``fault`` state depending on the situation.

Another type of issue can be a lack of acknowledgement due to network related reasons.
The most likely culprit is the network is too busy for the topic to be received at that time.
SAL has integer codes that indicate the status of a command.
These codes can indicate success, failure or non-acknowledgement.
If a command status is not received at any point during this communication, then the command is considered to have been not acknowledged.
A CSC can wait for a command to complete before moving on to other tasks, which is known as a blocking command.
But, a CSC can also switch to doing other tasks while it waits for a command to complete.

Events are published by the CSC and indicate a change in the component.
These event topics are received by the listener, which can then be handled for further processing.

Telemetry is the on-going data stream generated by the CSC.
It is published at a set rate.

The full process for defining CSCs and all the topics is described in the `ts_xml README <https://github.com/lsst-ts/ts_xml/blob/main/README.md>`_.
However, of particular interest is the policy regarding defining units in the XML definition files.
For that, please refer to the :ref:`XML_Units` document.

Sources
=======
* `CSC Development <https://confluence.lsstcorp.org/pages/viewpage.action?spaceKey=LTS&title=CSC+Development>`_
* `TSTN-017 <https://tstn-017.lsst.io/>`_
* `LSE-150 <https://docushare.lsst.org/docushare/dsweb/Get/LSE-150/>`_
* `LSE-70 <https://docushare.lsst.org/docushare/dsweb/Get/LSE-70>`_
* `LSE-209 <https://docushare.lsst.org/docushare/dsweb/Get/LSE-209>`_
* `LTS-306 <https://docushare.lsst.org/docushare/dsweb/Get/LTS-306>`_
* `LSE-307 <https://docushare.lsst.org/docushare/dsweb/Get/LSE-307>`_
