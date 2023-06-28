.. _Control-System-Upgrade-Getting-Ready-Upgrading-Interface-XML:

Upgrading the Interface (XML)
=============================

#. Coordinate with the major stakeholders at the Commissioning Activities Planning (CAP) meeting to discuss a new release.
#. Determine a date for deploying to the summit and work backwards to arrive at a date for closing the necessary work (usually XML).
    * Keep in mind dates for observing runs and special overnight work within the observatory.
    * The approximate look back time is two weeks from the end of work to summit deployment.
    * This period may be longer if extra testing or other circumstances require it.
    * Further instructions will be provided in :ref:`Control-System-Upgrade-Getting-Ready-Setting-Schedule`.
    * Once the Summit deployment date is selected, use the ``create_summit_upgrade_ticket`` script in the vanward_ package to create the appropriate Jira ticket.
#. Create a cycle build Confluence page (`Software Upgrades <https://confluence.lsstcorp.org/pages/viewpage.action?spaceKey=LSSTCOM&title=Software+Upgrades>`_) with the versions of core packages and any operational changes.
#. Present the schedule at the CAP meeting at least one week in advance of the work closure deadline.
#. Go over the work in the `appropriate release <https://jira.lsstcorp.org/projects/CAP?selectedItem=com.atlassian.jira.jira-projects-plugin%3Arelease-page&status=unreleased>`_ in the CAP Jira project.
    * This is identified by label of: ``ts_xml X.Y``.
    * Use the ``release_tickets`` script in the vanward_ package.
#. Ensure that all work merged in the `ts_xml <https://github.com/lsst-ts/ts_xml.git>`_ repository has a ticket associated with it in the release.
    * Folks should be following the `XML Work Reporting <https://tssw-developer.lsst.io/procedures/reporting-xml-release-work.html>`_ procedure.
    * Use the ``find_merges_without_release_tickets`` script in the vanward_ package.
#. Send a reminder about the work closure deadline at least one day prior AND the day of the closure.
#. Ensure that all work tickets are closed when the deadline passes (use Step 4 script).
#. Work with the Telescope and Site Build Engineer on the day of the artifact build to go over any potentially open work and sign off on all software versions being used.

Upgrading SAL
=============

While upgrading SAL usually coincides with an upgrade to the XML, it does not have to be the case.
An upgrade for SAL may use the previous cycle's XML version in order to limit the potential for surprises.
The primary developer (Dave Mills) for SAL is responsible for ensuring the necessary work is completed and the new version is ready.


Upgrading DDS (OpenSplice)
==========================

Upgrading the communication backplane via updating the OpenSplice version requires care and extra lead time.
The DDS oversight committee (Dave Mills, Tiago Ribeiro, Michael Reuter [advisory]) will make the determination if a new version of OpenSplice is ready for incorporation into a new cycle.
This determination requires dedicated testing from the main members of committee to ensure readiness.
Cycle builds upgrading OpenSplice have longer testing periods split into two phases.
The first phase builds a smaller section of the control system components and deploys them for testing on the TTS.
Work is done to ensure that this small system is operating within the normal parameters.
The second phase happens when the full system is built as part of the standard deployment operations.


.. _Control-System-Upgrade-Getting-Ready-Setting-Schedule:

Setting a Schedule
==================

While below is an example, use your best judgment to set dates and make sure the major stakeholders are informed of the schedule by the CAP meeting.

* Close of release work : Day 1.
* Artifact (RPMs/JARs) build on Day 2 to Day 3.
* Build conda packages and deployment artifacts Day 4 to Day 10.
* Initial deployment to TTS on Day 13 with all CSCs available on TTS by Day 15 at noon PT.
* Integration testing from Day 15 to Day 17.
* Summit deployment on Day 20.

From the time that the work closes to the end of building the deployment artifacts is about one week.
The one week time-frame allows for issues to be discovered and resolved.
After the initial TTS deployment the CSC developers have about 2.5 days to react to changes in the interface.
If possible, try to inform folks of those changes ahead of time, but this is not always possible.
Integration testing is confined to three days.
The summit deployment time is always at 9 AM summit time the following Monday after the TTS deployment.

.. _vanward: https://vanward.lsst.io
