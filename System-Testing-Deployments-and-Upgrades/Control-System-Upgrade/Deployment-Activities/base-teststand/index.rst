Base Test Stand
=================

This section contains site specific variations for the Base test stand.

.. _Deployment-Activities-BTS-Resources:

Resources
---------

* LOVE (k8s): http://love01.ls.lsst.org
* Argo CD: https://base-lsp.lsst.codes/argo-cd
* Chronograf: https://base-lsp.lsst.codes/chronograf
* Nublado: https://base-lsp.lsst.codes/
* Rancher: https://rancher.ls.lsst.org (1)
* Slack: #rubinobs-base-teststand

(1) Need to get kubeconfig file from here.
File a `Jira ticket <https://jira.lsstcorp.org/projects/IHS>`_ with IT for access.
Once able to log into Rancher:

#. Select the manke cluster.
#. Click the Kubeconfig File button in top-right.
#. Near bottom of dialog, click the download link.

.. _Deployment-Activities-BTS-Non-Production:

Non-Production Systems
----------------------

The Base Teststand operates all CSCs and systems on the production domain.

.. _Deployment-Activities-BTS-BareMetal:

Bare Metal Machines
-------------------

* Main OSPL Daemon: azar01.ls.lsst.org
* LOVE: love01.ls.lsst.org
* T&S CSCs: tel-hw1.ls.lsst.org
* Kubernetes: Can be done from own machine, just need kubeconfig file and kubectl installed.
    * Systems run on the manke cluster.
    * Can also use: https://k8slens.dev/.
* ATCamera (Tony Johnson): auxtel-mcm.ls.lsst.org

.. _Deployment-Activities-BTS-LOVE-Summary:

LOVE Summary View
-----------------

The overall system summary state view is called ``Summary State``.

.. _Deployment-Activities-BTS-Federation-Check:

Checking the Number of Federations
----------------------------------

This uses a script in https://github.com/lsst-ts/k8s-admin.
Run *./feds-check* from a machine with *kubectl* and the proper kubeconfig file.

.. _Deployment-Activities-BTS-Camera-Shutdown:

Shutdown Camera Services
-------------------------------

* Shutdown ATCamera OCS Bridges:
    * *sudo systemctl stop ats-ocs-bridge.service*
* Shutdown Camera Daemons
    * *sudo systemctl stop opensplice.service*

.. _Deployment-Activities-BTS-LOVE-Shutdown:

Shutdown LOVE
-------------

This needs to be done from love01.

* Uses the ``docker-compose-admin`` scripts in ``base-teststand/love01`` directory, which are checked out to the dco user home directory.
    * Become the dco user: *sudo -iu dco*
    * *./shutdown_love*
    * *./shutdown_daemon*

.. _Deployment-Activities-BTS-TandS-BM-Shutdown:

Shutdown T&S Bare Metal Services
--------------------------------

Handle tel-hw1:

* Uses the ``docker-compose-admin`` scripts in ``base-teststand/tel-hw1`` directory, which are checked out to the dco user home directory.
    * Become the dco user: *sudo -iu dco*
    * *./shutdown_atmcs_atp*
    * *./shutdown_m1m3*
    * *./shutdown_daemon*

.. _Deployment-Activities-BTS-Kubernetes:

Interacting with Kubernetes
---------------------------

Commands can be executed from your own machine with *kubectl* and the proper kubeconfig file.

.. _Deployment-Activities-BTS-Main-Daemon-Shutdown:

Shutdown Main Daemon
--------------------

This needs to be done from azar01.

* Uses the ``docker-compose-admin`` scripts in ``summit/azar01``, which are checked out to the dco user home directory.
    * Become the dco user: *sudo -iu dco*
    * *./shutdown_daemon*

.. _Deployment-Activities-BTS-Update-Configuration:

Update Configuration
--------------------

* Gather the branch for the configurations and version number for ``ts_ddsconfig``.
* Uses the ``docker-compose-admin/base-teststand/update_repo`` script, which is checked out to the dco user home directory.
* Repos to update:
    * ``docker-compose-ops`` (love01, tel-hw1)
    * ``LOVE-integration-tools`` (love01)
    * ``ts_ddsconfig`` (love01, tel-hw1) NOTE: Only necessary if there are updates.
* Become the dco user: *sudo -iu dco*
* *./update_repo <repo path> <branch or version>*

.. _Deployment-Activities-BTS-Main-Daemon-Startup:

Startup Main Daemon
-------------------

This needs to be done from azar01.

* Uses the ``docker-compose-admin`` scripts in ``summit/azar01`` directory.
    * Become the dco user: *sudo -iu dco*
    * *./launch_daemon*
    * Ensure daemon is ready before proceeding.

.. _Deployment-Activities-BTS-Minimal-K8S-System:

Startup Minimal Kubernetes System
---------------------------------

This replaces most of step 6.3 in the main document.
Follow the first three bullet points in that step and then continue the process with the next steps.

* *python sync_apps.py -p --no-sync=love* 
* NOTE: the --no-sync=love flag will prevent an error regarding resources not existing.
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

.. _Deployment-Activities-BTS-LOVE-Startup:

Startup LOVE
------------

This needs to be done from love01.

* Uses the ``docker-compose-admin`` scripts in ``base-teststand/love01`` directory.
    * Become the dco user: *sudo -iu dco*
    * *./launch_daemon*
    * Ensure daemon is ready before proceeding.
    * *./launch_love*

.. _Deployment-Activities-BTS-TandS-BM-Startup:

Startup T&S Bare Metal Services
-------------------------------

Handle tel-hw1

* Uses the ``docker-compose-admin`` scripts in ``base-teststand/tel-hw1`` directory.
    * Become the dco user: *sudo -iu dco*
    * *./launch_daemon*
    * Ensure daemon is ready before proceeding.
    * *./launch_atmcs_atp*
    * *./launch_m1m3*

.. _Deployment-Activities-BTS-Enabled-CSCs:

Enabled CSCs
------------

If proceeding with integration testing, the CSCs will be brought to ENABLED state as part of that process.
All of the startup processes maybe necessary for recovering the BTS from any maintenance.
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

    ATCamera must be in OFFLINE_AVAILABLE state before putting them into ENABLED state.

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
      - [Watcher, ENABLED]
