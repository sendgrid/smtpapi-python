.. image:: https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png
   :target: https://www.sendgrid.com
   :alt: SendGrid Logo

|Test and Deploy Badge| |Twitter Follow| |Codecov branch| |Python Versions| |PyPI Version| |GitHub contributors| |MIT Licensed|

**This module helps build SendGrid's SMTP API headers.**

Learn more about the SMTP API at `SendGrid documentation`_.

Announcements
=============
**The default branch name for this repository has been changed to `main` as of 07/27/2020.**

All the updates to this module are documented in our `CHANGELOG`_.

Table of Contents
=================

-  `Installation <#installation>`__
-  `Quick Start <#quick-start>`__
-  `Usage <#usage>`__
-  `How to Contribute <#how-to-contribute>`__
-  `Local Setup of the Project <#local-setup-of-the-project>`__
-  `About <#about>`__
-  `License <#license>`__

Installation
============

Prerequisites
-------------

-  Python version 2.7 or 3.4+
-  The SendGrid service, starting at the `free level`_

Install Package
---------------

.. code:: bash

    pip install smtpapi

Setup Environment Variables
---------------------------

Update the development environment with your `SENDGRID_API_KEY`_, for example:

.. code:: bash

    cp .env_sample .env

In ``.env`` set ``SENDGRID_API_KEY`` to your own API key.

You can add your environment variables to your environment by sourcing the file:

.. code:: bash

    source .env

Quick Start
===========

.. code:: python

    from smtpapi import SMTPAPIHeader

    header = SMTPAPIHeader()
    header.add_to('email@email.com')
    print(header.json_string())

Usage
=====

- `SendGrid documentation`_
- `Example Code`_

How to Contribute
=================

We encourage contribution to our projects, please see our `CONTRIBUTING`_ guide for more details.

Quick links:

-  `Feature Request`_
-  `Bug Reports`_
-  `Improvements to the Codebase`_
-  `Review Pull Requests`_

Local Setup of the Project
==========================

The simplest local development workflow is by using Docker.

Steps:

1. Install [Docker](https://www.docker.com/)
2. Run ``docker-compose build`` (this builds the container)
3. Run ``docker-compose up`` (this runs tests by default)

About
=====

**smtpapi-python** is maintained and funded by Twilio SendGrid, Inc.
The names and logos for **smtpapi-python** are trademarks of Twilio SendGrid, Inc.

License
=======

`The MIT License (MIT)`_

.. _SendGrid documentation: https://sendgrid.com/docs/API_Reference/SMTP_API/index.html
.. _CHANGELOG: https://github.com/sendgrid/smtpapi-python/blob/HEAD/CHANGELOG.md
.. _free level: https://sendgrid.com/free?source=sendgrid-python
.. _SENDGRID_API_KEY: https://app.sendgrid.com/settings/api_keys
.. _Example Code: https://github.com/sendgrid/smtpapi-python/tree/HEAD/examples
.. _CONTRIBUTING: https://github.com/sendgrid/smtpapi-python/blob/HEAD/CONTRIBUTING.md
.. _Feature Request: https://github.com/sendgrid/smtpapi-python/blob/HEAD/CONTRIBUTING.md#feature-request
.. _Bug Reports: https://github.com/sendgrid/smtpapi-python/blob/HEAD/CONTRIBUTING.md#submit-a-bug-report
.. _Improvements to the Codebase: https://github.com/sendgrid/smtpapi-python/blob/HEAD/CONTRIBUTING.md#improvements-to-the-codebase
.. _Review Pull Requests: https://github.com/sendgrid/smtpapi-python/blob/HEAD/CONTRIBUTING.md#code-reviews)
.. _The MIT License (MIT): https://github.com/sendgrid/smtpapi-python/blob/HEAD/LICENSE

.. |Test and Deploy Badge| image:: https://github.com/sendgrid/smtpapi-python/actions/workflows/test-and-deploy.yml/badge.svg
   :target: https://github.com/sendgrid/smtpapi-python/actions/workflows/test-and-deploy.yml
.. |Twitter Follow| image:: https://img.shields.io/twitter/follow/sendgrid.svg?style=social&label=Follow
   :target: https://twitter.com/sendgrid
.. |Codecov branch| image:: https://img.shields.io/codecov/c/github/sendgrid/smtpapi-python/main.svg?style=flat-square&label=Codecov+Coverage
   :target: https://codecov.io/gh/sendgrid/smtpapi-python
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/smtpapi.svg
   :target: https://pypi.org/project/smtpapi/
.. |PyPI Version| image:: https://img.shields.io/pypi/v/smtpapi.svg
   :target: https://pypi.org/project/smtpapi/
.. |GitHub contributors| image:: https://img.shields.io/github/contributors/sendgrid/smtpapi-python.svg
   :target: https://github.com/sendgrid/smtpapi-python/graphs/contributors
.. |MIT Licensed| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/sendgrid/smtpapi-python/blob/HEAD/LICENSE
