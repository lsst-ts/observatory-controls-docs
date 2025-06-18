.. _Control-System-Upgrade-Getting-Ready-Upgrading-Interface-XML:

Upgrading the Interface (XML)
=============================

#. Coordinate with major stakeholders at the Commissioning Activities Planning (CAP) meeting to discuss the upcoming release.
#. Determine the summit deployment date and work backwards to set the XML work closure deadline.
    * Consider observing runs and special overnight work at the observatory.
    * Typically allow about two weeks between work closure and deployment.
    * This period may be extended if extra testing or other circumstances require it.
    * See :ref:`Control-System-Upgrade-Getting-Ready-Setting-Schedule` for further instructions.
    * Once the deployment date is set, run the ``create_summit_upgrade_ticket`` script in the vanward_ package to create the appropriate Jira ticket.
#. Create a cycle build Confluence page (`Software Upgrades <https://confluence.lsstcorp.org/pages/viewpage.action?spaceKey=LSSTCOM&title=Software+Upgrades>`_) listing core package versions and any operational changes.
#. Present the schedule at the CAP meeting at least one week before the work closure deadline.
#. Review the release in the `CAP Jira project <https://rubinobs.atlassian.net/projects/CAP?selectedItem=com.atlassian.jira.jira-projects-plugin%3Arelease-page>`_, identified by the label ``ts_xml X.Y``.
    * Use the ``release_tickets`` script from the vanward_  package.
#. Confirm all merged work in the `ts_xml <https://github.com/lsst-ts/ts_xml.git>`_ repository is linked to a Jira ticket in the release.
    * Folks should be following the `XML Work Reporting <https://tssw-developer.lsst.io/development-guidelines/xml/reporting-xml-release-work.html#reporting-xml-release-work>`_ procedure.
    * Use the ``find_merges_without_release_tickets`` script in the vanward_ package.
#. Send reminders about the work closure deadline at least one day prior AND on the day of the deadline.
#. Ensure all work tickets are closed when the deadline passes (use the Step 5 script).
#. Work with the Telescope and Site Build Engineer on the day of the artifact build to go over any potentially open work and sign off on all software versions being used.
#. For **incremental upgrades**, use the ``move_bucket_ticket_links`` script in the vanward_ package to transfer changes not included in the mini update to the next full release cycle.


Upgrading SAL
=============

While upgrading SAL usually coincides with an upgrade to the XML, it does not have to be the case.
An upgrade for SAL may use the previous cycle's XML version in order to limit the potential for surprises.
The primary developers (Valerie Becker, Igor Suarez-Sola) for SAL is responsible for ensuring the necessary work is completed and the new version is ready.


Upgrading Kafka
==========================

Upgrading the communication backplane via updating the Kafka version requires care and extra lead time.
The Kafka oversight committee (Tiago Ribeiro, Michael Reuter) will make the determination if a new version of Kafka is ready for incorporation into a new cycle.
This determination requires dedicated testing from the main members of committee to ensure readiness.
Cycle builds upgrading Kafka have longer testing periods split into two phases.
The first phase builds a smaller section of the control system components and deploys them for testing on the TTS.
Work is done to ensure that this small system is operating within the normal parameters.
The second phase happens when the full system is built as part of the standard deployment operations.


.. _Control-System-Upgrade-Getting-Ready-Setting-Schedule:

Setting a Schedule for a full Cycle upgrade
=============================================

While below is an example, use your best judgment to set dates and make sure the major stakeholders are informed of the schedule by the CAP meeting.

* **Day 1:** Close of release work.  
* **Days 2–3:** Build artifacts (RPMs/JARs).  
* **Days 4–10:** Build conda packages and deployment artifacts.  
* **Day 13:** Initial deployment to BTS.  
* **By Day 15 (9 AM PT):** All CSCs available on BTS.  
* **Days 15–17:** Integration testing.  
* **Day 20:** Summit deployment.

It takes roughly one week from work closure to finishing the deployment artifacts, allowing time to identify and resolve problems.
After the initial BTS deployment the CSC developers have about 2.5 days to react to changes in the interface. While it’s ideal to notify folks of these changes in advance, this may not always be possible.  
Integration testing is limited to three days.  
Summit deployments always occur at 9 AM summit time on the Tuesday following the BTS deployment.

.. _vanward: https://vanward.lsst.io
