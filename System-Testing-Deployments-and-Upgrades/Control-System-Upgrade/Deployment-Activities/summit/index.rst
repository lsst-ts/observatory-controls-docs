Summit
======

This section contains site specific variations for the summit.

.. _Deployment-Activities-Summit-Resources:

Resources
---------

* LOVE: https://summit-lsp.lsst.codes/love and http://love01.cp.lsst.org
* Argo CD: https://summit-lsp.lsst.codes/argo-cd
* Chronograf: https://chronograf-summit-efd.lsst.codes/
* Nublado: https://summit-lsp.lsst.codes/
* Rancher: https://rancher.cp.lsst.org
* Slack: ``#summit-announce``

.. _Deployment-Activities-Summit-BareMetal:

Bare Metal Machines
-------------------

* T&S CSCs: azar2.cp.lsst.org, azar03.cp.lsst.org
* Auxtel illumination control machine: auxtel-ill-control.cp.lsst.org
* LOVE: love01.cp.lsst.org
* ATCamera (Tony Johnson): auxtel-mcm.cp.lsst.org
* CCCamera(Tony Johnson): comcam-mcm.cp.lsst.org
* MTCamera (Tony Johnson): lsstcam-mcm.cp.lsst.org
* M1M3 Support cRIO (Petr Kubánek): m1m3-crio-ss.cp.lsst.org
* M1M3 VMS cRIO (Petr Kubánek): m1m3-crio-vms.cp.lsst.org
* M1M3 TS cRIO (Petr Kubánek):m1m3-crio-ts.cp.lsst.org
* M2 VMS cRIO (Petr Kubánek): m2-crio-vms01.cp.lsst.org
* VMS Data Logger: vms-data.cp.lsst.org
* Flat FiberSpectrograph Red: flat-fiberspecred.cp.lsst.org
* Flat FiberSpectrograph Blue: flat-fiberspecblue.cp.lsst.org
.. * M2 Control (Te-Wei Tsai): m2-control.cp.lsst.org
* ESS:1 (Camera Hexapod/Rotator) Controller RPi (Wouter van Reeven): hexrot-ess01.cp.lsst.org
* ESS:2 (M2 Hexapod) Controller RPi (Wouter van Reeven): m2hex-ess01.cp.lsst.org
* ESS:106 (M2 Mirror): m2-ess01.cp.lsst.org
* ESS:107 (Laser Enclosure): laser-rpi.cp.lsst.org
* ESS:111 (Camera Inlet Humidity) Controller RPi: camera-ess01.cp.lsst.org
* ESS:112 (M2 Humidity) Controller RPi: m2-ess02.cp.lsst.org
* ESS:113 (M1M3 Humidity) Controller RPi: m1m3-ess01.cp.lsst.org
* ESS:201 (Auxtel Misc) Controller RPi (Wouter van Reeven): auxtel-ess01.cp.lsst.org
* ESS:203 (Auxtel Lightning) Controller RPi (Wouter van Reeven): auxtel-lightning01.cp.lsst.org
* ESS:204 (Auxtel Windsonic) Controller RPi (Wouter van Reeven): auxtel-ess02.cp.lsst.org
* ESS:307 (DIMM): dimm.cp.lsst.org

.. _Deployment-Activities-Summit-LOVE-Summary:

LOVE Summary View
-----------------

The overall system summary state view is called ``ASummary State View``.

.. _Deployment-Activities-Summit-Camera-Shutdown:

Shutdown Camera Services
------------------------

* Shutdown ATCamera OCS Bridge  
  From ``auxtel-mcm.cp.lsst.org`` run::

    sudo systemctl stop ats-ocs-bridge.service

* Shutdown MTCamera OCS Bridge  
  From ``lsstcam-mcm.cp.lsst.org`` run::

    sudo systemctl stop ocs-bridge.service

* Shutdown CCCamera OCS Bridge  
  From ``comcam-mcm.cp.lsst.org`` run::

    sudo systemctl stop comcam-ocs-bridge.service


.. _Deployment-Activities-Summit-LOVE-Shutdown:

Shutdown bare metal LOVE
------------------------

This needs to be done from ``love01.cp.lsst.org`` as ``dco`` user::

    sudo -iu dco
    ./shutdown_love

.. _Deployment-Activities-Summit-TandS-BM-Shutdown:

Shutdown T&S Bare Metal Services
--------------------------------

* Handle azar03::

    ssh azar03.cp.lsst.org
    sudo -iu dco
    ./shutdown_gc

* Handle M1M3 cRIO::

    ssh admin@m1m3-crio-ss.cp.lsst.org
    /etc/init.d/ts-M1M3support stop

* Handle M1M3 VMS cRIO::

    ssh admin@m1m3-crio-vms.cp.lsst.org
    /etc/init.d/ts-VMS stop

* Handle M1M3 Thermal System cRIO::

    ssh admin@m1m3-crio-ts.cp.lsst.org
    /etc/init.d/ts-m1m3thermal stop

* Handle M2 VMS cRIO::

    ssh admin@m2-crio-vms01.cp.lsst.org
    /etc/init.d/ts-VMS stop

* Handle VMS Data Logger::

    ssh vms-data.cp.lsst.org
    sudo systemctl stop docker.vmslogger

* Handle Auxtel illumination control::

    ssh auxtel-ill-control.cp.lsst.org
    sudo -iu dco
    ./launch_fiberspec

* Handle Flat FiberSpectrograph Red::

    ssh flat-fiberspecred.cp.lsst.org
    sudo -iu dco
    ./shutdown_fiberspec

* Handle Flat FiberSpectrograph Blue::

    ssh flat-fiberspecblue.cp.lsst.org
    sudo -iu dco
    ./shutdown_fiberspec

.. M2 Control:
.. * ssh to that machine.
.. * *ps wuax | grep splice*
.. * *sudo kill <PID>* on any processes turned up by the previous command.

.. _Deployment-Activities-Summit-Kubernetes:

Interacting with Kubernetes
---------------------------
Commands can be executed from your own machine with ``kubectl`` and the ``yagan.yaml`` kubeconfig file.
You can obtain the kubeconfig file from https://rancher.cp.lsst.org. If you don't have access, file a `Jira ticket <https://rubinobs.atlassian.net/jira/software/c/projects/IHS/boards/201>`_ with IT.
Once you're able to log into Rancher:

#. Select the yagan cluster.
#. Click the Kubeconfig File button in top-right.
#. Near bottom of dialog, click the download link.
#. Save the config file under your local ``.kube`` directory as ``yagan.yaml``
#. Point to the required cluster by doing:: 
    
    export KUBECONFIG=~/.kube/yagan.yaml
    kubectl config use-context yagan

#. Ensure you are pointing to the right cluster by doing::
     
    kubectl config current-context


.. _Deployment-Activities-Summit-Update-ESS-Controllers:

Update ESS Controllers
----------------------
* Updating the ESS controllers requires logging into the following machines:
    * hexrot-ess01.cp.lsst.org
    * m2hex-ess01.cp.lsst.org
    * m2-ess01.cp.lsst.org
    * m2-ess02.cp.lsst.org
    * m1m3-ess01.cp.lsst.org
    * laser-rpi.cp.lsst.org
    * camera-ess01.cp.lsst.org
    * auxtel-ess01.cp.lsst.org
    * auxtel-ess02.cp.lsst.org
    * auxtel-lightning01.cp.lsst.org
* Most use docker-compose-ops. To stop, update and restart controllers::

    sudo -iu dco
    ./shutdown_controller
    ./update_repo docker-compose-ops/ <name_of_deployment_branch>
    ./launch_controller

* ESS:107 (laser-rpi.cp.lsst.org) has two containers. To stop, update and restart them::

    sudo -iu dco
    ./shutdown_ess 
    ./shutdown_audiotrigger 
    ./update_repo docker-compose-ops/ <name_of_deployment_branch>
    ./launch_ess 
    ./launch_audiotrigger 

.. _Deployment-Activities-Summit-Update-cRIOs:

Update cRIOs
------------

These steps are usually taken care of by the person responsible for the MTM1M3, MTM1M3TS and MTVMs CSCs (Petr Kubánek), but they need to be followed in case he is unable to perform them for whatever reason.

* SSH into the cRIO machines:
    * ``m1m3-crio-ss`` for MTM1M3 Support System.
    * ``m1m3-crio-ts`` for the Thermal System.
    * ``m2-crio-vms01`` and ``m1m3-crio-vms`` for the VMSs.
    
* Update ``ts_xml`` and set up the kafka environment::

    cd ts_xml
    git checkout main
    git pull
    pip3 install .
    . ~/kafka.env
    . ~/ts_sal/setupKafka.env
    . ~/kafka.env

* Run ``salgeneratorKafka``:
    *  In ``m1m3-crio-ss``::

        salgeneratorKafka generate cpp MTM1M3
        salgeneratorKafka generate cpp MTMount

    *  In ``m1m3-crio-ts``::

        salgeneratorKafka generate cpp MTM1M3TS

    *  In ``m2-crio-vms01`` and ``m1m3-crio-vms``::

        salgeneratorKafka generate cpp MTVMLS


    This should take about an hour to run. For convinience, it is a good idea to run the terminal on the background using screen.
        

* Update the following repos:
    * ``ts_cRIOcpp`` in all machines.
    * ``ts_m1m3support`` in  ``m1m3-crio-ss``.
    * ``ts_m1m3thermal`` in ``m1m3-crio-ts``.
    * ``ts_vms`` in ``m2-crio-vms01`` and ``m1m3-crio-vms``.
* After ``salgeneratorKafka`` finishes and the C++ binding is done, clean and compile ``ts_cRIOcpp`` in all machines::

    cd ../ts_cRIOcpp
    make clean && make

* The same needs to be after for ``ts_m1m3support``, ``ts_m1m3thermal`` and ``ts_vms`` in their corresponding machines.
* Copy the binaries to ``/usr/sbin`` and start up the services:
    * In ``m1m3-crio-ss``::

        cp ts-M1M3supportd /usr/sbin/ts-M1M3supportd
        etc/init.d/ts-M1M3supportd start

    * In ``m1m3-crio-ts``::

        cp ts-M1M3thermald /usr/sbin/ts-M1M3thermald
        /etc/init.d/ts-m1m3thermal start

    * In ``m2-crio-vms01`` and ``m1m3-crio-vms``::

        cp ts-VMSd /usr/sbin/ts-VMSd
        /etc/init.d/ts-VMS start


.. _Deployment-Activities-Summit-Update-Configuration:

Update Configuration
--------------------

* Most configurations for the different applications deployed to the Summit can be found in the Phalanx repo (https://github.com/lsst-sqre/phalanx). Make sure those are correct.
* Some bare metal machine configurations also need to be updated. To do so, we use the ``docker-compose-admin/bin/update_repo`` script, which is linked into the ``dco`` user home directory. The directories to be updated are:
    * ``docker-compose-ops`` (azar2, azar03, auxtel-ill-control, flat-fiberspecred, flat-fiberspecblue)
    * ``LOVE-integration-tools`` (love01)
    * To update these machines, log into them and run::

        sudo -iu dco
        ./update_repo <repo-path> <branch>


.. _Deployment-Activities-Summit-LOVE-Startup:

Startup bare metal LOVE
-----------------------

This needs to be done from ``love01``. After ``LOVE-integration-tools`` has been updated::

    sudo -iu dco
    ./launch_love

.. _Deployment-Activities-Summit-Camera-Startup:

Startup Camera Services
-----------------------

* Startup ATCamera OCS Bridge  
  From ``auxtel-mcm.cp.lsst.org`` run::

    sudo systemctl start ats-ocs-bridge.service

* Startup MTCamera OCS Bridge  
  From ``lsstcam-mcm.cp.lsst.org`` run::

    sudo systemctl start ocs-bridge.service

* Startup CCCamera OCS Bridge  
  From ``comcam-mcm.cp.lsst.org`` run::

    sudo systemctl start comcam-ocs-bridge.service

* Ensure bridge services are running using::

    sudo systemctl status <camera-name>-ocs-bridge.service

* Transition to OFFLINE_AVAILABLE::
        
    ccs-shell
    ccs> set target <camera-name>-ocs-bridge
    ccs> setAvailable --withLock
    ccs> exit


.. _Deployment-Activities-Summit-TandS-BM-Startup:

Startup T&S Bare Metal Services
-------------------------------
* Handle azar03::

    sudo -iu dco
    ./launch_gc

* Handle Auxtel illumination control::

    sudo -iu dco
    ./launch_gc

* Handle Flat FiberSpectrograph Red::

    sudo -iu dco
    ./launch_fiberspec 

* Handle Flat FiberSpectrograph Blue::

    sudo -iu dco
    ./launch_fiberspec 

.. _Deployment-Activities-Summit-Enabled-CSCs:

Enabled CSCs
------------

The following CSCs are configured to go into ENABLED state automatically upon launching:

* ScriptQueue:1
* ScriptQueue:2
* ScriptQueue:3
* HVAC
* WeatherForecast

There are a few CSCs that must be put into ENABLED state before declaring an end to the deployment.
These are:

* ``set_summary_state.py``

  .. code:: bash

    data:
      - [ESS:104, ENABLED]
      - [ESS:105, ENABLED]
      - [ESS:106, ENABLED]
      - [ESS:107, ENABLED]
      - [ESS:108, ENABLED]
      - [ESS:109 ENABLED]
      - [ESS:110, ENABLED]
      - [ESS:111, ENABLED]
      - [ESS:112, ENABLED]
      - [ESS:113, ENABLED]
      - [ESS:114, ENABLED]
      - [ESS:115, ENABLED]
      - [ESS:116, ENABLED]
      - [ESS:117, ENABLED]
      - [ESS:118, ENABLED]
      - [ESS:119, ENABLED]
      - [ESS:120, ENABLED]
      - [ESS:121, ENABLED]
      - [ESS:122, ENABLED]
      - [ESS:201, ENABLED]
      - [ESS:202, ENABLED]
      - [ESS:204, ENABLED]
      - [ESS:301, ENABLED]
      - [ESS:302, ENABLED]
      - [ESS:303, ENABLED]
      - [ESS:304, ENABLED]
      - [ESS:305, ENABLED]
      - [ESS:306, ENABLED]
      - [ESS:308, ENABLED] 
      - [GIS, ENABLED]
      - [Watcher, ENABLED]
