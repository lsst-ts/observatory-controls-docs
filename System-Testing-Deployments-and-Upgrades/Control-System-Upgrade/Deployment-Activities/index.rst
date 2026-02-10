Deploying the Upgrade
=====================

These are the activities that are performed when the time of deployment comes around.
You will need access to a number of resources (:ref:`Summit <Deployment-Activities-Summit-Resources>`, :ref:`TTS <Deployment-Activities-TTS-Resources>`, :ref:`BTS <Deployment-Activities-BTS-Resources>`) at the sites so be sure that you have the credentials to do so.

.. attention::

  As the person running the deployment, you have absolute control over the system to complete this process.
  No one should do anything without your express consent.

.. important::

  Upgrading systems which are controlling hardware, especially the camera CCD, cold, cryo and vacuum systems, needs to be done with care and should be coordinated with the hardware/software experts for those systems.

.. important::

   If deploying the upgrade to the Summit, before shutting down the Control System, make sure that M2 is switched to closed loop control from the EUI. You should ask for help with this in ``#summit-simonyitel`` beforehand.
   In the case of an OS/k8s upgrade, ensure that the M2 CSC is back into ``ENABLED`` state before rebooting the Hexrot VM (where the EUI for M2 runs), otherwise it will go out of closed loop again.

.. important::

   If deploying the upgrade to the Summit, keep MTM1M3TS in ENABLED state and MTM1M3 in DISABLED state. This will be fixed at some point.
   The same goes for OS/k8s upgrades.

#. Send all CSC to ``OFFLINE`` state
    * Go to the LOVE interface for the specific site and use any of the ScriptQueues to run the ``system_wide_shutdown.py`` script (under STANDARD). This will send all CSC systems to ``OFFLINE`` state. 
    * The ScriptQueues (and any other CSC that fails to transition to ``OFFLINE``state) need to be shut down using the ``set_summary_state.py`` script. Assuming the script is run using ``MTQueue``, use the following configuration::

        data:
        - [ScriptQueue:3, OFFLINE]
        - [ScriptQueue:2, OFFLINE]
        - [ScriptQueue:1, OFFLINE]
        mute_alarms: false

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
    
    * The ScriptQueues MUST come down last, taking care that the order in the script's configuration shuts down the ScriptQueue where the script is run last.


.. _Control-System-Upgrade-Pre-Deployment-Activities-Clean-up:

#. **Clean up still running CSCs/systems**

   * To shut down the cameras, log into the ``mcm`` machines and stop the bridges using ``sudo systemctl stop`` (:ref:`Summit <Deployment-Activities-Summit-Camera-Shutdown>`, :ref:`TTS <Deployment-Activities-TTS-Camera-Shutdown>`, :ref:`BTS <Deployment-Activities-BTS-Camera-Shutdown>`).
   * One can work with the system principles to shut down the services.
   * Notify the camera upgrade team that the system is ready for :ref:`Stage 1<camera-install-stage-1>`.
   * Shut down and clean up bare metal deployments (:ref:`Summit <Deployment-Activities-Summit-TandS-BM-Shutdown>` only).
   * Clean up Kubernetes deployments:
      * To do this you will need to point to the correct Kubernetes cluster for each site (:ref:`Summit <Deployment-Activities-Summit-Kubernetes>`, :ref:`TTS <Deployment-Activities-TTS-Kubernetes>`, :ref:`BTS <Deployment-Activities-BTS-Kubernetes>` )
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


#. In the case that the changes to be applied break schema compatibility, it will be necessary to change the schema registry compatibility setting. To do so:

   * Exec into a schema registry pod.
   * Check the current setting, which should be ``FORWARD``::
      
      curl $SCHEMA_REGISTRY_LISTENERS/config 
   
   * Change the setting to ``NONE`` by doing::

      curl -s -X PUT -H 'Content-Type: application/vnd.schemaregistry.v1+json' --data '{  "compatibility": "NONE" }' $SCHEMA_REGISTRY_LISTENERS/config

   * Remember to change the compatibility setting back to ``FORWARD`` later.


#. Once all configurations are in place, deployment of the new system can begin.
    
    * **Be patient with container pulling (goes for everything containerized here).**

    #. Update ESS Controllers (:ref:`Summit <Deployment-Activities-Summit-Update-ESS-Controllers>` only)
    #. Update cRIOs if not done already (:ref:`Summit <Deployment-Activities-Summit-Update-cRIOs>` only)
    #. Log into the site specific ArgoCD UI to sync the relevant applications:
       
       * Start by syncing ``science-platform``.
       * Sync ``nublado``.
       * Sync ``sasquatch`` if necessary, but check first, in case there are configuration changes that we don't want to apply just yet.
       * Sync T&S applications, all under the ``telescope`` ArgoCD project. While the order doesn't matter in principle, it is a good idea to start with a small application (like ``control-system-test``). It is also useful to update LOVE before the rest of the control system applications, as we can monitor the state of the different CSCs from the summary state view.
    
    #. Startup Camera Services (:ref:`Summit <Deployment-Activities-Summit-Camera-Startup>`, :ref:`TTS <Deployment-Activities-TTS-Camera-Startup>`, :ref:`BTS <Deployment-Activities-BTS-Camera-Startup>`).
       
       * This is generally handled by the Camera team.
    
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
   * Alternatively, and more conviniently, it can be achieved through ``kubectl``. Be sure to point to the correct cluster (:ref:`Summit <Deployment-Activities-Summit-Kubernetes>`, :ref:`BTS <Deployment-Activities-BTS-Kubernetes>`,  :ref:`TTS <Deployment-Activities-TTS-Kubernetes>` ).
      * Make sure you are in the correct cluster context and run::

         kubectl delete job -n <namespace> -l csc-class=<csc-class>

      * For example, to delete ScriptQueue jobs, you would run::

         kubectl delete job -n obssys -l csc-class=scriptqueue


#. **Once you have updated the configurations, update the relevant components only**

   * Sync the ScriptQueues and any other CSCs that need to be updated.

#. **For test stands, minimal testing is required.**
   See further information in (:ref:`Control-System-Upgrade-Deployment-Activities-Minimal-Testing`)


Recovering the Control System after an OS/K8s upgrade
=====================================================

After IT performs a routine OS/K8s upgrade the Control System will need to be brought back.
In order to do this:

#. **The running Kubernetes jobs need to be cleaned.** 

#. **Sync Components**

#. **For the Summit** 

   * The cRIOs for MTM1M3, MTVMS:1, MTVMS:2 and MTM1M3TS will need to be started. See last step in :ref:`Deployment-Activities-Summit-Update-cRIOs`.
   * The CSCs on ``azar03.cp.lsst.org`` will need to be restarted.
   * ``azar02.cp.lsst.org`` will need to be rebooted. 

#. **For test stands, minimal testing is required.**
   See further information in :ref:`Control-System-Upgrade-Deployment-Activities-Minimal-Testing`.


.. _Control-System-Upgrade-Deployment-Activities-Minimal-Testing:

Minimal Testing
===============

#. In the case of an OS/K8s upgrades, both telescopes need to be tested to ensure they are able to track and take images.
#. In the case of an Incremental Upgrade:

   * It is important to ensure that all the new topics (if any) were created. This can be done both through Kafdrop and by looking at the logs in the ``schema-registry`` pod in ``sasquatch``.
   * The CSCs affected should be cycled through states, to ensure that they don't go into ``FAULT`` and that the correct topics get populated.
   * If components in either of the telescopes were affected, it is necessary to test that the one that was updated can still track and take images.


#. To get AT to track and take images:

   * Run ``auxtel/enable_atcs.py`` in LOVE.
   * Run ``auxtel/enable_lattis.py``.
   * Run ``auxtel_housekeeping.py``. This can be done either through nublado or through ``argo-workflows``.
   * Load the playlist. You can do this by running the ``run_command.py`` script in LOVE with the following configuration::

      component: ATCamera
      cmd: play
      parameters:
         playlist: bias
         repeat: true

   * Run ``auxtel/prepare_for/onsky.py``.
   * Run ``auxtel/track_target.py``. One possible configuration is::

      slew_icrs:
      dec: -20
      ra: 18

   * Run ``auxtel/take_image_latiss.py``. One possible configuration is::

      nimages: 5
      image_type: BIAS
      program: IntegrationTesting
      reason: minimal_testing 

   * Ensure that the images have been properly ingested. You can do this in Chronograf by checking the ``LATISS Exposure Table``, ``LATISS Header Status``and ``LATISS OODS ingest status`` dashboards.

   * Remember to run ``auxtel/stop_tracking.py`` after.

   * Once the testing is done, run ``auxtel/standby_atcs.py`` to leave the test stand in its default state.

#. To get MT to track and take images:

   * Run ``maintel/enable_atcs.py`` in LOVE.
   * Run ``maintel/enable_lsstcam.py``.
   * Run ``maintel_housekeeping.py``. This can be done either through nublado or through ``argo-workflows``.
   * Load the playlist. You can do this by running the ``run_command.py`` script in LOVE with the following configuration::

      component: MTCamera
      cmd: play
      parameters:
         playlist: lsstcam-20250530
         repeat: true

   * Run ``maintel/home_both_axes.py``
   * Run ``maintel/enable_hexapod_compensation_mode.py``
   * Run ``maintel/mtdome/open_dome.py``
   * Run ``maintel/mtdome/enable_dome_following.py``
   * Run ``maintel/m1m3/raise_m1m3.py``. In the test stands this script will not work at low elevations (it will hang). If this happens, use ``point_azel.py`` to bring it to 80 degrees elevation. 
   * Run ``maintel/track_target.py``. One possible configuration is::

      target_name: HD164461
      rot_value: 80.0
      rot_type: PhysicalSky
      track_for: 30

   * Run ``maintel/take_image_lsstcam.py``. One possible configuration is::

      exp_times: 30
      nimages: 5
      image_type: "ACQ"
      reason: minimal_testing

   * Ensure that the images have been properly ingested. You can do this in Chronograf by checking the ``LSSTCam Exposure Table``, ``LSSTCam Header Status``and ``LSSTCam OODS ingest status`` dashboards.
   * Ensure that there are no retrieval failures in RubinTV.
   * Remember to run ``maintel/stop_tracking.py`` or ``maintel/csc_end_of_night.py``.

#. There are some site specific variations (:ref:`TTS <Deployment-Activities-TTS-Minimal-Testing>`).



.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    summit/*
    tucson-teststand/*
    base-teststand/*
