Summit
======

This section contains site specific variations for the Summit.

.. _Pre-Deployment-Activities-Summit-Configuration-Repos-Info:

Configuration Repository Information
------------------------------------
Most deployment configuration files are kept in https://github.com/lsst-sqre/phalanx.

* Site specific configurations are under ``phalanx/environments/values-summit.yaml``. One can enable applications and set a specific cycle tag there.

* Application specific configurations are found under:
    * ``phalanx/applications/<name-of-app>/values-summit.yaml``
    * ``phalanx/applications/<name-of-app>/secrets-summit.yaml`` (In the case of secrets specific to one site).

For changes in https://github.com/lsst-it/docker-compose-ops or
https://github.com/lsst-ts/LOVE-integration-tools, use the following options:

* ``docker-compose-ops``: ``summit``
* ``LOVE-integration-tools``: ``deploy/summit`` (love01)

.. _Pre-Deployment-Activities-Summit-Scheduling:

Scheduling Summit Upgrade
-------------------------

Please note that the summit work **MUST** be put on the Summit Jira calendar by filing a ticket on the `Summit Jira <https://rubinobs.atlassian.net/projects/SUMMIT>`_ project.
By filling in the ``Start Date`` and ``End Date`` fields, the ticket will automatically appear on the calendar.
Set the ticket priority level to one.
Make sure Andy Clements is aware of the ticket.
The summit work **MUST** take place after 5 PM Chilean time on the given day to avoid bothering the day crew.

.. _Pre-Deployment-Activities-Summit-Slack-Announce:

Slack Channel for Announcements
-------------------------------

``#summit-announce``

