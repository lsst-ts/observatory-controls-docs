.. This is a template top-level index file for a directory in the procedure's arm of the documentation

.. This is the label that can be used as for cross referencing in the given area
.. Recommended format is "Directory Name"-"Title Name"  -- Spaces should be replaced by hypens
.. _Troubleshooting:

###############
Troubleshooting
###############


Software user manuals are often packaged and released with the code such that the documentation is available at the same time new features are released.
Because issues often arise with software that is already released, this section focuses on current issues and their workarounds.

.. Important::
    This section only addresses active issues which are directly related to deployed software.
    This is not a generic help section.


The issues are grouped according to which items are affected.
All items must link a JIRA ticket to where the issue is being addressed.


Control Packages
^^^^^^^^^^^^^^^^

ATAOS
-----

The current implementation of the ATAOS performs automatic offsetting of the telescope based on the filter/grating selection.
However, the offsets get wiped out when changing targets.
This is best resolved by changing the spectrograph to use and empty filter/grating, then switching to the filter/grating of choice.

This issue is being addressed in `DM-24808 <https://jira.lsstcorp.org/browse/DM-24808>`__


..  Any Figures should be stored in the same directory as this file.
    To add images, add the image file (png, svg or jpeg preferred) to the same directory as this .rst file.
    The reST syntax for adding the image is:
    .. figure:: /filename.ext
        :name: fig-label
        :target: http://target.link/url
        Caption text.
