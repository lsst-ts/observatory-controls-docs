.. Review the README in this procedure's directory on instructions to contribute.
.. Static objects, such as figures, should be stored in the _static directory. Review the _static/README in this procedure's directory on instructions to contribute.
.. Do not remove the comments that describe each section. They are included to provide guidance to contributors.
.. Do not remove other content provided in the templates, such as a section. Instead, comment out the content and include comments to explain the situation. For example:
	- If a section within the template is not needed, comment out the section title and label reference. Include a comment explaining why this is not required.
    - If a file cannot include a title (surrounded by ampersands (#)), comment out the title from the template and include a comment explaining why this is implemented (in addition to applying the ``title`` directive).

.. Include one Primary Author and list of Contributors (comma separated) between the asterisks (*):
.. |author| replace:: *Amanda Ibsen*
.. If there are no contributors, write "none" between the asterisks. Do not remove the substitution.
.. |contributors| replace:: *List-of-contributors*

.. This is the label that can be used as for cross referencing this procedure.
.. Recommended format is "Directory Name"-"Title Name"  -- Spaces should be replaced by hyphens.
.. _Setting-up-playlist-BTS:

.. Each section should includes a label for cross referencing to a given area.
.. Recommended format for all labels is "Title Name"-"Section Name" -- Spaces should be replaced by hyphens.
.. To reference a label that isn't associated with an reST object such as a title or figure, you must include the link an explicit title using the syntax :ref:`link text <label-name>`.
.. An error will alert you of identical labels during the build process.

########################################
Setting up a playlist for testing in BTS
########################################

For testing that requires using the Cameras at BTS, a playlist with simulated images is needed. There are several already available playlist, but ocassionally, one may desire to either update
or create a new one. This document describes how to go about it.

Setting up a playlist for LATISS
================================

Usually, when we play back images, they are played back from the DAQ 2-day store (named like that for legacy reasons), so they need to be loaded. The one exception to this (currently) is LATISS at BTS.
LATISS at BTS has no DAQ, so we emulate it using files on disk. This makes setting up a playlist somewhat different that the other cases.

1. Log into the machine where playlist are stored
-------------------------------------------------
The machine where playlists and images are stored in BTS for latiss is ``auxtel-fp01.ls.lsst.org``. You will need SSH access to this machine.

2. Copy the images needed for the new playlist
----------------------------------------------
The images for the new playlist need to be in ``.raw`` and ``.meta`` format. The easiest (and perhaps only) way  to generate these files currently is to extract them from the 
2-day store at the Summit on ``auxtel-fp01.cp.lsst.org``. Despite its name, a lot of old images are still stored there. 

* ``ssh`` into ``auxtel-fp01.cp.lsst.org``.
* Use ``store`` commands to access the store::

    connect lat
    ls raw/{image_id} # not do ls raw, as there is too much there
    readRaw raw/{image_id} /tmp #this will generate the .raw and .meta files and copy them to /tmp

* You can move those files to ``auxtel-fp01.ls.lsst.org`` via ``scp``. They need to be copied into the directory ``/data/data/auxtel/playlist-data/emu/``.

3. Set up the playlist
-----------------------
Playlits are plain text files that specify a directory and a list of images. They are in the directory ``/home/ccs/playlists``. Here is an example file::
    
    [ccs@auxtel-fp01 playlists]$ cat default.plist
    /data/data/auxtel/playlist-data/
    emu
    AT_O_20210218_000249
    AT_O_20210218_000250
    AT_O_20210218_000251
    ...

To define a new playlist simply create a new file in that directory listing the images you want to use. To verify the playlist was correctly set, you can use ``ccs-shell`` commands::

    ccs-shell
    set target ats-fp #for latiss
    listPlaylists

Your new playlist should appear there.

4. Verify that the playlist can be loaded
-----------------------------------------

To verify that the playlist can actually be used in ``LOVE``, try loading it by running the ``run_command`` script with the following configuration::

    component: ATCamera #for latiss
    cmd: play
    parameters:
        playlist: {playlist name}

Once loaded, you should be able to take images using the simulated playlist. See further information on how to do this in :ref:`Control-System-Upgrade-Deployment-Activities-Minimal-Testing`.
You can also verify that the correct images were used by visually inspecting them in ``https://base-lsp.lsst.codes/rubintv/base``.

