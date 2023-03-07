.. This is a template top-level index file for a directory in the procedure's arm of the documentation

.. This is the label that can be used as for cross referencing in the given area
.. Recommended format is "Directory Name"-"Title Name"  -- Spaces should be replaced by hypens
.. _Writing-SAL-Scripts:

###################
Writing SAL Scripts
###################

This page contains and example of how to convert a Jupyter notebook with an observatory control operation into a SAL Script that can run in the ScriptQueue.
Having the ability to execute SAL Script via the ScriptQueue is recommended when an operation will be executed either multiple times, in concert with other SAL Scripts, or to make it readily available to others.

If this is the first time you are contributing to the observatory control software, it is highly recommend that you take a look at the `development guidelines`_.

.. _development guidelines: https://tssw-developer.lsst.io/

.. _Writing-SAL-Scripts-Starting-From-a-Jupyter-Notebook:

Starting From a Jupyter Notebook
--------------------------------

You most likely started by writing a Jupyter notebook and had the chance to run it a couple time on-sky.
You now want to turn that in to a SAL Script that can be maintained, incorporated to the observatory operation routine and launched from the ScriptQueue.

This procedure follows from a real case scenario where a user develops an operation that dithers the telescope in a random pattern and performs a series of observations at each position.
As anticipated in the `Concept of Operations`_, the procedure was first developed using a Jupyter notebook, and tested in one of the `Operational Environments`_ (including on sky tests).

.. _Concept of Operations: https://tstn-024.lsst.io/
.. _Operational Environments: https://obs-ops.lsst.io/Observing-Interface-Setup/environments.html

To illustrate this example we created an :ref:`example notebook <example-notebook-writing-a-sal-script>`, which can now be converted into a SAL Script.
We recommend looking at this example and making sure you understand what is being performed by the Jupyter notebook.
Most importantly, make sure you understand how the observatory control classes are setup (``atcs`` and ``latiss``), how we parameterize the operation (defining the target and the observation setup) and how the operation is performed.
It may also be helpful to have the Jupyter notebook opened on the side as you read through he process of converting it into a SAL Script.

.. _Writing-SAL-Scripts-Initial-SAL-Script:

Initial SAL Script
------------------

The first stage of the process of writing a SAL Script consists basically of; identifying which repository to host it and creating the initial modules to develop the code.

SAL Scripts are hosted in two main repositories; `external scripts`_ and `standard scripts`_.
The initial entry-point for SAL Scripts is, usually, the `external scripts`_ repository.
More instructions about the repository structure can be found in the `tstn-010`_.

.. _external scripts: https://github.com/lsst-ts/ts_externalscripts
.. _standard scripts: https://github.com/lsst-ts/ts_standardscripts
.. _tstn-010: https://tstn-010.lsst.io/

Because this SAL Script is not going to be used as part of regular operations, and the functionality is still in development, it should be located in the `external scripts`_ repository.
To get started you need to clone the `external scripts`_ repository.

.. prompt:: bash

  git clone https://github.com/lsst-ts/ts_externalscripts.git

Development must be done on "ticket" branches so you will also have to create a ticket in `Jira`_ to track your work.

.. _Jira: https://jira.lsstcorp.org/

Once issued you can create a "ticket branch" to work on that is consistent with the name of the JIRA ticket, e.g.;

.. prompt:: bash

  cd ts_externalscripts/
  git checkout tickets/DM-27242

Most tickets are created under the Data Management (DM) Jira project.
If you are working on a different project, use the appropriate ticket handle.

The SAL Scripts repositories are organized such that:

1.  The actual code is hosted in the ``python/lsst/ts/externalscripts/`` sub directory.
2.  For each SAL Script there must be an executable in the ``scripts/`` directory that executes the code.
    The format will be shown furthermore.

The :ref:`example notebook <example-notebook-writing-a-sal-script>` we created was written for the Auxiliary Telescope.
Therefore, you can create the python file to host the SAL Script code in ``python/lsst/ts/externalscripts/auxtel/``.
Let us call the file ``slew_dither.py``, e.g. ``python/lsst/ts/externalscripts/auxtel/slew_dither.py``.

.. note::

  We recommend using an Integrated Development Environment (IDE) for software development, but you can also use your preferred code/text editor (e.g. vi/vim, emacs, etc.).
  `PyCharm`_ is a good IDE for Python development.
  `Atom`_, `Sublime`_ and `Visual Studio Code`_ are good graphical code editors.
  For help setting up some of the most popular code editors visit the `editors section`_ of the DM developer guidelines.


.. _PyCharm: https://www.jetbrains.com/pycharm/
.. _Atom: https://atom.io/
.. _Sublime: https://www.sublimetext.com/
.. _Visual Studio Code: https://code.visualstudio.com/
.. _editors section: https://developer.lsst.io/index.html#editors

The first step in the process is setting up the import statements.
We already know most of the libraries needed to run the script from the notebook, so we can go ahead and copy those to the file.

Next we want to create a class to host the SAL Script.
All SAL Scripts must subclass `salobj.BaseScript`_ and they must also implement a couple of abstract methods.

.. _salobj.BaseScript: https://ts-salobj.lsst.io/py-api/lsst.ts.salobj.BaseScript.html#lsst.ts.salobj.BaseScript

The skeleton of the SAL Script will look like the following:

.. code-block:: python
  :linenos:

  import asyncio
  import logging
  import yaml

  import numpy as np
  from matplotlib import pyplot as plt

  from lsst.ts import salobj

  from lsst.ts.observatory.control.auxtel.atcs import ATCS
  from lsst.ts.observatory.control.auxtel.latiss import LATISS
  from lsst.ts.observatory.control.utils.enums import RotType

  __all__ = ["SlewDither"]


  class SlewDither(salobj.BaseScript):
    """ Slew and dither SAL Script.

    The class documentation must be written here. You should explain what is
    the purpose of the script, what it does and all other important details
    for users.
    We adopt numpy docstring formatting (https://numpydoc.readthedocs.io/en/latest/format.html).

    Parameters
    ----------
    index : `int`
        Index of Script SAL component.

    Notes
    -----
    **Checkpoints**



    **Details**

    Add details here....

    """

    def __init__(self, index=1):

        super().__init__(
            index=index,
            descr="Add short description here. This is published in the "
                  "description field of the Script description event.",
        )

        # Instantiate atcs and latiss. We need to do this after the call to
        # super().__init__() above. We can also pass in the script domain and
        # logger to both classes so log messages generated internally are
        # published to the efd.
        self.atcs = ATCS(domain=self.domain, log=self.log)
        self.latiss = LATISS(domain=self.domain, log=self.log)

    @classmethod
    def get_schema(cls):
        return {}

    async def configure(self, config):
      """
      """

    def set_metadata(self, metadata):
      """
      """
        pass

    async def run(self):
      pass

Once you created the file to host the SAL Script code, you will also have to update the ``__init__.py`` file to allow Python to import it.
The ``__init__.py`` file should be co-located with the file you created above.
In this case, we are hosting the code in ``python/lsst/ts/externalscripts/auxtel/slew_dither.py``, so we must edit ``python/lsst/ts/externalscripts/auxtel/__init__.py``.
For the SAL Script above, the entry would look like:

.. code-block:: python

  from .slew_dither import *

Which is basically the name of the file, without the trailing ``.py``.

Executable
^^^^^^^^^^

The last step in the process is to create the executable file in the ``python/lsst/ts/externalscripts/data/scripts/`` directory.
This is the file that is actually executed by the ``ScriptQueue`` when running the SAL Script.
Here we also maintain the same directory hierarchy of the modules, so an Auxiliary Telescope SAL Script should be created under the ``auxtel`` directory.
It is also a good idea to create the executable file with the same name as that of the SAL Script.
In this case, we create ``python/lsst/ts/externalscripts/data/scripts/slew_dither.py``.

The content of this file should be as follows:

.. code-block:: python
  :linenos:

  #!/usr/bin/env python
  # This file is part of ts_externalscripts
  #
  # Developed for the LSST Telescope and Site Systems.
  # This product includes software developed by the LSST Project
  # (https://www.lsst.org).
  # See the COPYRIGHT file at the top-level directory of this distribution
  # for details of code ownership.
  #
  # This program is free software: you can redistribute it and/or modify
  # it under the terms of the GNU General Public License as published by
  # the Free Software Foundation, either version 3 of the License, or
  # (at your option) any later version.
  #
  # This program is distributed in the hope that it will be useful,
  # but WITHOUT ANY WARRANTY; without even the implied warranty of
  # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  # GNU General Public License for more details.
  #
  # You should have received a copy of the GNU General Public License

  import asyncio

  from lsst.ts.externalscripts.auxtel import SlewDither

  asyncio.run(SlewDither.amain())

A couple things worth mentioning in the file above:

1.  The first line

    .. code-block:: python

      #!/usr/bin/env python

  Must always be present.
  It tells the operating system that the file being executed is a Python script.

2.  The entry between ``from`` and ``import`` statements in line 24 is derived from the location of your SAL script in the package where the leading ``python`` is removed and ``.`` replaces ``/`` (e.g.; ``python/lsst/ts/externalscripts/auxtel/`` becomes ``lsst.ts.externalscripts.auxtel``).

3.  The name after the ``import`` statement in line 24 is the name of the class you created, e.g. ``SlewDither``.

4.  The call in line 26 is basically the name of the class, ``SlewDither`` (imported in line 24), followed by ``.amain()``.
    Check `Python Script file documentation <https://ts-salobj.lsst.io/sal_scripts.html#python-script-file>`__ in SalObj for a more detailed description.

Once this file is created, we must also make sure it is "executable" by all users.
You can do that from the command line with the following command:

.. prompt:: bash

  chmod a+x python/lsst/ts/externalscripts/data/scripts/slew_dither.py

Alternatively, you can also change the permission of the file after adding it to the git repository with the following command:

.. prompt:: bash

  git update-index --chmod=+x python/lsst/ts/externalscripts/data/scripts/slew_dither.py

.. _Writing-SAL-Scripts-Configuration-Schema:

Configuration Schema
--------------------

Now that we have a base Python module, we are ready to start filling it up with some code.

The first step is probably to write a configuration schema for the SAL Script.
For this we will need to carefully inspect the Jupyter notebook, and identify what are the inputs to the SAL Script.

The schema is written using `json schema`_ in the ``get_schema`` method of the class.
We write the schema as a string and convert it to a dictionary using Python's ``yaml`` library.
Although json schema can be a bit intimidating at the start, it is straightforward to write some simple (and even more complex) schemas once you understand the basic principles.

.. _json schema: https://json-schema.org/

We start with a simple header, that will be common to all configuration scheme:

.. code-block:: python

  schema = """
  $schema: http://json-schema.org/draft-07/schema#
  $id: https://github.com/lsst-ts/ts_externalscripts/blob/master/python/lsst/ts/externalscripts/auxtel/slew_dither.py
  title: SlewDither v1
  description: Configuration for SlewDither SAL Script.
  """

As you can see from the code snippet above, the header consists of some basic schema definitions plus some information about the schema itself.
Let's break down the schema header line-by-line:

1.  The first entry (``$schema``) contains the version of the json schema specification; we adopt "draft-07".
2.  The second line contains a link to the file where the schema is defined.
    Note that the path above will not exists until we actually make a release, e.g. merge the code back to the master branch.
3.  The third line contains the "title" of the schema, which consists of the name of the script plus a    version of the configuration.
    Make sure you version the schema appropriately (using `semantic versioning`_), as this provides a way for us to track down configuration versions.
4.  Next we add a short description of the configuration.
    Basically a phrase explaining what this schema is for.

.. _semantic versioning: https://semver.org/

We are now ready to add more content to the configuration file.
The first thing to keep in mind is that json schema provides a way of specifying data structures.
A data structure is basically a collection of "data types", that can contain a name and additional attributes.

To start we have to define the type of the data structure that will contain the configuration schema.
For that we always use the "``object``" type.
We will also want to restrict the configuration to only allow input information for the entries defined in the configuration, which is done via a modifier attribute called "``additionalProperties``".

With these additions our schema will now look like this:

.. code-block:: python

  schema = """
  $schema: http://json-schema.org/draft-07/schema#
  $id: https://github.com/lsst-ts/ts_externalscripts/blob/master/python/lsst/ts/externalscripts/auxtel/slew_dither.py
  title: SlewDither v1
  description: Configuration for SlewDither SAL Script.
  type: object
  additionalProperties: false
  properties:
    ...
  """

So far we have defined the top level structure of the configuration schema.
The next step is to fill the ``properties`` section of this top level ``object`` with the configuration structure.
Each entry will consist of the following:

.. code-block:: python

  """
  <parameter-name>:
    type: <type>
    description: <description of the parameter>
    <additional modifiers>
  """

By inspecting the :ref:`example notebook <example-notebook-writing-a-sal-script>`, we can clearly identify these as input parameters:

``target_name``
  A string with the name of the target.

  .. code-block:: python

    """
    target_name:
      type: string
      description: >-
        Target name. Must be a valid target identifier in
        Simbad (http://simbad.u-strasbg.fr/simbad/sim-fid).
    """

  Note in the ``description`` field how we can add long, multi-line descriptions by placing the >- on the first line and indenting from the "description" attribute.

``rot_value``
  Float with the rotator positioning value.

  .. code-block:: python

    """
    rot_value:
      description: >-
        Rotator position value. Actual meaning depends on rot_type.
      type: number
      default: 0
    """

  A ``float`` is defined as ``type: number``.

  Note we can add default values to entries (e.g. ``default: 0``).
  This means that, if the value is not encountered in the user-provided configuration, it will receive the value specified in this field.

``rot_type``
  Enumeration defining how to threat ``rot_value``.
  See `RotType`_ documentation.

  .. code-block:: python

    """
    rot_type:
      type: string
      enum: ["Sky", "SkyAuto", "Parallactic", "PhysicalSky", "Physical"]
      default: PhysicalSky
      description: >-
        Rotator strategy. Options are:
          Sky: Sky position angle strategy. The rotator is positioned with respect
               to the North axis so rot_angle=0. means y-axis is aligned with North.
               Angle grows clock-wise.

          SkyAuto: Same as sky position angle but it will verify that the requested
                   angle is achievable and wrap it to a valid range.

          Parallactic: This strategy is required for taking optimum spectra with
                       LATISS. If set to zero, the rotator is positioned so that the
                       y-axis (dispersion axis) is aligned with the parallactic
                       angle.

          PhysicalSky: This strategy allows users to select the **initial** position
                        of the rotator in terms of the physical rotator angle (in the
                        reference frame of the telescope). Note that the telescope
                        will resume tracking the sky rotation.

          Physical: Select a fixed position for the rotator in the reference frame of
                    the telescope. Rotator will not track in this mode.
    """

  This is a good example of a complex data definition.
  We define an entry of ``type: string``, with an ``enum`` modifier and also give it a default value, so users will not need to define it all the time.
  Furthermore, we also take advantage of long format ``description`` to add substantial information about the parameter.

``n_grid``
  Integer specifying the number of visits in the grid.

  .. code-block:: python

    """
    n_grid:
      type: integer
      minimum: 1
      description: Integer specifying the number of visits in the grid.
    """

  This is an example of specifying an integer instead of a number (which can be both integer and float).
  We also limit the value of this parameter to be equal to or larger than one.

``exptime``
  List of floats with the exposure time for each exposure.

  .. code-block:: python

    """
    exptime:
      type: array
      minItems: 1
      items:
        type: number
        exclusiveMinimum: 0
      description: List of exposure times (in seconds) for each visit.
    """

  This is a good example of how we define arrays in json schema.
  In addition to adding the ``type: array``, we can also specify additional information about the number of items (must be at least 1, e.g. ``minItems``) and we define properties for the values (floats larger than zero).

``obs_filter``
  List of strings with the names of the filters for each exposure.

  .. code-block:: python

    """
    obs_filter:
      type: array
      minItems: 1
      items:
        type: string
      description: List of filter names for each exposure.
    """


``obs_grating``
  List of strings with the names of the gratings for each exposure.

  .. code-block:: python

    """
    obs_grating:
      type: array
      minItems: 1
      items:
        type: string
      description: List of grating names for each exposure.
    """

.. note::

  Unfortunately json schema does not offer a way to cross check entries in the schema.
  That means we can not verify at this level that ``exptime``, ``obs_filter`` and ``obs_grating`` will have the same size.

  There is, in fact, a away around this but it will make the schema considerably harder.
  If you are interested in seeing how this can be accomplished see the :ref:`self consistent schema <Self-Consistent-Schema>` page.


.. _RotType: https://ts-observatory-control.lsst.io/py-api/lsst.ts.observatory.control.RotType.html#rottype

Finally, we can also specify which configuration parameters **must** be specified in any configuration.
That is done using the ``required`` keyword on the top level.


.. code-block:: python

  schema = """
  required: [target_name, exptime, obs_filter, obs_grating]
  """

The full configuration schema, added to the ``get_schema`` method in the class, will look like this:

.. code-block:: python

  @classmethod
  def get_schema(cls):
    schema = """
    $schema: http://json-schema.org/draft-07/schema#
    $id: https://github.com/lsst-ts/ts_externalscripts/blob/master/python/lsst/ts/externalscripts/auxtel/slew_dither.py
    title: SlewDither v1
    description: Configuration for SlewDither SAL Script.
    type: object
    additionalProperties: false
    required: [target_name, exptime, obs_filter, obs_grating]
    properties:
      target_name:
        type: string
        description: Target name. Must be a valid target identifier in Simbad.
      rot_value:
        description: >-
          Rotator position value. Actual meaning depends on rot_type.
        type: number
        default: 0
      rot_type:
        type: string
        enum: ["Sky", "SkyAuto", "Parallactic", "PhysicalSky", "Physical"]
        default: PhysicalSky
        description: >-
          Rotator strategy. Options are:
            Sky: Sky position angle strategy. The rotator is positioned with respect
                 to the North axis so rot_angle=0. means y-axis is aligned with North.
                 Angle grows clock-wise.

            SkyAuto: Same as sky position angle but it will verify that the requested
                     angle is achievable and wrap it to a valid range.

            Parallactic: This strategy is required for taking optimum spectra with
                         LATISS. If set to zero, the rotator is positioned so that the
                         y-axis (dispersion axis) is aligned with the parallactic
                         angle.

            PhysicalSky: This strategy allows users to select the **initial** position
                          of the rotator in terms of the physical rotator angle (in the
                          reference frame of the telescope). Note that the telescope
                          will resume tracking the sky rotation.

            Physical: Select a fixed position for the rotator in the reference frame of
                      the telescope. Rotator will not track in this mode.
      n_grid:
        type: integer
        minimum: 1
        description: Integer specifying the number of visits in the grid.
      exptime:
        type: array
        minItems: 1
        items:
          type: number
          exclusiveMinimum: 0
        description: List of exposure times (in seconds) for each visit.
      obs_filter:
        type: array
        minItems: 1
        items:
          type: string
        description: List of filter names for each exposure.
      obs_grating:
        type: array
        minItems: 1
        items:
          type: string
        description: List of grating names for each exposure.
  """

  return yaml.safe_load(schema)

.. _Writing-SAL-Scripts-Handling-Configuration:

Handling Configuration
----------------------

Having the configuration schema defined we now must implement how the SAL Script handle the input configuration.
This operation is handled by the ``configure`` method.
The method receives the configuration as a ``type.SimpleNamespace`` Python object.

In the configuration schema written above, we noted that the schema is not verifying that the sizes of the input arrays (e.g. ``exptime``, ``obs_filter`` and ``obs_grating``) are consistent.
That means we need to do it in the ``configure`` method.

With all that in consideration the ``configure`` method would look like this:

.. code-block:: python

  async def configure(self, config):
    """Handle script input configuration.

    Parameters
    ----------
    config: `types.SimpleNamespace`
      Configuration data. See `get_schema` for information about data
      structure.

    Raises
    ------
    RuntimeError:
      If sizes of the configuration arrays (exptime, obs_filter and
      obs_grating) are different.

    """

    # Check that exptime, obs_filter and obs_grating have the same time.
    # Raise RuntimeError exception if not.

    if not (len(config.exptime) == len(config.obs_filter) == len(obs_grating)):
        raise RuntimeError(
            f"Inconsistent size of arrays: exptime: {len(config.exptime)}, "
            "obs_filter: {len(config.obs_filter)}, obs_grating: {len(obs_grating)}."
        )

    # We can also log information about the configuration

    self.log.debug(
        f"target_name: {config.target_name}, rot_value: {config.rot_value}, "
        f"n_grid: {config.n_grid}, rot_type: {config.rot_type}, exptime: {config.exptime}, "
        f"obs_filter: {config.obs_filter}, obs_grating: {config.obs_grating}."
    )

    # Finally, let's just copy config to the class.

    self.config = config

.. _Writing-SAL-Scripts-Metadata:

Metadata
--------

SAL Scripts provides a way to report information about itself to the system.
These includes, amongst other things estimated duration, position on the sky and instrument configuration.

The full set of metadata information is defined in the `Script.metadata`_ topic.

.. _Script.metadata: https://ts-xml.lsst.io/sal_interfaces/Script.html#metadata

Here we concentrate on filling up the most basic information, the estimated duration.
This information is used by LOVE to provide feedback to the users about the execution progress.
The metadata information is handled in the ``set_metadata`` method of the SAL Script:

.. code-block:: python

  def set_metadata(self, metadata):
    """Set estimated duration of the script.
    """
    # Add 30s for slew
    estimated_slew_time = 30.

    # Estimate time taking data; basically sum the exposure times
    data_duration = np.sum(self.config.exptime)

    metadata.duration = estimated_slew_time + data_duration

It is helpful to have reasonable time estimates as they are displayed via LOVE and watched by observers.

.. _Writing-SAL-Scripts-The-run-Method:

The ``run`` Method
------------------

The ``run`` method in the SAL Script is responsible for executing the operation, it is called once the script "transitions" to "running" state.

Having developed the procedure in the notebook already, we can simply transfer the code to this method.
We will also have perform some minor modifications to use the configuration parameters.

Furthermore, we may also want to add some ``checkpoints`` to the process.
These are calls done in the ``run`` method (you can not use them in other places of the code) of a SAL Script where it is possible to pause the execution.

Taking all that into consideration, this is what the ``run`` method of this SAL Script would look like:

.. code-block:: python
  :linenos:

  async def run(self):

    self.log.debug(
      f"Slew to {self.config.target_name} with "
      f"rot_value: {self.config.rot_value} and rot_type: {self.config.rot_type}"
    )

    await atcs.slew_object(
        name=self.config.target_name,
        rot=self.config.rot_value,
        rot_type=self.config.rot_type
      )

    # After slew is a good idea to add a checkpoint.
    await self.checkpoint("Slew finished")

    # Compute grid
    grid_x = (np.random.rand(self.config.n_grid)-0.5)*120.
    grid_y = (np.random.rand(self.config.n_grid)-0.5)*120.

    for iter, xx, yy in zip(range(self.config.n_grid), grid_x, grid_y):

      # Let's add some debugging messages
      self.log.debug(
        f"Starting iteration {iter+1} of {self.config.n_grid}: "
        f"offset x/y: {xx},{yy} arcsec."
      )

      # We may also want to add a checkpoint at the start of each iteration
      await self.checkpoint(f"iter[{iter+1}/{self.config.n_grid}]")

      # Offset telescope
      # Use non-relative offset as they are easier to reset
      await atcs.offset_xy(x=xx, y=yy, relative=False)

      # Take data
      for etime, flt, grt in zip(
          self.config.exptime, self.config.obs_filter, self.config.obs_grating
      ):
        # We can also add checkpoints at before every image, this will give us
        # more granularity in controlling the script.
        await self.checkpoint(
          f"iter[{iter+1}/{self.config.n_grid}]: "
          f"exptime: {etime}, filter: {flt}, grating: {grt}"
        )
        await latiss.take_object(exptime=etime, filter=flt, grating=grt)

    # Reset offset
    await atcs.offset_xy(x=0., y=0., relative=False)

Once this is completed you are pretty much done.
The full source for the SAL Script worked in this example can be found here.

.. _Writing-SAL-Scripts-Unit-Testing:

Unit Testing
------------

One of the advantages of writing operations as SAL Scripts instead of Jupyter notebooks is that it is simpler to write unit tests for them.
Unit tests reassure us about the integrity of the code its maintainability.
If something changes in the underlying libraries that will affect the software, unit tests help us capture those issues early and apply corrections.

Some of the basic unit testing required for SAL Scripts are:

1. Test executable.
2. Test configuration integrity.

In addition one may extend the basic unit testing so it will also:

1. Test the run method.
2. If applicable, test edge cases.

Unit tests should be added to the ``tests`` folder in the package root.
Any unit test added to this folder will run as part of the CI job in `Telescope and Site Jenkis server`_,
and all unit tests must pass in order for a Pull Request to be merged.

.. _Telescope and Site Jenkis server: https://tssw-ci.lsst.org/

A basic unit test for this SAL Script would look like this:

.. code-block:: python

  # This file is part of ts_externalscripts
  #
  # Developed for the LSST Telescope and Site Systems.
  # This product includes software developed by the LSST Project
  # (https://www.lsst.org).
  # See the COPYRIGHT file at the top-level directory of this distribution
  # for details of code ownership.
  #
  # This program is free software: you can redistribute it and/or modify
  # it under the terms of the GNU General Public License as published by
  # the Free Software Foundation, either version 3 of the License, or
  # (at your option) any later version.
  #
  # This program is distributed in the hope that it will be useful,
  # but WITHOUT ANY WARRANTY; without even the implied warranty of
  # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  # GNU General Public License for more details.
  #
  # You should have received a copy of the GNU General Public License

  import random
  import unittest

  import numpy as np

  from lsst.ts import salobj
  from lsst.ts.standardscripts import BaseScriptTestCase
  from lsst.ts.externalscripts import get_scripts_dir
  from lsst.ts.externalscripts.auxtel import SlewDither

  class TestSlewDither(BaseScriptTestCase, unittest.IsolatedAsyncioTestCase):

    async def basic_make_script(self, index):
      self.script = SlewDither(index=index)
      return [self.script, ]

    async def test_configure_errors(self):
      """Test error handling in the do_configure method."""

      async with self.make_script():

        # Check schema validation.
        for bad_config in (
            {},  # need target_name, exptime, obs_filter, obs_grating
            {"target_name": "HD 164461"},  # need exptime, obs_filter, obs_grating
            {"target_name": "HD 164461", "exptime": [1., 2.]},  # need obs_filter, obs_grating
            {"target_name": "HD 164461", "exptime": [1., 2.], "obs_filter": ["filter_1", "filter_2"]},  # need  obs_grating
            {"target_name": "HD 164461", "n_grid": 0 , "exptime": [1., 2.], "obs_filter": ["filter_1", "filter_2"], "obs_grating": ["grating_1", "grating_2"]},  # n_grid >= 1
            {"target_name": "HD 164461", "exptime": [0., 2.], "obs_filter": ["filter_1", "filter_2"], "obs_grating": ["grating_1", "grating_2"]},  # exptime can't be zero.
            {"target_name": "HD 164461", "exptime": [1., 2.], "obs_filter": ["filter_1", "filter_2"], "obs_grating": ["grating_1", "grating_2"], "rot_type": "BADVALUE"},  # Bad rot_type
        ):
          with self.subTest(bad_config=bad_config):
            with self.assertRaises(salobj.ExpectedError):
              await self.configure_script(**bad_config)

        # Check configuration fails if exptime/obs_filter/obs_grating have
        # different sizes. Note that the exception raised by the SAL Script is
        # going to be different in this case. So, we need to check it
        # separately
        for bad_config in (
            {"target_name": "HD 164461", "exptime": [1.], "obs_filter": ["filter_1", "filter_2"], "obs_grating": ["grating_1", "grating_2"]},  # wrong exptime size
            {"target_name": "HD 164461", "exptime": [1., 2.], "obs_filter": ["filter_1", ], "obs_grating": ["grating_1", "grating_2"]},  # wrong obs_filter size
            {"target_name": "HD 164461", "exptime": [1., 2.], "obs_filter": ["filter_1", "filter_2"], "obs_grating": ["grating_1", ]},  # wrong obs_grating size
        ):
          with self.subTest(bad_config=bad_config):
            with self.assertRaises(salobj.RuntimeError):
              await self.configure_script(**bad_config)


    async def test_configure_good(self):
      """Test configure method with valid configurations."""
      async with self.make_script():

        target_name = "HD 164461"
        rot_value = 45.
        rot_type = "SkyAuto"

        n_grid = 10
        n_exp = 4
        # generate n_grid random numbers between [0, 10).
        exptime = np.random.rand(n_exp)*10
        # generate n_grid array with filter_1 -> filter_3
        obs_filter = [f"filter_{i%4+1}" for i in range(n_exp)]
        # generate n_grid array with grating_1 -> grating_3
        obs_grating = [f"grating_{i%4+1}" for i in range(n_exp)]

        # Basic providing only target_name, exptime, obs_filter, obs_grating
        await self.configure_script(
            target_name=target_name,
            n_grid=n_grid,
            exptime=exptime,
            obs_filter=obs_filter,
            obs_grating=obs_grating
          )

        # Check configuration was correctly loaded
        self.assertEqual(self.script.config.target_name, target_name)
        self.assertEqual(self.script.config.rot_value, 0.)  # check default
        self.assertEqual(self.script.config.rot_type, "PhysicalSky")  # check default
        self.assertEqual(self.script.config.n_grid, n_grid)
        self.assertEqual(self.script.config.exptime, exptime)
        self.assertEqual(self.script.config.obs_filter, obs_filter)
        self.assertEqual(self.script.config.obs_grating, obs_grating)

        # Same as before but now lets also provide rot_value and rot_type
        await self.configure_script(
            target_name=target_name,
            rot_value=rot_value,
            rot_type=rot_type,
            n_grid=n_grid,
            exptime=exptime,
            obs_filter=obs_filter,
            obs_grating=obs_grating
          )

        # Check configuration was correctly loaded
        self.assertEqual(self.script.config.target_name, target_name)
        self.assertEqual(self.script.config.rot_value, rot_value)
        self.assertEqual(self.script.config.rot_type, rot_type)
        self.assertEqual(self.script.config.n_grid, n_grid)
        self.assertEqual(self.script.config.exptime, exptime)
        self.assertEqual(self.script.config.obs_filter, obs_filter)
        self.assertEqual(self.script.config.obs_grating, obs_grating)


    async def test_executable(self):
      scripts_dir = get_scripts_dir()
      script_path = scripts_dir / "slew_dither.py"
      await self.check_executable(script_path)

  if __name__ == "__main__":
      unittest.main()

One thing to notice in the unit test above is the use of ``BaseScriptTestCase`` from ``ts_standardscript``, even though we are writing the SAL Script in ``ts_externalscripts``.
This is an utility class that provides a lot of the functionality needed for developing unit tests for SAL Scripts.

Furthermore, as can be seen, the unit test written above is not testing the ``run`` method.
Implementing a check on this method is a bit more involving as it will require us to emulate both ``ATCS`` and ``LATISS`` classes.
Fortunately, there are a couple of classes provided by ``ts_observatory_control`` to support this.

To implement this tests we would have to make the following modifications:

1.  Import ATCSMock and LATISSMock from ts_observatory_control;

    .. code-block:: python

      from lsst.ts.observatory.control.mock import ATCSMock, LATISSMock

2.  Modify ``basic_make_group`` to instantiate both classes:

    .. code-block:: python

      async def basic_make_script(self, index):
        self.script = SlewDither(index=index)

        self.atcs_mock = ATCSMock()
        self.latiss_mock = LATISSMock()

        return [self.script, self.atcs_mock, self.latiss_mock]

3.  Add ``test_run``:

    .. code-block:: python

      async def test_run(self):

        async with self.make_script():

          # Need to enable all CSCs before test. The Script itself assumes
          # all CSCs are enabled so, in order to test we need to enable them
          # first. We can use the script own classes to do this and the mock
          # classes accepts any configuration.
          await self.script.atcs.enable()
          await self.script.latiss.enable()

          # To run the script we need to configure it first.
          target_name = "HD 164461"

          n_grid = 5
          n_exp = 3
          # generate n_grid random numbers between [0, 10).
          exptime = np.random.rand(n_exp)*10
          # generate n_grid array with filter_1 -> filter_3
          obs_filter = [f"filter_{i%4+1}" for i in range(n_exp)]
          # generate n_grid array with grating_1 -> grating_3
          obs_grating = [f"grating_{i%4+1}" for i in range(n_exp)]

          # Basic providing only target_name, exptime, obs_filter, obs_grating
          await self.configure_script(
              target_name=target_name,
              exptime=exptime,
              n_grid=n_grid,
              obs_filter=obs_filter,
              obs_grating=obs_grating
            )

          # Now we are ready to run it

          await self.run_script()

          # We could implement some checks here but if the script runs
          # successfully we are probably done!


.. _Writing-SAL-Scripts-Next-Steps:

Next Steps
----------

In the SAL Script above we purposefully left some room for improvements.
There are at least two very clear cases;

1.  When we create the random x and y grid the "size" of the offset is fixed:

    .. code-block:: python

      grid_x = (np.random.rand(n_grid)-0.5)*120.

    The method ``np.random.rand(n_grid)`` generates a random number between 0 and 1, which means the code above will generate an offset between -60. and 60. arcsec.

    Would you be able to convert that into configuration parameter?

2.  In the ``run`` method, if something happens inside the outer ``for`` loop (starting in line 22), the telescope would probably be left with an applied offset.
    Can you think of a way to improve that?

.. _Writing-SAL-Scripts-See-Also:

See Also
--------

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    example-notebook/*
    schema_2/*
