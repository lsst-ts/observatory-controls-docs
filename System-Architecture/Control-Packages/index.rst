.. This is a template top-level index file for a directory in the procedure's arm of the documentation

.. This is the label that can be used as for cross referencing in the given area
.. Recommended format is "Directory Name"-"Title Name"  -- Spaces should be replaced by hypens
.. _System-Architecture-Control-Packages:


.. note::
    This is a template file that is associated with a template directory structure.
    This note will be deleted when the section is properly populated


.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    */index
..    *

##########################
Control Packages & Classes
##########################

A control package/class is a high-level grouping of CSCs.
The idea is to create some coordinated control systems for the telescope that
are related to a particular purpose.
A couple of these purposes are control of the low-level telescope and control
of the entire observatory.
These packages become the telescope control system and observatory control system.
Another layer of packages are the telescope's imaging system and its calibration system.
These systems can be then used by the provided scripting system in
order to perform coordinated functionality of the observatory.
The control packages deal with performing actions with the observatory
such as rotating and moving the dome or telescope mount.
Another way to think about these packages is that they perform coordinated
actions with multiple CSCs from one command.
An official lsst-ts git repository has been created to store these packages.
As a result of the continuing development of the functionality of these
packages, they must have integration and unit tests written in order to be
considered safe for official observatory use.

.. so I am not sure what we are trying to descibe here.  The section is called Control Packages
.. and Classes, so I assume we are trying to define Classes?  Classes are essentially scripts that
.. have gone through riggerous testing (as utilities) and contain functionality that can be used
.. by more than one script.

Another level of packages will deal with helping to perform observing duties and
integrating with the Science Platform.
The observing duties packages are located in the lsst-ts git repo.
The science platform packages are located in the lsst-dm repo.
This level is considered a testing grounds for these utilities which could be
promoted to a official control package.

Control package description, link to dev area(s) and workflow

..  Any Figures should be stored in the same directory as this file.
    To add images, add the image file (png, svg or jpeg preferred) to the same directory as this .rst file.
    The reST syntax for adding the image is:
    .. figure:: /filename.ext
        :name: fig-label
        :target: http://target.link/url
        Caption text.
