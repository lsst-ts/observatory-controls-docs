.. |author| replace:: *Erik Dennihy*
.. |contributors| replace:: *none*

.. _Managing-Common-Observing-Environment:

#####################################
Managing Common Observing Environment
#####################################

.. note::

    Managing the common observing environment requires authorization. 
    Please check with Tiago Ribeiro for access.

The common observing environment (also known as the obsenv) is a set of packages deployed on an nfs mount for quick access.
It is intended to serve as a central environment sourced by different control system interfaces to enable rapid development.  



These packages are sourced and used by:
- The Script Queue CSCs
- The nublado control interface
- Some individual CSCs for testing development. 

.. _obs-env_user:

The obs-env at the Summit and Test Stands
=========================================

Each instance of the control system maintains its own common observing environment. 
The common observing environments are not synced accross the sites, so changes to the common observing environment at the summit do not affect changes at the test stands and vice-versa.

The obs-env user and process control
====================================

The packages in the common observing environment contain many interdependencies (e.g. standardscripts importing from observatory_control), 
and as such carefuly deployment of test versions and control is required to keep the packages aligned. 
To limit the risk of package misalignment, we create the obs-env user to manage the observing environment.  

The obs-env user is the only user available to use the manage_obs_env program.
All commands submitted by the obs-env user are recorded to allow capturing the history. 
In order to run the mange_obs_env program, you must first log in as the obs_env user. 

.. _manage_obs_env-program:

Using the manage_obs_env program
================================

These packages are managed by a program called manage_obs_env which can only be executed by the obsenv user. 
The manage_obs_env program is setup to automatically handle all of the github commands required to setup the environment. 
It is configured as a set of actions. 

A full list of available actions can be seen by running manage_obs_env --help.
Some useful actions are:
* --reset: this resets the environment to its base branch, essentially undoing any changes
* --checkout-branch: this action can be use to checkout a branch in a specific repository
* --show-current: this will print a list of all current repositories. 

Using the run branches for development and deployment
=====================================================

To enable collaborative and development, we use the concept of a "run branch" to deploy temporary changes to packages in the common observing environment.
The run branches are public branches with a two-week life cycle that can be used to deploy hotfixes, patches, and in limited cases new required capabilities. 
At the end of the two-week lifecycle, then run branch will be closed using a review and pull request process appropriate for the repository and desired changes may be adopted/merged back into the develop/main branch of the repository. 
The run branches are NOT intended to replace the approved development/testing/deployment cycle for new features, they are strictly to be used when expediency is required. 

Some common use cases of the run branches include:
- Applying a hotfix for a bug in a script that was discovered and is needed to continue operations. 
- Addition of a new observing block that has been tested separately at the test stands. 
- Applying a temporary change needed to run a test at the summit. A second commit overwriting the change would be appropriate.
- Applying a temporary patch while a long-term solution is being developed. The expectation is that this commit would be removed at the end of the run branch lifecycle.  

Some un-allowed uses of the run branch include:
- Deployment of a new sal script which has not completed review/testing.
- Using the run branch to merge a new feature which was developed as part of a separate ticket branch. 

Since the run branches are collaborative and public, anyone can push commits to the remote repository at any time. 
As such, it is paramount that users follow some best practices for shared development. 
- NEVER rebase the run the branch of a repository unless you are absolutely sure it is necessary. 
If you need to pickup commits from a different branch, or even pickup some recently merged changes, consider cherry-picking commits instead to preserve the linear history of the run branch. 
- NEVER force push your commits to the remote repository. 
In doing so, you stand to overwrite commits pushed by your colleague and could erase important patches. 
- Always pull changes from the remote repository before pushing your local changes. 

In addition, since it is a collaborative branch, the process of closing a run branch and deciding what changes to keep/drop is inherently difficult. 
The most effective strategy to avoid confusion is to write clear and direct commit messages e.g. instead of "fix typo" please expand to say "In auxtel/atmcs.py, fix typo in docstring in slew_icrs method.". 

When possible, please use the git --fixup command to enable auto-squashing of commits. 
This avoids all ambiguity of what features/patches are common and should be squashed during merging. 
