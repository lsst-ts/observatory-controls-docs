Base Test Stand
=================

This section contains site specific variations for the Base test stand.

.. _Deployment-Activities-BTS-Resources:

Resources
---------

* LOVE: https://base-lsp.lsst.codes/love
* Argo CD: https://base-lsp.lsst.codes/argo-cd
* Chronograf: https://base-lsp.lsst.codes/chronograf
* Nublado: https://base-lsp.lsst.codes/
* Rancher: https://rancher.ls.lsst.org 
* Slack: ``#base-teststand``

.. _Deployment-Activities-BTS-Update-Configuration:

Update Configuration
--------------------

* Configurations for the different applications deployed to BTS can be found in the Phalanx repo (https://github.com/lsst-sqre/phalanx).

.. _Deployment-Activities-BTS-LOVE-Summary:

LOVE Summary View
-----------------

The overall system summary state view is called ``SummaryState``.

.. .. _Deployment-Activities-BTS-Federation-Check:

.. Checking the Number of Federations
.. ----------------------------------

.. This uses a script in https://github.com/lsst-ts/k8s-admin.
.. Run ``./feds-check`` from a machine with ``kubectl`` and the proper kubeconfig file.

Interacting with Kubernetes
---------------------------
Commands can be executed from your own machine with ``kubectl`` and the ``manke.yaml`` kubeconfig file.
You can obtain the kubeconfig file from https://rancher.ls.lsst.org. If you don't have access, file a `Jira ticket <https://rubinobs.atlassian.net/jira/software/c/projects/IHS/boards/201>`_ with IT.
Once you're able to log into Rancher:

#. Select the manke cluster.
#. Click the Kubeconfig File button in top-right.
#. Near bottom of dialog, click the download link.
#. Save the config file under your local ``.kube`` directory as ``manke.yaml``
#. Point to the required cluster by doing::
    
    export KUBECONFIG=~/.kube/manke.yaml
    kubectl config use-context manke

#. Ensure you are pointing to the right cluster by doing::
    
    kubectl config current-context

.. _Deployment-Activities-BTS-BareMetal:

Bare Metal Machines
-------------------
* ATCamera (Tony Johnson): ``auxtel-mcm.ls.lsst.org``
* MTCamera (Tony Johnson): ``lsstcam-mcm.ls.lsst.org``

.. _Deployment-Activities-BTS-Camera-Shutdown:

Shutdown Camera Services
------------------------

* Shutdown ATCamera OCS Bridge  
  From ``auxtel-mcm.ls.lsst.org`` run::

    sudo systemctl stop ats-ocs-bridge.service

* Shutdown MTCamera OCS Bridge  
  From ``lsstcam-mcm.ls.lsst.org`` run::

    sudo systemctl stop lsstcam-ocs-bridge.service

.. _Deployment-Activities-BTS-Camera-Startup:

Startup Camera Services
-----------------------

* Startup ATCamera OCS Bridge  
  From ``auxtel-mcm.ls.lsst.org`` run::

    sudo systemctl start ats-ocs-bridge.service

* Startup MTCamera OCS Bridge  
  From ``lsstcam-mcm.ls.lsst.org`` run::

    sudo systemctl start lsstcam-ocs-bridge.service

* Ensure bridge services are running using::

    sudo systemctl status <camera-name>-ocs-bridge.service

* Transition to OFFLINE_AVAILABLE::

    ccs-shell
    ccs> set target <camera-name>-ocs-bridge
    ccs> setAvailable --withLock
    ccs> exit

.. _Deployment-Activities-BTS-Enabled-CSCs:

Enabled CSCs
------------

If proceeding with integration testing, the CSCs will be brought to ENABLED state as part of that process.
All of the startup processes may be necessary for recovering the BTS from any maintenance.
The following components will automatically transition to ENABLED state when launched:

* WeatherForecast
* ScriptQueue:1
* ScriptQueue:2
* DSM:1
* DSM:2

Only leverage the following scripts, if necessary.
Required configurations will be given for each script execution.

* ``set_summary_state.py``

  .. code:: bash

    data:
      - [ESS:*, ENABLED]
      - [Watcher, ENABLED]
