Tucson Test Stand
=================

This section contains site specific variations for the Tucson test stand.

.. _Pre-Deployment-Activities-TTS-Configuration-Repos-Info:

Configuration Repository Information
------------------------------------

Deployment configuration files are kept in https://github.com/lsst-sqre/phalanx. 
* Site specific configurations are under ``phalanx/environments/values-tucson-teststand.yaml``. One can enable applications and set a specific cycle tag there.
* Application specific configurations are found under:
    * ``phalanx/applications/<name-of-app>/values-tucson-teststand.yaml``
    * ``phalanx/applications/<name-of-app>/secrets-tucson-teststand.yaml`` (In the case of secrets specific to one site).


.. _Pre-Deployment-Activities-TTS-Slack-Announce:

Slack Channel for Announcements
-------------------------------

``#tucson-teststand``
