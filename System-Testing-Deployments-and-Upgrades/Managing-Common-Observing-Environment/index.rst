.. |author| replace:: *Erik Dennihy*
.. |contributors| replace:: *none*

.. _Managing-Common-Observing-Environment:

#####################################
Managing Common Observing Environment
#####################################

.. note::

    Managing the common observing environment requires authorization. 
    Please check with Tiago Ribeiro for access.

The common observing evironment (obs-env) is a set of packages deployed on the nfs mount for quick access.
These packages are managed by a package called manage_obs_env which can only be executed by the obsenv user. 

.. _obs-env_user:

The obs-env user
================

The obs-env user is the super use available to use the manage_obs_env program.
All commands submitted by the obs-env user are recorded to allow capturing the history. 
In order to run the mange_obs_env program, you must fisrt log in as the obs_env user. 

.. _manage_obs_env-program:

Using the manage_obs_env program
================================

The manage_obs_env program is setup to automatically handle all of the github commands required to setup the environment. 
It is configured as a set of actions. 
A full list of available actions can be seen by running manage_obs_env --help.
Some useful actions are:
* --reset: this resets the environment to its base branch, essentially undoing any changes
* --checkout-branch: this action can be use to checkout a branch in a specific repository
* --show-current: this will print a list of all current respositories. 
