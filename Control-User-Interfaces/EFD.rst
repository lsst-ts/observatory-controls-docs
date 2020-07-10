.. This is a template top-level index file for a directory in the procedure's arm of the documentation

.. This is the label that can be used as for cross referencing in the given area
.. Recommended format is "Directory Name"-"Title Name"  -- Spaces should be replaced by hypens
.. _EFD:

###############################
Engineering Facilities Database
###############################

.. Quick intro to EFD, what it does, why we need it.

The Engineering Facilities Database (EFD) records all interactions between components that occur over the middleware.
The database is useful for numerous activities, including: troubleshooting of software or hardware related issues, optimization of observing parameters (e.g. focus as a function of temperature), and recovering useful data that happened during an observation that may not be in the header.

.. Brief explanation on how data flows from the summit to NCSA (with the idea of leading into the next part which should guide the user on when to use which instance, summit, base, ncsa).

The primary location of the EFD is on the summit, however a separate instance also lives at the base facility in La Serena.
Under normal conditions, the data is then synced to NCSA and available via the LSP within several minutes.
It is recommended to use the NCSA instance if the information is not time critical in order to not add unncessary traffic to the Base Facility.
Direct interaction with the summit EFD is strongly discouraged and should only be used if no other viable option exists.

The EFD is backed by InfluxBD, details of the EFD architecture, implementation and deployment(s) are found at `https://sqr-034.lsst.io <https://sqr-034.lsst.io>`__.

Interacting with the EFD
^^^^^^^^^^^^^^^^^^^^^^^^

There are two primary user-interfaces to the EFD, Chronograf and the EFD Client. Each endpoint satisfies multiple, but not identical use-cases.

Chronograf
----------
`Chronograf <https://docs.influxdata.com/chronograf/v1.8/>`_ is a web-based graphical front-end to the database where users can make simple queries and create plots or graphical representations of data.

.. note::

  To login to Chronograf, you need to be a member of the GitHub lsst-sqre organization. If you are not, please request access on the ``#com-square`` LSSTC Slack channel.

.. Would be nice to show some sort of screenshot here?

More information on using Chronograf can be found at the `getting started page <https://docs.influxdata.com/chronograf/v1.8/introduction/getting-started/>`__.


EFD Client
__________

The `EFD Client <https://efd-client.lsst.io/>`__ permits access to the data from a notebook or python program.
This is often the preferred method for more detailed analyses or where record-keeping is required.
It contains multiple methods to aid with queries and data interactions, essentially wrapping much of the functionality from `aioinflux (the influxDB client) <https://aioinflux.readthedocs.io/en/stable/api.html>`__.


Accessing the EFD
^^^^^^^^^^^^^^^^^

The following sections list the EFD instances available, where they run and who the intended audience is for each one.

..  I just 95% copied/pasted here, but I think only the summit, base and LSP instances are required to be shown?
    I would think users also don't need to know about the Kafka details?
    It does make sense to link to a "master list" of all instances, but for most people I'm not sure it's necessary.
    Seeing as this area is still in flux I'm hesitant to keep a master list here, but at the same time I don't like the idea of duplicating data.
    Maybe the best thing to do is just link this section to sqr-034. Might need some thought.


Summit EFD
----------

Instance running at the Summit (Chile).

Intended audience: Operations scripts and software. May be used by Commissioning and Science Verification teams when Base EFD is unavailable.

Data at the Summit EFD is also replicated to the LDF EFD to enable project wide access.

Chronograf: https://chronograf-summit-efd.lsst.codes

InfluxDB HTTP API (used by the EFD Client): https://influxdb-summit-efd.lsst.codes

Kafka Schema Registry: https://schema-registry-summit-efd.lsst.codes

Kafka Broker: kafka-0-summit-efd.lsst.codes:31090

Base EFD
--------

Instance running at the Base facility (Chile), which is a on-the-fly replica of the summit EFD.

Intended audience: Commissioning and Science Verification teams.

The plan is to have replication from the summit to the base and from the base to LDF working soon.

Chronograf: https://chronograf-base-efd.lsst.codes

InfluxDB HTTP API: https://influxdb-base-efd.lsst.codes

Kafka Schema Registry: https://schema-registry-base-efd.lsst.codes

Kafka Broker: cp-helm-charts-cp-kafka-headless.cp-helm-charts:9092

LSP Stable EFD
---------------

Instance running at NCSA on the LSP production cluster.

Intended audience: Everyone in the project.

Chronograf: https://lsst-chronograf-efd.ncsa.illinois.edu

InfluxDB HTTP API: https://lsst-influxdb-efd.ncsa.illinois.edu

Kafka Schema Registry: https://lsst-schema-registry-efd.ncsa.illinois.edu

Kafka Broker: cp-helm-charts-cp-kafka-headless.cp-helm-charts:9092


LSP Integration EFD
--------------------

Instance running at NCSA on the LSP development cluster.

.. note::

  As of March 20, this instance holds a copy of the Summit EFD data and dashboards and can be used during the shutdown of the Rubin Observatory caused by the COVID-19 outbreak.

Intended audience: Commissioning and Science Verification teams.

Chronograf: https://lsst-chronograf-int-efd.ncsa.illinois.edu

InfluxDB HTTP API: https://lsst-influxdb-int-efd.ncsa.illinois.edu

Kafka Schema Registry: https://lsst-schema-registry-int-efd.ncsa.illinois.edu

Kafka Broker:  cp-helm-charts-cp-kafka-headless.cp-helm-charts:9092


..  Any Figures should be stored in the same directory as this file.
    To add images, add the image file (png, svg or jpeg preferred) to the same directory as this .rst file.
    The reST syntax for adding the image is:
    .. figure:: /filename.ext
        :name: fig-label
        :target: http://target.link/url
        Caption text.
