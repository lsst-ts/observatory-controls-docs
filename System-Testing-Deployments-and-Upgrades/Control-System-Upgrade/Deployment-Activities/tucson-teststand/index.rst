Tucson Test Stand
=================

This section contains site specific variations for the Tucson test stand.

.. _Deployment-Activities-TTS-Resources:

Resources
---------

* LOVE: http://love1.tu.lsst.org
* LOVE (k8s): http://love.tu.lsst.org
* Argo CD: https://tucson-teststand.lsst.codes/argo-cd
* Chronograf: https://tucson-teststand.lsst.codes/chronograf
* Nublado: https://tucson-teststand.lsst.codes/
* Rancher: https://rancher.tu.lsst.org (1)
* Slack: #rubinobs-tucson-teststand

(1) Need to get kubeconfig file from here.
File a `Jira ticket <https://jira.lsstcorp.org/projects/IHS>`_ with Tucson IT for access.
Once able to log into Rancher:

#. Select the pillan cluster.
#. Click the Kubeconfig File button in top-right.
#. Near bottom of dialog, click the download link.

.. _Deployment-Activities-TTS-Non-Production:

Non-Production Systems
----------------------

The Tucson Teststand operates all CSCs and systems on the production domain.

.. _Deployment-Activities-TTS-BareMetal:

Bare Metal Machines
-------------------

* LOVE: love1.tu.lsst.org
* T&S CSCs: tel-hw1.tu.lsst.org
* Kubernetes: Can be done from own machine, just need kubeconfig file and kubectl installed.
    * Systems run on the pillan cluster.
    * Can also use: https://k8slens.dev/.
* ATCamera (Tony Johnson): auxtel-mcm.tu.lsst.org
* CCCamera (Tony Johnson): comcam-mcm.tu.lsst.org
* Calibration Systems (Erik Dennihy): loonie.tu.lsst.org

.. _Deployment-Activities-TTS-LOVE-Summary:

LOVE Summary View
-----------------

The overall system summary state view is called ``Summary State``.

.. _Deployment-Activities-TTS-Federation-Check:

Checking the Number of Federations
----------------------------------

This uses a script in https://github.com/lsst-ts/k8s-admin.
Run *./feds-check-k8s* from a machine with *kubectl* and the proper kubeconfig file.

.. _Deployment-Activities-TTS-Camera-Shutdown:

Shutdown Camera Services
-------------------------------

* Shutdown Camera OCS Bridges:
    * ATCamera: *sudo systemctl stop ats-ocs-bridge.service*
    * CCCamera: *sudo systemctl stop comcam-ocs-bridge.service*
* Shutdown Camera Daemons
    * *sudo systemctl stop opensplice.service*
    * Command is the same everywhere.

.. _Deployment-Activities-TTS-LOVE-Shutdown:

Shutdown LOVE
-------------

This needs to be done from love1.

* Uses the ``docker-compose-admin`` scripts in ``tucson-teststand/love1`` directory, which are checked out to the dco user home directory.
    * Become the dco user: *sudo -iu dco*
    * *./shutdown_love*
    * *./shutdown_daemon*

.. _Deployment-Activities-TTS-TandS-BM-Shutdown:

Shutdown T&S Bare Metal Services
--------------------------------

Handle tel-hw1:

* Uses the ``docker-compose-admin`` scripts in ``tucson-teststand/tel-hw1`` directory, which are checked out to the dco user home directory.
    * Become the dco user: *sudo -iu dco*
    * *./shutdown_atmcs_atp*
    * *./shutdown_m1m3*
    * *./shutdown_daemon*

Handle calibration systems:

Log into the machines listed in that section then stop and remove all running containers.

.. _Deployment-Activities-TTS-Kubernetes:

Interacting with Kubernetes
---------------------------

Commands can be executed from your own machine with *kubectl* and the proper kubeconfig file.

.. _Deployment-Activities-TTS-Main-Daemon-Shutdown:

Shutdown Main Daemon
--------------------

The main daemon on TTS runs on Kubernetes.
Shut it down by deleting the **deployment** under the ``ospl-main-daemon`` app on Argo CD.

.. _Deployment-Activities-TTS-Update-Configuration:

Update Configuration
--------------------

* Gather the branch for the configurations and version number for ``ts_ddsconfig``.
* Uses the ``docker-compose-admin/tucson-teststand/update_repo`` script, which is checked out to the dco user home directory.
* Repos to update:
    * ``docker-compose-ops`` (love1, tel-hw1)
    * ``LOVE-integration-tools`` (love1)
    * ``ts_ddsconfig`` (love1, tel-hw1) NOTE: Only necessary if there are updates.
* Become the dco user: *sudo -iu dco*
* *./update_repo <repo path> <branch or version>*

.. _Deployment-Activities-TTS-Main-Daemon-Startup:

Startup Main Daemon
-------------------

The main daemon on TTS runs on Kubernetes and will be handled by the *sync_apps.py* script.
This will be detailed in the next section

.. _Deployment-Activities-TTS-Minimal-K8S-System:

Startup Minimal Kubernetes System
---------------------------------

This replaces most of step 6.3 in the main document.
Follow the first three bullet points in that step and then continue the process with the next steps.

* *python sync_apps.py -p -t*
* csc-cluster-config, ospl-config and ospl-main-daemon apps will be synced automatically.
* Once the ospl-main-daemon app is synced, the script will pause.
* Check the logs on Argo CD UI to see if daemon is ready.
* Type ``go`` and enter to move onto syncing the ospl-daemon app
* Once the ospl-daemon app is synced, the script will pause.
* Check the logs on Argo CD UI to see if daemons are ready.
* Type ``go`` and enter to move onto syncing the kafka-producers app.
* Script will again pause once the kafka-producers are synced.
* The kafka-producers use a startup probe, so once all of the pods show a green heart, type ``go`` and enter to move onto syncing the love app.
* Once the love app is synced, stop here and return to step 6.4 in the main document.
* Make sure you leave the script running.

.. _Deployment-Activities-TTS-LOVE-Startup:

Startup LOVE
------------

This needs to be done from love1.

* Uses the ``docker-compose-admin`` scripts in ``tucson-teststand/love1`` directory.
    * *./launch_daemon*
    * Ensure daemon is ready before proceeding.
    * *./launch_love*

.. _Deployment-Activities-TTS-TandS-BM-Startup:

Startup T&S Bare Metal Services
-------------------------------

Handle tel-hw1

* Uses the ``docker-compose-admin`` scripts in ``tucson-teststand/tel-hw1`` directory.
    * *./launch_daemon*
    * Ensure daemon is ready before proceeding.
    * *./launch_atmcs_atp*
    * *./launch_m1m3*

.. _Deployment-Activities-TTS-Enabled-CSCs:

Enabled CSCs
------------

If proceeding with integration testing, the CSCs will be brought to ENABLED state as part of that process.
All of the startup processes maybe necessary for recovering the TTS from any maintenance.
In this case, all of the CSCs must be returned to ENABLED state.
The following components will automatically transition to ENABLED state when launched:

* WeatherForecast
* ScriptQueue:1
* ScriptQueue:2
* DSM:1
* DSM:2

For the other components, leverage the following scripts.
Required configurations will be given for each script execution.

.. note::

    Both ATCamera and CCCamera must be in OFFLINE_AVAILABLE state before putting them into ENABLED state.

* ``auxtel/enable_atcs.py``
* ``auxtel/enable_latiss.py``
* ``maintel/enable_mtcs.py``
* ``maintel/enable_comcam.py``
* ``set_summary_state.py``

  .. code:: bash

    data:
      - [ESS:1, ENABLED]
      - [ESS:101, ENABLED]
      - [ESS:102, ENABLED]
      - [ESS:103, ENABLED]
      - [ESS:104, ENABLED]
      - [ESS:105, ENABLED]
      - [ESS:201, ENABLED]
      - [ESS:202, ENABLED] 
      - [ESS:203, ENABLED]
      - [ESS:204, ENABLED]
      - [ESS:301, ENABLED]
* ``set_summary_state.py``

  .. code:: bash

    data:
      - [Scheduler:1, ENABLED]
      - [Scheduler:2, ENABLED]
      - [OCPS:1, ENABLED]
      - [OCPS:2, ENABLED]
* ``set_summary_state.py``

  .. code:: bash

    data:
      - [Watcher, ENABLED]
