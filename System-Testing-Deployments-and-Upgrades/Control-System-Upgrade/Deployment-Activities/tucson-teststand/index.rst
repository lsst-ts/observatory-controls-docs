Tucson Test Stand
=================

This section contains site specific variations for the Tucson test stand.

.. _Deployment-Activities-TTS-Resources:

Resources
---------

* LOVE: https://tucson-teststand.lsst.codes/love
* Argo CD: https://tucson-teststand.lsst.codes/argo-cd
* Chronograf: https://tucson-teststand.lsst.codes/chronograf
* Nublado: https://tucson-teststand.lsst.codes/
* Rancher: https://rancher.tu.lsst.org
* Slack: ``#tucson-teststand``

.. _Deployment-Activities-TTS-Update-Configuration:

Update Configuration
--------------------

* Configurations for the different applications deployed to TTS can be found in the Phalanx repo (https://github.com/lsst-sqre/phalanx).

.. _Deployment-Activities-TTS-LOVE-Summary:

LOVE Summary View
-----------------

The overall system summary state view is called ``SummaryState``.


Interacting with Kubernetes
---------------------------
Commands can be executed from your own machine with ``kubectl`` and the ``pillan.yaml`` kubeconfig file.
You can obtain the kubeconfig file from https://rancher.tu.lsst.org. If you don't have access, file a `Jira ticket <https://rubinobs.atlassian.net/jira/software/c/projects/IHS/boards/201>`_ with IT.
Once you're able to log into Rancher:

#. Select the pillan cluster.
#. Click the Kubeconfig File button in top-right.
#. Near bottom of dialog, click the download link.
#. Save the config file under your local ``.kube`` directory as ``pillan.yaml``
#. Point to the required cluster by doing::
    
    export KUBECONFIG=~/.kube/pillan.yaml
    kubectl config use-context pillan

#. Ensure you are pointing to the right cluster by doing::
    
    kubectl config current-context


.. _Deployment-Activities-TTS-BareMetal:

Bare Metal Machines
-------------------

* ATCamera (Tony Johnson): ``auxtel-mcm.tu.lsst.org``
* CCCamera (Tony Johnson): ``comcam-mcm.tu.lsst.org``

.. _Deployment-Activities-TTS-Camera-Shutdown:

Shutdown Camera Services
------------------------

* Shutdown ATCamera OCS Bridge  
  From ``auxtel-mcm.tu.lsst.org`` run::

    sudo systemctl stop ats-ocs-bridge.service

* Shutdown CCCamera OCS Bridge  
  From ``comcam-mcm.tu.lsst.org`` run::

    sudo systemctl stop comcam-ocs-bridge.service


.. _Deployment-Activities-TTS-Camera-Startup:

Startup Camera Services
-----------------------

* Startup ATCamera OCS Bridge  
  From ``auxtel-mcm.tu.lsst.org`` run::

    sudo systemctl start ats-ocs-bridge.service

* Startup CCCamera OCS Bridge  
  From ``comcam-mcm.tu.lsst.org`` run::

    sudo systemctl start comcam-ocs-bridge.service

* Ensure bridge services are running using::

    sudo systemctl status <camera-name>-ocs-bridge.service

* Transition to OFFLINE_AVAILABLE::

    ccs-shell
    ccs> set target <camera-name>-ocs-bridge
    ccs> setAvailable --withLock
    ccs> exit

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
* ScriptQueue:3
* DSM:1
* DSM:2

Only leverage the following scripts, if necessary.
Required configurations will be given for each script execution.

* ``set_summary_state.py``

  .. code:: bash

    data:
      - [ESS:*, ENABLED]
      - [Watcher, ENABLED]
