Deploying the Upgrade
=====================

These are the activities that are performed when the time of deployment comes around.
You will need access to a number of resources (:ref:`Summit <Deployment-Activities-Summit-Resources>`, :ref:`TTS <Deployment-Activities-TTS-Resources>`, :ref:`BTS <Deployment-Activities-BTS-Resources>`) at the sites so be sure that you have the credentials to do so.
.. A number of scripts are available for easing the bare metal docker-compose deployment handling.
.. The scripts can be retrieved from this repo: https://github.com/lsst-ts/docker-compose-admin.
.. Use the scripts from the appropriate site directory.
.. If changes are necessary to these scripts from work described in the previous section, use the appropriate site Jira ticket.

.. attention::

  As the person running the deployment, you have absolute control over the system to complete this process.
  No one should do anything without your express consent.

.. important::

  Upgrading systems which are controlling hardware, especially the camera CCD, cold, cryo and vacuum systems, needs to be done with care and should be coordinated with the hardware/software experts for those systems.

#. Go to the LOVE interface for the specific site and use any of the ScriptQueues to run the ``system_wide_shutdown.py`` script (under STANDARD). This will send all CSC systems to ``OFFLINE`` state.

    * If CSCs do not transition to ``OFFLINE`` with ``system_wide_shutdown.py``, try running ``set_summary_state.py``. An example configuration would be:
        .. code:: bash
            data:
            - [ESS:118, OFFLINE]
    * **WARNING**: Not all CSCs report ``OFFLINE``; these will instead report ``STANDBY`` as the last state seen. To check that they are indeed ``OFFLINE`` check for heartbeats using Chronograf.
    * It is recommended to use LOVE for this, but if it's not working, Nublado is a good fallback.
    * An overall status view is available from LOVE in the Summary state view (:ref:`Summit <Deployment-Activities-Summit-LOVE-Summary>`, :ref:`TTS <Deployment-Activities-TTS-LOVE-Summary>`, :ref:`BTS <Deployment-Activities-BTS-LOVE-Summary>`).
    * You can also consult these dashboards on Chronograf. The names are the same across sites.
        * ``Heartbeats``
        * ``AT Summary State Monitor``
        * ``MT Summary State Monitor``
        * ``Envsys Summary State Monitor``
        * ``Calibration Systems Summary State Monitor``
        * ``Observatory Systems Summary State Monitor``
    * The Watcher should come down FIRST, to avoid a flurry of alarms going off.
    * The ScriptQueues MUST come down last.

#. Once all systems are in OFFLINE, still running CSCs/systems need to be cleaned up.
    #. To shut down the cameras, it is necessary to log into the ``mcm`` machines and stop the bridges using ``sudo systemctl stop`` (:ref:`Summit <Deployment-Activities-Summit-Camera-Shutdown>`, :ref:`TTS <Deployment-Activities-TTS-Camera-Shutdown>`, :ref:`BTS <Deployment-Activities-BTS-Camera-Shutdown>`).
        * One can work with the system principles to shutdown the services.
        * Notify people doing the camera upgrade that the system is ready for them to proceed with :ref:`Stage 1<camera-install-stage-1>`.
    #. Shutdown and Cleanup Bare Metal Deployments (:ref:`Summit <Deployment-Activities-Summit-TandS-BM-Shutdown>`, :ref:`TTS <Deployment-Activities-TTS-TandS-BM-Shutdown>`, :ref:`BTS <Deployment-Activities-BTS-TandS-BM-Shutdown>`).
    #. Cleanup Kubernetes Deployment.
        * Below uses scripts in this repo: https://github.com/lsst-ts/k8s-admin.
        * Execute the following to clean up all T&S running jobs(:ref:`Summit <Deployment-Activities-Summit-Kubernetes>`, :ref:`TTS <Deployment-Activities-TTS-Kubernetes>`, :ref:`BTS <Deployment-Activities-BTS-Kubernetes>`):
            ``./cleanup_all``
        * To clean up Nublado, run:
            ``./cleanup_nublado``
#. With everything shutdown, the configurations need to be updated before deployment starts.
    * Ensure Phalanx branch (https://github.com/lsst-sqre/phalanx) contains all the necessary updates, then create a PR and merge it.
    * All other configuration repositories should have the necessary commits already on branches and pushed to GitHub.
    * Update configuration repositories on bare metal machine deployments (:ref:`Summit <Deployment-Activities-Summit-Update-Configuration>` only).
        * Unlike shutdown, only the T&S systems are handled here. DM and Camera are handled by the system principles.
        * Also, only certain T&S systems are handled here, the rest need to be coordinated with system principles.
#. Once all configurations are in place, deployment of the new system can begin.
    * Be patient with container pulling (goes for everything containerized here).
    #. Update ESS Controllers (:ref:`Summit <Deployment-Activities-Summit-Update-ESS-Controllers>` only)
    #. Log into the site specific ArgoCD UI to sync the relevant applications:
        * Start by syncing ``science-platform``.
        * If told to do so beforehand, sync ``nublado``.
        * Sync ``sasquatch`` if necessary, but check first, in case there are configuration changes that we don't want to apply just yet.
        * Sync T&S applications, all under the ``telescope`` ArgoCD project. While the order doesn't matter in principle, it is a good idea to start with a small application (like ``control-system-test``). It is also useful to update LOVE before the rest of the control system applications, as we can monitor the state of the different CSCs from the summary state view.
    #. Startup Camera Services (:ref:`Summit <Deployment-Activities-Summit-Camera-Startup>`, :ref:`TTS <Deployment-Activities-TTS-Camera-Startup>`, :ref:`BTS <Deployment-Activities-BTS-Camera-Startup>`).
        * This is done by the deployment team for a system restart, but is handled by the Camera team for a Cycle upgrade.
    #. Use the site specific Slack channel (:ref:`Summit <Pre-Deployment-Activities-Summit-Slack-Announce>`, :ref:`TTS <Pre-Deployment-Activities-TTS-Slack-Announce>`, :ref:`BTS <Pre-Deployment-Activities-BTS-Slack-Announce>`) to notify the people doing the camera upgrade that they can proceed to :ref:`Stage 2<camera-install-stage-2>`.
    #. Startup Services on Bare Metal Deployments (:ref:`Summit <Deployment-Activities-Summit-TandS-BM-Startup>` only).
#. Once the deployment steps have been executed, the system should be monitored to see if all CSCs come up into ``STANDBY``. 
    * Some CSCs (Script Queues) should come up ``ENABLED``.
    * Report any issues directly to the system principles (DMs are OK).
    * This step is completed when either all CSCs are in STANDBY/OFFLINE or CSCs with issues cannot be fixed in a reasonable (~30 minutes) amount of time.
    * If leaving this step with CSCs in non-working order, make sure to report that on the site specific Slack channel.
#. Some CSCs need to be ENABLED (:ref:`Summit <Deployment-Activities-Summit-Enabled-CSCs>`, :ref:`TTS <Deployment-Activities-TTS-Enabled-CSCs>`, :ref:`BTS <Deployment-Activities-BTS-Enabled-CSCs>`).
#. If not carrying on with integration testing, folks can be told they can use Nublado again via the site specific Slack channel.

Site Specific Variations
========================

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    summit/*
    tucson-teststand/*
    base-teststand/*
