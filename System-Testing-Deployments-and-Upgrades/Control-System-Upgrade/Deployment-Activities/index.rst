Deploying the Upgrade
=====================

These are the activities that are performed when the time of deployment comes around.
You will need access to a number of resources (:ref:`Summit <Deployment-Activities-Summit-Resources>`, :ref:`TTS <Deployment-Activities-TTS-Resources>`, :ref:`BTS <Deployment-Activities-BTS-Resources>`) at the sites so be sure that you have the credentials to do so.

.. attention::

  As the person running the deployment, you have absolute control over the system to complete this process.
  No one should do anything without your express consent.

.. important::

  Upgrading systems which are controlling hardware, especially the camera CCD, cold, cryo and vacuum systems, needs to be done with care and should be coordinated with the hardware/software experts for those systems.

#. Send all CSC to ``OFFLINE`` state
    * Go to the LOVE interface for the specific site and use any of the ScriptQueues to run the ``system_wide_shutdown.py`` script (under STANDARD). This will send all CSC systems to ``OFFLINE`` state. 
    * If CSCs do not transition to ``OFFLINE`` with ``system_wide_shutdown.py``, try running ``set_summary_state.py``. An example configuration would be::

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
    
    * The Watcher MUST come down FIRST, to avoid a flurry of alarms going off.
    
    * The ScriptQueues MUST come down last.

.. _Control-System-Upgrade-Pre-Deployment-Activities-Clean-up:
#. **Clean up still running CSCs/systems**

   * To shut down the cameras, log into the ``mcm`` machines and stop the bridges using ``sudo systemctl stop`` (:ref:`Summit <Deployment-Activities-Summit-Camera-Shutdown>`, :ref:`TTS <Deployment-Activities-TTS-Camera-Shutdown>`, :ref:`BTS <Deployment-Activities-BTS-Camera-Shutdown>`).
   * One can work with the system principles to shut down the services.
   * Notify the camera upgrade team that the system is ready for :ref:`Stage 1<camera-install-stage-1>`.
   * Shut down and clean up bare metal deployments (:ref:`Summit <Deployment-Activities-Summit-TandS-BM-Shutdown>` only).
   * Clean up Kubernetes deployments:
      * Scripts are in https://github.com/lsst-ts/k8s-admin.
      * Ensure the correct cluster is set, then run::

          ./cleanup_all

      * To clean up Nublado::

          ./cleanup_nublado


#. **With everything shutdown, the configurations need to be updated before deployment starts**

   * Ensure Phalanx branch (https://github.com/lsst-sqre/phalanx) contains all the necessary updates, then create a PR and merge it.
   * All other configuration repositories should have the necessary commits already on branches and pushed to GitHub.
   * Update configuration repositories on bare metal machine deployments (:ref:`Summit <Deployment-Activities-Summit-Update-Configuration>` only).
      
      * Unlike shutdown, only the T&S systems are handled here. DM and Camera are handled by the system principles.
      * Also, only certain T&S systems are handled here, the rest need to be coordinated with system principles.

#. Once all configurations are in place, deployment of the new system can begin.
    * **Be patient with container pulling (goes for everything containerized here).**
    #. Update ESS Controllers (:ref:`Summit <Deployment-Activities-Summit-Update-ESS-Controllers>` only)
    #. Log into the site specific ArgoCD UI to sync the relevant applications:
       
       * Start by syncing ``science-platform``.
       * Sync ``nublado``.
       * Sync ``sasquatch`` if necessary, but check first, in case there are configuration changes that we don't want to apply just yet.
       * Sync T&S applications, all under the ``telescope`` ArgoCD project. While the order doesn't matter in principle, it is a good idea to start with a small application (like ``control-system-test``). It is also useful to update LOVE before the rest of the control system applications, as we can monitor the state of the different CSCs from the summary state view.
    
    #. Startup Camera Services (:ref:`Summit <Deployment-Activities-Summit-Camera-Startup>`, :ref:`TTS <Deployment-Activities-TTS-Camera-Startup>`, :ref:`BTS <Deployment-Activities-BTS-Camera-Startup>`).
       
       * This is handled by the Camera team for a Cycle upgrade, but it is done by the deployment team for a system restart.
    
    #. Use the site specific Slack channel (:ref:`Summit <Pre-Deployment-Activities-Summit-Slack-Announce>`, :ref:`TTS <Pre-Deployment-Activities-TTS-Slack-Announce>`, :ref:`BTS <Pre-Deployment-Activities-BTS-Slack-Announce>`) to notify the people doing the camera upgrade that they can proceed to :ref:`Stage 2<camera-install-stage-2>`.
    
    #. Startup Services on Bare Metal Deployments (:ref:`Summit <Deployment-Activities-Summit-TandS-BM-Startup>` only).

#. **Once the deployment steps have been executed, the system should be monitored to see if all CSCs come up into** ``STANDBY``
   
   * Some CSCs (ScriptQueues) should come up ``ENABLED``.
   * Report any issues directly to the system principles (DMs are OK).
   * This step is completed when either all CSCs are in STANDBY/OFFLINE or CSCs with issues cannot be fixed in a reasonable (~30 minutes) amount of time.
   * If leaving this step with CSCs in non-working order, make sure to report that on the site specific Slack channel.

#. Some CSCs need to be ENABLED (:ref:`Summit <Deployment-Activities-Summit-Enabled-CSCs>`, :ref:`TTS <Deployment-Activities-TTS-Enabled-CSCs>`, :ref:`BTS <Deployment-Activities-BTS-Enabled-CSCs>`).

#. If not carrying on with integration testing, folks can be told they can use Nublado again via the site specific Slack channel.


Deploying an Incremental Upgrade
================================

The process is similar to that of deploying a full upgrade, but with some key differences:

#. **Send only relevant CSCs to** ``OFFLINE`` **state**

   * Remember to send the Watcher to ``OFFLINE`` state first.
   * Use the ``set_summary_state.py`` script in LOVE to send the affected components to ``OFFLINE``.
   * The ScriptQueues should also be sent to ``OFFLINE``, as they too need to be updated to be able to interact with the interface.      
   
#. **Clean up jobs for relevant CSCs, ScriptQueues**

   * For CSCs, this can be done by logging into ``ArgoCD``, finding the job and deleting it.
   * Alternatively, and more conviniently, it can be achieved through ``kubectl``. 
      * Make sure you are in the correct cluster context and run::

         kubectl delete job -n <namespace> -l csc-class=<csc-class>

      * For example, to delete ScriptQueue jobs, you would run::

         kubectl delete job -n obssys -l csc-class=scriptqueue


#. **Once you have updated the configurations, update the relevant components only**

   * Sync the ScriptQueues and any other CSCs that need to be updated.


Recovering the Control System after an OS/K8s upgrade
================================

After IT performs a routine OS/K8s upgrade the Control Syem will need to be brought back.
In order to do this:

#. **The running Kubernetes jobs need to be cleaned.** 

#. **Sync Components**

#. **For the Summit** the cRIOs for MTM1M3, MTVMS:1, MTVMS:2 and MTM1M3TS will need to be started.
   See :ref:`Deployment-Activities-Summit-TandS-BM-Startup`.

#. **For test stands, minimal testing is required.**
   This involves tracking and taking an image using both telescopes.


Site Specific Variations
========================

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    summit/*
    tucson-teststand/*
    base-teststand/*
