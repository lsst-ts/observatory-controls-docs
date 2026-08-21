########
Upgrades
########

Use this page as the operational checklist for a control-system deployment or
an OS/K8s maintenance window. The detailed :ref:`Control System Upgrade
<Control-System-Upgrade-Getting-Ready>` guide remains the source of truth for
builds, configurations, camera work, Kafka, and exceptional recovery.

An upgrade changes CSC interfaces provided by ``ts_xml``. A full upgrade is a
Cycle release; an incremental upgrade changes a limited, schema-compatible set
of interfaces between Cycle releases. OS/K8s maintenance is not an interface
upgrade, but it requires the same careful shutdown and recovery.

Before you begin
^^^^^^^^^^^^^^^^

#. Confirm the deployment schedule, scope, affected CSCs, and system owners.
#. Ensure local ``k8s-admin`` and ``vanward`` checkouts are current.
#. Verify access to the site's Kubernetes cluster, LOVE, Argo CD, Argo
   Workflows, Chronograf, and Slack channel.
#. For a release, confirm configuration changes are merged. For an incremental
   XML release, confirm schema compatibility.
#. Announce in the site Slack channel with the appropriate ``vanward`` helper:
   ``release_announcement`` for a full release or
   ``incremental_release_announcement`` for an incremental release. Announce
   the day before, one hour before, and at deployment start.
#. Select the site, then follow exactly one checklist below.

.. tab-set::

   .. tab-item:: BTS

      BTS uses the Base test stand (``manke`` Kubernetes context). Notify
      ``#base-teststand`` before starting.

      .. rubric:: Full upgrade

      #. :ref:`Shut down the control system
         <Control-System-Upgrade-Deployment-Activities-Shutdown>` in LOVE by
         running ``system_wide_shutdown.py`` from a ScriptQueue. Bring the
         Watcher down first and ScriptQueues down last. Verify CSC states and
         VM heartbeats in LOVE and Chronograf.
      #. :ref:`Stop the camera bridges
         <Deployment-Activities-BTS-Camera-Shutdown>`:

         .. code-block:: bash

            # On auxtel-mcm.ls.lsst.org
            sudo systemctl stop ats-ocs-bridge.service

            # On lsstcam-mcm.ls.lsst.org
            sudo systemctl stop ocs-bridge.service

      #. :ref:`Drain LOVE-producer and Telegraf consumer lag and clean up
         deployments <Control-System-Upgrade-Deployment-Activities-Cleanup>`.
         Set the :ref:`BTS Kubernetes context <Deployment-Activities-BTS-Kubernetes>`,
         run ``cleanup_all`` from ``k8s-admin``, clean up Nublado if required,
         and scale Telegraf connectors to zero:

         .. code-block:: bash

            ./cleanup_all
            ./cleanup_nublado  # only when required
            kubectl scale deploy -n sasquatch \
              --selector app.kubernetes.io/name=sasquatch-telegraf --replicas=0

      #. :ref:`Coordinate configuration and camera updates
         <Control-System-Upgrade-Deployment-Activities-Configuration>` with
         the responsible teams. Use the detailed guide for schema-registry
         compatibility or camera-stage changes.
      #. :ref:`In Argo CD, sync LOVE first
         <Control-System-Upgrade-Deployment-Activities-Deploy>` to start the
         LOVE producers required for CSCs to appear in LOVE. Then sync
         ``science-platform``, ``nublado``, and ``sasquatch`` if needed, then
         telescope applications, starting with a small application.
      #. :ref:`Start the camera bridges
         <Deployment-Activities-BTS-Camera-Startup>`:

         .. code-block:: bash

            sudo systemctl start ats-ocs-bridge.service
            sudo systemctl start ocs-bridge.service

      #. Confirm CSCs reach ``STANDBY`` (except expected enabled CSCs),
         :ref:`restore required enabled CSCs <Deployment-Activities-BTS-Enabled-CSCs>`
         scale Telegraf connectors back to one, and verify EFD ingestion in
         Chronograf.
      #. Run :ref:`minimal testing <Control-System-Upgrade-Deployment-Activities-Minimal-Testing>`
         for AuxTel and SimonyiTel when applicable. Return each tested
         telescope to its documented safe end state.

      .. rubric:: Incremental upgrade

      #. Send the Watcher, every affected CSC, and the ScriptQueues to
         ``OFFLINE`` with ``set_summary_state.py`` in LOVE.
      #. Set the :ref:`BTS Kubernetes context <Deployment-Activities-BTS-Kubernetes>`
         and :ref:`delete jobs only for affected CSCs
         <Control-System-Upgrade-Deployment-Activities-Incremental>`:

         .. code-block:: bash

            kubectl delete job -n <namespace> -l csc-class=<csc-class>

      #. :ref:`Update the necessary configuration
         <Control-System-Upgrade-Deployment-Activities-Incremental>`, then
         sync LOVE first, followed by the ScriptQueues and affected
         applications in Argo CD.
      #. Confirm new topics, if any, were created; cycle affected CSCs through
         their states; and confirm expected topic traffic with no ``FAULT``.
      #. If a telescope CSC changed, verify it can track and take images and
         that the images are ingested.

      .. rubric:: OS/K8s maintenance

      #. :ref:`Bring down the control system as for a full upgrade
         <Control-System-Upgrade-Deployment-Activities-OS-K8s>`, including
         camera bridges, stopped-job cleanup, drained consumer lag, and
         Telegraf at zero replicas.
      #. From ``k8s-admin``, run ``./cleanup_all`` and then
         ``./shutdown_kafka``. Monitor the shutdown, tell IT when the system
         is ready, and wait for maintenance to finish.
      #. From ``k8s-admin``, run ``./start_kafka``. Verify Kafka brokers,
         controllers, schema registry, and Telegraf are healthy.
      #. Sync LOVE first, then telescope namespaces in Argo CD; restart camera
         bridges; and confirm CSC and EFD health.
      #. Run BTS minimal testing for both telescopes.

   .. tab-item:: TTS

      TTS uses the Tucson test stand (``pillan`` Kubernetes context). Notify
      ``#tucson-teststand`` before starting.

      .. rubric:: Full upgrade

      #. :ref:`Shut down the control system
         <Control-System-Upgrade-Deployment-Activities-Shutdown>` in LOVE by
         running ``system_wide_shutdown.py`` from a ScriptQueue. Bring the
         Watcher down first and ScriptQueues down last. Verify CSC states and
         VM heartbeats in LOVE and Chronograf.
      #. :ref:`Stop the camera bridges
         <Deployment-Activities-TTS-Camera-Shutdown>`:

         .. code-block:: bash

            # On auxtel-mcm.tu.lsst.org
            sudo systemctl stop ats-ocs-bridge.service

            # On comcam-mcm.tu.lsst.org
            sudo systemctl stop comcam-ocs-bridge.service

      #. :ref:`Drain LOVE-producer and Telegraf consumer lag and clean up
         deployments <Control-System-Upgrade-Deployment-Activities-Cleanup>`.
         Set the :ref:`TTS Kubernetes context <Deployment-Activities-TTS-Kubernetes>`,
         run ``./cleanup_all`` from ``k8s-admin``, clean up Nublado if
         required, and scale Telegraf connectors to zero.
      #. :ref:`Coordinate configuration and camera updates
         <Control-System-Upgrade-Deployment-Activities-Configuration>` with
         responsible teams. Use the detailed guide for schema-registry
         compatibility or camera-stage changes.
      #. :ref:`In Argo CD, sync LOVE first
         <Control-System-Upgrade-Deployment-Activities-Deploy>` to start the
         LOVE producers required for CSCs to appear in LOVE. Then sync
         ``science-platform``, ``nublado``, and ``sasquatch`` if needed, then
         telescope applications, starting with a small application.
      #. :ref:`Start the camera bridges
         <Deployment-Activities-TTS-Camera-Startup>`:

         .. code-block:: bash

            sudo systemctl start ats-ocs-bridge.service
            sudo systemctl start comcam-ocs-bridge.service

      #. Confirm CSCs reach expected states, restore required enabled CSCs,
         scale Telegraf connectors back to one, and verify EFD ingestion.
      #. Perform TTS minimal testing. Current documentation states that neither
         camera can take images at TTS, so verify tracking only.

      .. rubric:: Incremental upgrade

      #. Send the Watcher, every affected CSC, and the ScriptQueues to
         ``OFFLINE`` with ``set_summary_state.py`` in LOVE.
      #. Set the :ref:`TTS Kubernetes context <Deployment-Activities-TTS-Kubernetes>`
         and :ref:`delete jobs only for affected CSCs
         <Control-System-Upgrade-Deployment-Activities-Incremental>`:

         .. code-block:: bash

            kubectl delete job -n <namespace> -l csc-class=<csc-class>

      #. :ref:`Update the necessary configuration
         <Control-System-Upgrade-Deployment-Activities-Incremental>`, then
         sync LOVE first, followed by the ScriptQueues and affected
         applications in Argo CD.
      #. Confirm new topics, if any, were created; cycle affected CSCs through
         their states; and confirm expected topic traffic with no ``FAULT``.
      #. If a telescope CSC changed, verify it can track. Do not require
         imaging until the TTS camera limitation is resolved.

      .. rubric:: OS/K8s maintenance

      #. :ref:`Bring down the control system as for a full upgrade
         <Control-System-Upgrade-Deployment-Activities-OS-K8s>`, including
         camera bridges, stopped-job cleanup, drained consumer lag, and
         Telegraf at zero replicas.
      #. From ``k8s-admin``, run ``./cleanup_all`` and then
         ``./shutdown_kafka``. Monitor the shutdown, tell IT when the system
         is ready, and wait for maintenance to finish.
      #. From ``k8s-admin``, run ``./start_kafka``. Verify Kafka brokers,
         controllers, schema registry, and Telegraf are healthy.
      #. Sync LOVE first, then telescope namespaces in Argo CD; restart camera
         bridges; and confirm CSC and EFD health.
      #. Verify tracking for both TTS telescopes.

   .. tab-item:: Summit

      The Summit uses the ``yagan`` Kubernetes context. Notify
      ``#summit-announce`` before starting.

      .. important::

         Before a full upgrade or OS/K8s maintenance, coordinate with the
         hardware teams: M2 must be in closed-loop control, ``MTM1M3TS`` must
         remain ``ENABLED``, and ``MTM1M3`` must remain ``DISABLED``.

      .. rubric:: Full upgrade

      #. :ref:`Shut down the control system
         <Control-System-Upgrade-Deployment-Activities-Shutdown>` in LOVE by
         running ``system_wide_shutdown.py`` from a ScriptQueue, using the
         documented Summit exclusions for ``MTM1M3`` and ``MTM1M3TS``. Bring
         the Watcher down first and ScriptQueues down last. Verify CSC states
         and VM heartbeats in LOVE and Chronograf.
      #. :ref:`Stop the ATCamera and MTCamera bridges
         <Deployment-Activities-Summit-Camera-Shutdown>`. :ref:`Stop additional
         Summit bare-metal T&S services <Deployment-Activities-Summit-TandS-BM-Shutdown>`
         as required.
      #. :ref:`Drain LOVE-producer and Telegraf consumer lag and clean up
         deployments <Control-System-Upgrade-Deployment-Activities-Cleanup>`.
         Set the :ref:`Summit Kubernetes context <Deployment-Activities-Summit-Kubernetes>`,
         run ``./cleanup_all`` from ``k8s-admin``, clean up Nublado if
         required, and scale Telegraf connectors to zero.
      #. Coordinate camera, :ref:`bare-metal
         <Deployment-Activities-Summit-Update-Configuration>`, :ref:`ESS-controller
         <Deployment-Activities-Summit-Update-ESS-Controllers>`, and :ref:`cRIO
         <Deployment-Activities-Summit-Update-cRIOs>` updates with their owners.
      #. :ref:`In Argo CD, sync LOVE first
         <Control-System-Upgrade-Deployment-Activities-Deploy>` to start the
         LOVE producers required for CSCs to appear in LOVE. Then sync
         ``science-platform``, ``nublado``, and ``sasquatch`` if needed, then
         telescope applications, starting with a small application.
      #. :ref:`Start camera <Deployment-Activities-Summit-Camera-Startup>` and
         :ref:`required bare-metal services
         <Deployment-Activities-Summit-TandS-BM-Startup>`. Confirm CSCs reach
         expected states, :ref:`restore required enabled CSCs
         <Deployment-Activities-Summit-Enabled-CSCs>`, restore Telegraf to one
         replica, and verify EFD ingestion.
      #. Run :ref:`minimal testing <Control-System-Upgrade-Deployment-Activities-Minimal-Testing>`
         for affected telescopes, including image-ingest checks where imaging
         is performed. Return each telescope to its documented safe end state.

      .. rubric:: Incremental upgrade

      #. Send the Watcher, every affected CSC, and the ScriptQueues to
         ``OFFLINE`` with ``set_summary_state.py`` in LOVE.
      #. Set the :ref:`Summit Kubernetes context
         <Deployment-Activities-Summit-Kubernetes>` and :ref:`delete jobs only
         for affected CSCs <Control-System-Upgrade-Deployment-Activities-Incremental>`:

         .. code-block:: bash

            kubectl delete job -n <namespace> -l csc-class=<csc-class>

      #. :ref:`Update the necessary configuration
         <Control-System-Upgrade-Deployment-Activities-Incremental>`, then
         sync LOVE first, followed by the ScriptQueues and affected
         applications in Argo CD.
      #. Confirm new topics, if any, were created; cycle affected CSCs through
         their states; and confirm expected topic traffic with no ``FAULT``.
      #. If a telescope CSC changed, verify it can track and take images and
         that the images are ingested.

      .. rubric:: OS/K8s maintenance

      #. :ref:`Bring down the control system as for a full upgrade
         <Control-System-Upgrade-Deployment-Activities-OS-K8s>`, preserving the
         M2 and M1M3 states above. Do not shut down Summit ESS controllers for
         routine OS/K8s work.
      #. From ``k8s-admin``, run ``./cleanup_all`` and then
         ``./shutdown_kafka``. Monitor the shutdown, notify IT, and wait for
         maintenance to finish.
      #. From ``k8s-admin``, run ``./start_kafka``. Verify Kafka brokers,
         controllers, schema registry, and Telegraf are healthy.
      #. Sync LOVE first, then telescope namespaces in Argo CD. Start
         :ref:`documented Summit cRIO services
         <Deployment-Activities-Summit-Update-cRIOs>` and restart CSCs on
         ``azar03.cp.lsst.org``.
      #. Restore Telegraf to one replica, verify CSC and EFD health, and run
         Summit minimal testing for both telescopes.

Further detail
^^^^^^^^^^^^^^

Use the detailed :doc:`deployment activities
<Control-System-Upgrade/Deployment-Activities/index>` and its site-specific
sections for recovery steps, Kubernetes access, camera coordination, and
minimal-test configurations. Report any CSC that cannot be restored promptly
in the appropriate site Slack channel before ending the deployment.
