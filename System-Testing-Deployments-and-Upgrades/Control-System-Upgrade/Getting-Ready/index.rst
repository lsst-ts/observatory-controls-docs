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


Incremental Upgrades to the Interface (XML)
===========================================

Incremental upgrades to the interface (XML) are handled similarly to full upgrades, but with some key differences:

#. They can be requested through Slack in the ``#recap-software`` channel as the need arises. The request will then proceed to be discussed in the next CAP meeting.
#. Since an incremental upgrade does not require a full Cycle build, nor the whole suite of integration tests, the time between the closure of XML work and deployment to the Summit will be shorter than that of a full Cycle upgrade. The schedule will thus depend on the amount of components updated.
#. Notes detailing the components affected, XML changes and software versions will be added to the current Cycle's confluence page. 
#. The Jira tickets tracking the relevant changes for the affected components need to be identified and kept in the current release in the Jira CAP project. The people requesting the incremental upgrade are responsible for providing the Jira ticket keys for the work that needs to be included in the upgrade.
   It is advisable to double check with folks that they have specified all necessary tickets, as it has been the case before that people forget a relevant one.
#. Once the relevant tickets have been identified, the commit SHAs associated with them need to be found so they can be included in the new release. The ``collect_ticket_commits`` in the vanward_ can help with that.
#. All XML changes not included in the incremental upgrade need to be moved to the next release in the CAP project. The ``move_bucket_ticket_links`` script in the vanward_ package can be used to take care of that.
#. Since an incremental upgrade changes the XML interface only partially, it is important to check that the changes do not break schema compatibility. See :ref:`Control-System-Upgrade-Getting-Ready-Checking-Schema-Compatibility` for further instructions.

Upgrading SAL
=============

While upgrading SAL usually coincides with an upgrade to the XML, it does not have to be the case.
An upgrade for SAL may use the previous cycle's XML version in order to limit the potential for surprises.
The primary developers (Valerie Becker, Igor Suarez-Sola) for SAL are responsible for ensuring the necessary work is completed and the new version is ready.


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
After the initial BTS deployment the CSC developers have about 2 days to react to changes in the interface. While it’s ideal to notify folks of these changes in advance, this may not always be possible.  
Integration testing is limited to three days.  
Summit deployments always occur at 9 AM summit time on the Tuesday following the BTS deployment.

.. _Control-System-Upgrade-Getting-Ready-Checking-Schema-Compatibility:

Checking Schema compatibility for an Incremental upgrade
========================================================

* To check that the changes made to the XML interface for the incremental upgrade are schema compatible, you will need to start a local Kafka Server and schema registry.
  You can do so by running::

    docker compose -f {path/to/ts_salobj}/docker-compose.yaml up -d

  This will run the ``docker-compose.yaml`` file found in the ts_salobj_ repo.

* Create a conda environment and make sure that the branches for the repos ts_xml_ and ts_salobj_ are installed::

    conda create -n schema-checker-dev pip -y
    conda activate schema-checker-dev
    cd {/path/to/ts_xml}
    pip install -e .   
    cd {/path/to/ts_salobj}
    pip install -e .

* Now you will need to build the topic_registrar container. 
  You can do by running::

    docker build . --tag ts-dockerhub.lsst.org/topic_registrar:c00{NN}

  Where ``NN`` corresponds to the cycle number. The docker file for the container is::

    ARG cycle=c00{NN}
    ARG hub=ts-dockerhub.lsst.org
    FROM ${hub}/deploy-env:${cycle}
    LABEL maintainer="Michael Reuter <mareuter@lsst.org>"
    WORKDIR /home/saluser
    RUN source /home/saluser/.setup_sal_env.sh && \
        conda install -c lsstts ts-xml={xml_version}
    COPY startup.sh /home/saluser/.startup.sh
    USER root
    RUN chown saluser:saluser /home/saluser/.startup.sh && \
        chmod a+x /home/saluser/.startup.sh
    USER saluser

  Where ``xml_version``corresponds to the version of the current relase. 
  The ``startup.sh`` file should contain::

    #!/usr/bin/env bash
    source $HOME/.setup_sal_env.sh
    create_topics --all

* Run the following script to register the topics::
  
    docker run --rm --name topic_registrar \
    --env LSST_TOPIC_SUBNAME=chk \
    --env LSST_SCHEMA_REGISTRY_URL=http://schema-registry:8081 \
    --env LSST_KAFKA_BROKER_ADDR=broker:29092 \
    --network kafka \
    --platform linux/amd64 \
    ts-dockerhub.lsst.org/topic_registrar:c00{NN}

* To generate the report of all differences found, run the following script::

    #!/usr/bin/env bash
    export LSST_TOPIC_SUBNAME=chk
    export LSST_KAFKA_BROKER_ADDR=localhost:9092
    export LSST_SCHEMA_REGISTRY_URL=http://localhost:8081
    check_schema --all
  
  The output of this script should be recorder in the Confluence page for the Cycle, under the section for the Incremental Upgrade.
  Notice that the scripts will only report when a new topic is created or an old one removed.
  It will not produce results for variables added to topics.

.. _ts_xml: https://github/lsst-ts/ts_xml
.. _ts_salobj: https://github.com/lsst-ts/ts_salobj
.. _vanward: https://vanward.lsst.io
