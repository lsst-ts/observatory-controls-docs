Summit
======

This section contains site specific variations for the summit.

.. _Deployment-Activities-Summit-Resources:

Resources
---------

* LOVE: http://love01.cp.lsst.org
* Argo CD: https://summit-lsp.lsst.codes/argo-cd
* Chronograf: https://chronograf-summit-efd.lsst.codes/
* Nublado: https://summit-lsp.lsst.codes/
* Rancher: https://rancher.cp.lsst.org (1)
* Slack: #summit-announce

(1) Need to get kubeconfig file from here.
File a `Jira ticket <https://jira.lsstcorp.org/projects/IHS>`_ with Chilean IT for access.
Once able to log into Rancher:

#. Select the yagan cluster.
#. Click the Kubeconfig File button in top-right.
#. Near bottom of dialog, click the download link.

.. _Deployment-Activities-Summit-Non-Production:

Non-Production Systems
----------------------

The non-production domain systems list is kept here: `Summit deployment <https://confluence.lsstcorp.org/display/LTS/Summit+deployment>`_.

.. _Deployment-Activities-Summit-BareMetal:

Bare Metal Machines
-------------------

* Main OSPL Daemon: azar1.cp.lsst.org
* T&S CSCs: azar2.cp.lsst.org
* LOVE: love01.cp.lsst.org
* LOVE2: love02.cp.lsst.org
* Kubernetes: Can be done from own machine, just need kubeconfig file and kubectl installed.
    * Systems run on the yagan cluster.
    * Can also use: https://k8slens.dev/.
* ATCamera (Tony Johnson): auxtel-mcm.cp.lsst.org
* CCCamera(Tony Johnson): comcam-mcm.cp.lsst.org
* M1M3 Dev (Petr Kubánek): m1m3-dev.cp.lsst.org
* M1M3 Test (Petr Kubánek): m1m3-test.cp.lsst.org
* M1M3 Support cRIO (Petr Kubánek): 139.229.178.182
* M1M3 VMS cRIO (Petr Kubánek): 139.229.178.183
* M2 VMS cRIO (Petr Kubánek): 139.229.178.193
* ATMCS/ATPneumatics cRIO (Tiago Ribeiro): 139.229.170.47
* AT PMD (Eric Coughlin): at-keener.cp.lsst.org
* M2 Control (Te-Wei Tsai): m2-control.cp.lsst.org
* ESS:1 Controller RPi (Wouter van Reeven): hexrot-ess01.cp.lsst.org
* ESS:201 Controller RPi (Wouter van Reeven): auxtel-ess01.cp.lsst.org
* ESS:204 Controller RPi (Wouter van Reeven): auxtel-ess02.cp.lsst.org
* ESS:203 Controller RPi (Wouter van Reeven): auxtel-lightning01.cp.lsst.org
* ESS:101 Controller RPi (Wouter van Reeven): mtdome-ess01.cp.lsst.org
* ESS:102 Controller RPi (Wouter van Reeven): mtdome-ess02.cp.lsst.org
* ESS:103 Controller RPi (Wouter van Reeven): mtdome-ess03.cp.lsst.org

.. _Deployment-Activities-Summit-Odd-State:

Odd State Components
--------------------

ATMCS does not yet respond properly to exitControl and will remain in STANDBY with heartbeats still present.
ATPneumatics does not always respond to being sent to OFFLINE.  It may remain in STANDBY with heartbeats still present.

.. _Deployment-Activities-Summit-LOVE-Summary:

LOVE Summary View
-----------------

The overall system summary state view is called ``ASummary State View``.

.. _Deployment-Activities-Summit-Federation-Check:

Checking the Number of Federations
----------------------------------

This uses a script in https://github.com/lsst-ts/k8s-admin.
Run *./feds-check* from a machine with *kubectl* and the proper kubeconfig file.

.. _Deployment-Activities-Summit-Camera-Shutdown:

Shutdown Camera Services
------------------------

* Shutdown Camera OCS Bridges:
    * ATCamera: *sudo systemctl stop ats-ocs-bridge.service*
    * CCCamera: *sudo systemctl stop comcam-ocs-bridge.service*
* Shutdown Camera Daemons (command is the same on both machines)
    * *sudo systemctl stop opensplice.service*

.. _Deployment-Activities-Summit-LOVE-Shutdown:

Shutdown LOVE
-------------

This needs to be done from love01.

* Uses the ``docker-compose-admin`` scripts in ``summit/love01`` directory.
    * *./shutdown_love*
    * *./shutdown_daemon*

If LOVE2 is operating, go to love02.

* Uses the ``docker-compose-admin`` scripts in ``summit/love02`` directory.
    * *./shutdown_love*
    * *./shutdown_daemon*

.. _Deployment-Activities-Summit-TandS-BM-Shutdown:

Shutdown T&S Bare Metal Services
--------------------------------

Handle azar2:

* Uses the ``docker-compose-admin`` scripts in ``summit/azar2`` directory.
    * *./shutdown_eas*
    * *./shutdown_daemon*

Handle AT systems (ATMCS and ATPneumatics):

* *ssh admin@139.229.170.47*
* *vim setup.env*
* Line 60: replace 0 with 2 in the **LSST_DDS_DOMAIN_ID** variable.
* *reboot && exit*

Handle M1M3 cRIO:

* *ssh admin@139.229.178.182*
* */etc/init.d/ts-M1M3support stop*

Handle M1M3 VMS cRIO:

* *ssh admin@139.229.178.183*
* */etc/init.d/ts-VMS stop*

Handle M2 VMS cRIO:

* *ssh admin@139.229.178.193*
* */etc/init.d/ts-VMS stop*

Handle M1M3 Dev & Test:

* ssh to those machines.
* *ps wuax | grep splice*
* *sudo kill <PID>* on any processes turned up by the previous command.

AT PMD (at-keener):

* Uses ``docker-compose-ops``, so should be similar to azar2 (just doesn't have ``docker-compose-admin`` scripts).

M2 Control:

* ssh to that machine.
* *ps wuax | grep splice*
* *sudo kill <PID>* on any processes turned up by the previous command.

.. _Deployment-Activities-Summit-Kubernetes:

Interacting with Kubernetes
---------------------------

Commands can be executed from your own machine with *kubectl* and the yagan.yaml kubeconfig file.

Download from https://rancher.cp.lsst.org/dashboard

.. _Deployment-Activities-Summit-Main-Daemon-Shutdown:

Shutdown Main Daemon
--------------------

This needs to be done from azar1.

* Uses the ``docker-compose-admin`` scripts in ``summit/azar1`` directory.
    * *./shutdown_daemon*

.. _Deployment-Activities-Summit-Update-ESS-Controllers:

Update ESS Controllers
----------------------
    * Updating the ESS controllers requires logging into the following machines:
        * hexrot-ess01.cp.lsst.org
        * auxtel-ess01.cp.lsst.org
        * auxtel-ess02.cp.lsst.org
        * auxtel-lightning01.cp.lsst.org
        * mtdome-ess01.cp.lsst.org 
        * mtdome-ess02.cp.lsst.org
        * mtdome-ess03.cp.lsst.org 
    * To stop, update and restart the container, issue the following commands:
        * *docker stop ess-controller*
        * *docker rm ess-controller*
        * *docker image pull lsstts/ess-controller-aarch64:latest*
        * *docker run -it --name ess-controller --network host --privileged lsstts/ess-controller-aarch64*

.. _Deployment-Activities-Summit-Update-Configuration:

Update Configuration
--------------------

* Gather the branch for the configurations and version number for ``ts_ddsconfig``.
* Uses the ``docker-compose-admin/summit/update_repo`` script, which is linked into the dco user home directory.
* Directories to update:
    * ``docker-compose-ops`` (azar1, azar2, love01, love02)
    * ``LOVE-integration-tools`` (love01, love02)
    * ``ts_ddsconfig`` (azar1, azar2, love01, love02) NOTE: Only necessary if there are updates.
* Become the dco user: *sudo -iu dco* (The dco has not been setup on love01, so use the scripts in your home directory.)
* *sudo ./update_repo <repo path> <branch or version>*

.. _Deployment-Activities-Summit-Main-Daemon-Startup:

Startup Main Daemon
-------------------

This needs to be done from azar1.

* Uses the ``docker-compose-admin`` scripts in ``summit/azar1`` directory.
    * *./launch_daemon*

.. _Deployment-Activities-Summit-LOVE-Startup:

Startup LOVE
-------------

This needs to be done from love01.

* Uses the ``docker-compose-admin`` scripts in ``summit/love01`` directory.
    * *./launch_daemon*
    * Ensure daemon is ready before proceeding.
    * *./launch_love*

If LOVE2 is operating, go to love02.

* Uses the ``docker-compose-admin`` scripts in ``summit/love02`` directory.
    * *./launch_daemon*
    * Ensure daemon is ready before proceeding.
    * *./launch_love*

.. _Deployment-Activities-Summit-Camera-Startup:

Startup Camera Services
-----------------------

This needs to be done from auxtel-mcm and comcam-mcm.

* Start Camera Daemons (command is the same on both machines)
    * *sudo systemctl start opensplice.service*
* Start Camera OCS Bridges:
    * ATCamera: *sudo systemctl start ats-ocs-bridge.service*
    * CCCamera: *sudo systemctl start comcam-ocs-bridge.service*
    * Ensure bridge services are running:
	* ATCamera: *sudo systemctl status ats-ocs-bridge.service*
	* CCCamera: *sudo systemctl status comcam-ocs-bridge.service*
* Transition to OFFLINE_AVAILABLE:
    * ATCamera:
        * *ccs-shell*
        * *ccs> set target ats-ocs-bridge*
        * *ccs> lock*
        * *ccs> setAvailable*
        * *ccs> unlock*
        * *ccs> exit*
    * CCCamera:
        * *ccs-shell*
        * *ccs> set target comcam-ocs-bridge*
        * *ccs> lock*
        * *ccs> setAvailable*
        * *ccs> unlock*
        * *ccs> exit*

.. _Deployment-Activities-Summit-TandS-BM-Startup:

Startup T&S Bare Metal Services
-------------------------------

Handle azar2:

* Uses the ``docker-compose-admin`` scripts in ``summit/azar2`` directory.
    * *./launch_daemon*
    * Ensure daemon is ready before proceeding.
    * *./launch_eas*

.. _Deployment-Activities-Summit-Enabled-CSCs:

Enabled CSCs
------------

The following CSCs are configured to go into ENABLED state automatically upon launching:

* ScriptQueue:1
* ScriptQueue:2

There are a few CSCs that must be put into ENABLED state before declaring an end to the deployment.
These are:

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
      - [ESS:205, ENABLED]
      - [ESS:301, ENABLED]
      - [Watcher, ENABLED]
