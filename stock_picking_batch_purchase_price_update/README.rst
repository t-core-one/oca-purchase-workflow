=========================================
Stock Picking Batch Purchase Price Update
=========================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:d7604986d42602023ca0320e4a9421ab94ec9deb2429dac7b9d73765004621c1
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fpurchase--workflow-lightgray.png?logo=github
    :target: https://github.com/OCA/purchase-workflow/tree/15.0/stock_picking_batch_purchase_price_update
    :alt: OCA/purchase-workflow
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/purchase-workflow-15-0/purchase-workflow-15-0-stock_picking_batch_purchase_price_update
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/purchase-workflow&target_branch=15.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

Allow update purchase price from incoming picking operations, picking
detailed operations and picking batch detailed operations if the
purchase order is not invoiced.

NOTICE:
^^^^^^^

The price on the picking reflects the purchase price for all pickings
and is not individual for each picking.

**Table of contents**

.. contents::
   :local:

Configuration
=============

-  Go to 'Inventory > Configuration > Operations' Types
-  Select Reception operation
-  Enable 'Show Detailed Operations' option.
-  Go to picking batch with picking type Reception
-  Add optional column 'Purchase price' in operations and/or detailed
   operations

Usage
=====

1. Go to Inventory > Operations > Batch Transfers
2. Select or create a batch transfer with picking type Receptions
3. Add optional column 'Purchase Price' in operations and or detailed
   operations

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/purchase-workflow/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/purchase-workflow/issues/new?body=module:%20stock_picking_batch_purchase_price_update%0Aversion:%2015.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* Tecnativa

Contributors
------------

-  `Tecnativa <https://www.tecnativa.com>`__:

   -  Carlos Dauden

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-carlosdauden| image:: https://github.com/carlosdauden.png?size=40px
    :target: https://github.com/carlosdauden
    :alt: carlosdauden

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-carlosdauden| 

This module is part of the `OCA/purchase-workflow <https://github.com/OCA/purchase-workflow/tree/15.0/stock_picking_batch_purchase_price_update>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
