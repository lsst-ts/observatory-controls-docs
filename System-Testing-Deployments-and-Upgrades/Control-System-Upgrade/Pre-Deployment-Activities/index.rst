Preparing for Deployment
========================

There are a few things that must be done before the deployment happens and while the builds of deployable artifacts are ongoing.

#. Create a Jira ticket for the cycle build configuration work.
   * The ``create_configuration_tickets`` script in the vanward_ package will create all the necessary Jira tickets.
   * Link these tickets into the appropriate cycle build Confluence page (see :ref:`Upgrading the Interface (XML) <Control-System-Upgrade-Getting-Ready-Upgrading-Interface-XML>` for details).
#. Prepare the configuration for the cycle build in the git repositories listed in :ref:`Control-System-Upgrade-Pre-Deployment-Activities-Repositories` using the Jira tickets above as the appropriate branches.
    #. Use the site specific file/directory: :ref:`Summit <Pre-Deployment-Activities-Summit-Configuration-Repos-Info>`, :ref:`TTS <Pre-Deployment-Activities-TTS-Configuration-Repos-Info>`, :ref:`BTS <Pre-Deployment-Activities-BTS-Configuration-Repos-Info>`.
    #. Update the cycle build tag.
    #. Update any changes to CSC configurations including launch command-line.
    #. Add new CSC/applications as necessary.
#. Work with build team during the build process to ensure schedule and resolve any encountered problems.
#. Announce the deployment schedule on the slack channel: :ref:`Summit <Pre-Deployment-Activities-Summit-Slack-Announce>`, :ref:`TTS <Pre-Deployment-Activities-TTS-Slack-Announce>`, :ref:`BTS <Pre-Deployment-Activities-BTS-Slack-Announce>`.
    #. Use the ``release_announcement`` script from vanward_ to craft the announcement.
    #. The announcement must go out the calendar day before the deployment.
    #. Another announcement must go out one hour before the deployment.
    #. A final announcement must go out as the deployment begins.
    #. If you want to work with the System Principles for Camera and other machines, make sure to inform them you will require their help standing down services.
#. Coordinate with SQuaRE to make sure that a new nublado with the current XML/SAL will be available for the deployment day.
    #. Make a PR for the site specific science-platform configuration here: https://github.com/lsst-sqre/phalanx.
    #. Edit the appropriate configuration file: :ref:`Summit <Pre-Deployment-Activities-Summit-RSP-Config>`, :ref:`TTS <Pre-Deployment-Activities-TTS-RSP-Config>`, :ref:`BTS <Pre-Deployment-Activities-BTS-RSP-Config>`.
    #. Notify SQuaRE when the PR is ready to merge.
    #. Syncing the ``cachemachine`` app will take place during the deployment.

.. _Control-System-Upgrade-Pre-Deployment-Activities-Repositories:

Deployment Configuration Repositories
=====================================

As noted above, following repositories contain the configuration as code.

* https://github.com/lsst-it/docker-compose-ops
* https://github.com/lsst-ts/argocd-csc
* https://github.com/lsst-ts/LOVE-integration-tools

Deployment Helper Repositories
==============================

The following repositories contain helper scripts that aid in the deployment process.
Specific uses for each repository are handled within the deployment documentation.

* https://github.com/lsst-ts/docker-compose-admin
* https://github.com/lsst-ts/k8s-admin
* `https://github.com/lsst-ts/argocd-csc/bin <https://github.com/lsst-ts/argocd-csc/tree/main/bin>`_

Site Specific Variations
========================

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    summit/*
    tucson-teststand/*
    base-teststand/*

.. _vanward: https://vanward.lsst.io
