.. _System-Architecture-Supporting-Infrastructure:

#########################
Supporting Infrastructure
#########################

Storage Retention Policies
^^^^^^^^^^^^^^^^^^^^^^^^^^

Summit
------

.. list-table:: Retention Policies
   :widths: auto
   :header-rows: 1

   * - Content
     - Retention (days)
     - Provider
     - Server
   * - AuxTel Raw Images (Butler)
     - 90
     - S3
     - elqui
   * - AuxTel Quicklook Images (Butler)
     - 7
     - S3
     - elqui
   * - Large File Annex
     - 30
     - S3
     - elqui
   * - RubinTV Products
     - ?? [1]_
     - S3
     - elqui
   * - ComCam Raw Images (Butler)
     - 90
     - S3
     - elqui
   * - ComCam Quicklook Images (Butler)
     - 7
     - S3
     - elqui
   * - LSSTCam Raw Images (Butler)
     - 30
     - S3
     - elqui
   * - LSSTCam Quicklook Images (Butler)
     - 7
     - S3
     - elqui
   * - Calibration Products
     - None [2]_
     - S3
     - elqui
   * - DREAM Products
     - ?? [3]_
     - S3
     - elqui
   * - EFD
     - 30
     - Ceph PVC
     - yagan

BTS
---

.. list-table:: Retention Policies
   :widths: auto
   :header-rows: 1

   * - Content
     - Retention (days)
     - Provider
     - Server
   * - AuxTel Raw Images (Butler)
     - 20
     - S3
     - konkong
   * - AuxTel Quicklook Images (Butler)
     - 2
     - S3
     - konkong
   * - Large File Annex
     - 30
     - S3
     - konkong
   * - RubinTV Products
     - ?? [1]_
     - S3
     - konkong
   * - LSSTCam Raw Images (Butler)
     - 5
     - S3
     - konkong
   * - LSSTCam Quicklook Images (Butler)
     - 2
     - S3
     - konkong
   * - Calibration Products
     - None [2]_
     - S3
     - konkon
   * - EFD
     - 30
     - Ceph PVC
     - manke

TTS
---

.. list-table:: Retention Policies
   :widths: auto
   :header-rows: 1

   * - Content
     - Retention (days)
     - Provider
     - Server
   * - AuxTel Raw Images (Butler)
     - 20
     - Ceph NFS
     - pillan
   * - AuxTel Quicklook Images (Butler)
     - ?? [1]_
     - Ceph NFS
     - pillan
   * - Large File Annex
     - 30
     - S3
     - pillan
   * - RubinTV Products
     - ?? [1]_
     - S3
     - pillan
   * - ComCam Raw Images (Butler)
     - 30
     - Ceph NFS
     - pillan
   * - ComCam Quicklook Images (Butler)
     - ?? [1]_
     - Ceph NFS
     - pillan
   * - Calibration Products
     - None [2]_
     - Ceph NFS
     - pillan
   * - EFD
     - 30
     - Ceph PVC
     - pillan


.. rubric:: Footnotes

.. [1] These products currently have no known retention policy applied.
.. [2] These have an indeterminate lifetime and will be managed by TAXICAB.
.. [3] It is TBD if all DREAM products are handled by the LFA retention policy.
