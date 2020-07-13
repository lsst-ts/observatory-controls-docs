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
Under normal conditions, the data is then synced to the US data facility and available via the science platform in near real time.
The US data facility instance is intended to service all needs not related to on summit activities such as controller scripts and tight loop feedback.
Direct interaction with the summit EFD is strongly discouraged and should only be used if no other viable option exists.

.. note::

The current global situation has caused deviation from the above plan.
Since the closure of the summit facilities, the summit EFD has been mirrored to another instance running on the base computing infrastructure.
This is expected to be a temporary solution and that the primary EFD will move back to the summit when activities resume.

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

.. figure:: /Control-User-Interfaces/weather.png
    :name: weather
    :target: weather.png

    An example Chronograf dashboard showing weather station information on the summit from 1-2 January 2020.

More information on using Chronograf can be found at the `getting started page <https://docs.influxdata.com/chronograf/v1.8/introduction/getting-started/>`__.

EFD Client
----------

The `EFD Client <https://efd-client.lsst.io/>`__ permits access to the data from a notebook or python program.
This is often the preferred method for more detailed analyses or where record-keeping is required.
It contains multiple methods to aid with queries and data interactions, essentially wrapping much of the functionality from `aioinflux (the influxDB client) <https://aioinflux.readthedocs.io/en/stable/api.html>`__.


Accessing the EFD
^^^^^^^^^^^^^^^^^

Following is a list of EFD instances.
Please refer https://sqr-034.lsst.io for technical details: e.g. information about connecting directly to the influxDB server API.
There are also several instances of the EFD deployed at various places that are unlikely to be of general interest.
These are also listed in the aforementioned SQuaRE technical note.

The entry titled "efd_client alias" is the string to pass to the ``EfdClient`` constructor in order to authenticate to that instance of the EFD.

..  I just 95% copied/pasted here, but I think only the summit, base and LSP instances are required to be shown?
    I would think users also don't need to know about the Kafka details?
    It does make sense to link to a "master list" of all instances, but for most people I'm not sure it's necessary.
    Seeing as this area is still in flux I'm hesitant to keep a master list here, but at the same time I don't like the idea of duplicating data.
    Maybe the best thing to do is just link this section to sqr-034. Might need some thought.

=====================  ================  ========================================================================  ==================================================================  ===================================
Location               efd_client alias  Audience                                                                  Chronograf link                                                     Notes
=====================  ================  ========================================================================  ==================================================================  ===================================
Summit (Cerro Pachón)  summit_efd        Operations scripts and software. Last resort backup.                      `chronograf <https://chronograf-summit-efd.lsst.codes>`__           Currently unavailable
Base (La Serena)       base_efd          Temporary copy of the summit EFD for use by Commissioning and V&V.        `chronograf <https://chronograf-base-efd.lsst.codes>`__             Temporary
Data Facility (NCSA)   ldf_int_efd       Anyone on project interacting with the EFD through the science platform.  `chronograf <https://lsst-chronograf-int-efd.ncsa.illinois.edu>`__  In development.  Alias will change.
=====================  ================  ========================================================================  ==================================================================  ===================================

..  Any Figures should be stored in the same directory as this file.
    To add images, add the image file (png, svg or jpeg preferred) to the same directory as this .rst file.
    The reST syntax for adding the image is:
    .. figure:: /filename.ext
        :name: fig-label
        :target: http://target.link/url
        Caption text.
