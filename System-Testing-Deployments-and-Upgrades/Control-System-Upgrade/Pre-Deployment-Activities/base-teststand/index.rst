Base Test Stand
===============

This section contains site specific variations for the Base test stand.

.. _Pre-Deployment-Activities-BTS-Configuration-Repos-Info:

Configuration Repository Information
------------------------------------

Deployment configuration files are kept in https://github.com/lsst-sqre/phalanx.

* Site specific configurations are under ``phalanx/environments/values-base.yaml``. One can enable applications and set a specific cycle tag there.

* Application specific configurations are found under:
   * ``phalanx/applications/<name-of-app>/values-base.yaml``
   * ``phalanx/applications/<name-of-app>/secrets-base.yaml`` (In the case of secrets specific to one site).


.. _Pre-Deployment-Activities-BTS-Slack-Announce:

Slack Channel for Announcements
-------------------------------

``#base-teststand``