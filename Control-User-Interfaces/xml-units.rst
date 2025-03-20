.. This is a template top-level index file for a directory in the procedure's arm of the documentation

.. This is the label that can be used as for cross referencing in the given area
.. Recommended format is "Directory Name"-"Title Name"  -- Spaces should be replaced by hypens
.. _XML-Units:

##################
XML Unit Standards
##################

.. Glossary of Terms

.. list-table:: Glossary of Terms
   :widths: 10 50

   * - CAP
     - Commissioning Activities Planning 
   * - CSC
     - Commandable SAL Component
   * - EFD
     - Engineering Facility Database
   * - SI
     - International System of Units
   * - TSSW
     - Telescope & Site Software
   * - XML
     - eXtensible Markup Language

.. Define policy pertaining to XML unit definitions

It is the policy of this Project to use the `International System of Units <https://www.nist.gov/pml/owm/metric-si/si-units>`_ (SI), by default, in all XML Unit definitions.
The Project recognizes that certain hardware and system constraints may require the use of units outside this standard.
For example, many hardware components measure pressure in the common Imperial units of psi, psia or psig (all variants of pounds per square inch).
Steps were taken to allow for exceptions in these cases.
The process for requesting an exception is defined in the Non-SI Unit Requests section of this document.

The Commandable SAL Component (CSC) interface definitions, the XML files, are located in the `ts_xml <https://github.com/lsst-ts/ts_xml>`_ repository.
This repo is maintained by the Telescope & Site Software (TSSW) team, but is utilized by the Project as a whole.
As such, this Unit Standards definition is published at the `Observatory Controls <https://obs-controls.lsst.io/index.html>`_ level, but is cross-linked to the `TSSW Developer Guide <https://tssw-developer.lsst.io/index.html>`_ for completeness.


XML Unit Standards Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Project elected to use the `Astropy Python library <https://docs.astropy.org/en/stable/units/>`_ to verify the units defined in the XML files conform to SI-standard.
Additionally, all XML formatting is defined by the schemas located in the `ts_xml <https://github.com/lsst-ts/ts_xml>`_ repository.
The enforcement of these content and formatting standards is done via the `unit tests <https://github.com/lsst-ts/ts_xml/tree/develop/tests>`_ that are run automatically with each new commit and pull request.
They can also be run manually by following the instructions located in the `ts_xml README <https://github.com/lsst-ts/ts_xml?tab=readme-ov-file>`_.

The Astropy library also contains utilities for unit conversion.
As such, it is possible to take non-SI units published by hardware components or third-party software tools and convert them to SI-units, in the CSC code, for the purpose of interface definitions and publishing to the Engineering Facility Database (EFD).
For example, to convert psi to Pa, the following code example can be used:

.. code-block:: python

   import astropy.units as u
   from astropy.units import imperial, misc

   def psi_to_pa(value: float) -> float:
       """Convert a value in PSI to a value in Pa.

       Parameters
       ----------
       value: `float`
           The value in PSI.

       Returns
       -------
       float
           The value in Pa.
       """
       quantity_in_psi = value * imperial.psi
       quantity_in_pa = quantity_in_psi.to(u.Pa)
       return quantity_in_pa.value

Non-SI Unit Requests
^^^^^^^^^^^^^^^^^^^^

To request the use of a non-SI unit, a request must be made at the weekly Commissioning Activities Planning (CAP) meeting.
The request must be made and approved BEFORE the changes are implemented.
Simply add an agenda item to the `Future Meetings <https://confluence.lsstcorp.org/display/LSSTCOM/Agenda+Items+for+Future+CAP+Meetings>`_ page, attend the specific meeting once accepted and present the case.
If approved, continue with the development process defined in the `TSSW Developer Guide <https://tssw-developer.lsst.io/index.html>`_, specifically the `Reporting Work for XML Release <https://tssw-developer.lsst.io/development-guidelines/xml/reporting-xml-release-work.html#reporting-xml-release-work>`_ section.

Types of Exceptions
-------------------

There are actually two ways to handle non-standard unit exceptions:

#. Improvements to the Astropy library.
#. Explicit unit test exceptions.

For the first case, there have been times when a conventional SI unit was not included in the Astropy definition.
In this case, a change request is made directly to the Astropy maintainers to add the unit to the library.
In the interim, until the change is released, the second method is used and then removed.

In the second case, the `unit test <https://github.com/lsst-ts/ts_xml/blob/develop/tests/test_Units.py>`_ that verifies unit conformity is updated to allow for the non-standard unit.
Either the unit is added to the NONSTANDARD_UNITS list, or it is added to the local instance of the Astropy library using the tools provided by the library itself.
Examples of both methods can be found in the unit test file linked above.

Any changes to the unit test constitute a change to the ts_xml package, and therefore must follow the development guidelines before being released.

