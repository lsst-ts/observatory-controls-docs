#############################
Camera Control System Upgrade
#############################

In the following instructions we assume you are dealing with comcam, if dealing with auxtel or main-camera make substitutions where appropriate.

Shutdown Services
-----------------

When doing an XML upgrade it is first necessary to wait for SAL to be shutdown. Once the comcam-ocs-bridge have been shutdown it is possible to proceed with stage 1 of the upgrade.

.. _camera-install-stage-1:

Stage 1: Installing the release
-------------------------------


* Use foreman to change the puppet environment to deploy the new release.
  (For the summit use https://foreman.cp.lsst.org, and for TTS use https://foreman.tu.lsst.org, and for BTS use https://foreman.ls.lsst.org).
* Check that puppet in fact installed the new release on all nodes by looking for the release in :file:`/lsst/ccs/<release>`.
* On each host, move the :file:`/lsst/ccs/prod` link to point to the new release
* On each host, while logged in as user ccs, restart all of the ccs subsystems using :command:`sudo systemctl restart <xxx>`.
  Do not restart the *ocs-bridge* at this stage.
* Check that all CCS subsystems succesfully restarted.
  Check that telemetry is working (see http://ccs.lsst.org).
* Wait for the go-ahead from the person upgrading SAL before proceeding to stage 2.

.. _camera-install-stage-2:

Stage 2: Restarting opensplice and ocs-bridge
---------------------------------------------

These instructions should be performed on comcam-mcm while logged in as user ccs.

* Use the command :command:`sudo systemctl restart comcam-ocs-bridge`
* Put the ocs-bridge into *OFFLINE_AVAILABLE* mode using

.. code-block:: bash

    $ ccs-shell
    ccs> set target comcam-ocs-bridge
    ccs comcam-ocs-bridge> lock
    ccs comcam-ocs-bridge> setAvailable
    ccs comcam-ocs-bridge> unlock

* Test operation of the *comcam-ocs-bridge* using *comcam-ocs-gui*. At a minimum ensure you can switch the system to *enabled* mode and then back to *standby*.
