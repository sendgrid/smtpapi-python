[![Travis Badge](https://travis-ci.org/sendgrid/smtpapi-python.svg?branch=master)](https://travis-ci.org/sendgrid/smtpapi-python)

**This module helps build SendGrid's SMTP API headers.**

Learn more about the SMTP API at [SendGrid's documentation](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

# Announcements

All updates to this module is documented in our [CHANGELOG](https://github.com/sendgrid/smtpapi-python/blob/master/CHANGELOG.md).

# Installation

## Prerequisites

- Python version 2.6, 2.7, 3.4 or 3.5
- The SendGrid service, starting at the [free level](https://sendgrid.com/free?source=sendgrid-python)

## Install Package

```bash
pip install smtpapi
```

# Quick Start

```python
from smtpapi import SMTPAPIHeader
header = SMTPAPIHeader()
header.add_to('email@email.com')
print header.json_string()
```

# Usage

- [SendGrid Docs](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html)
- [Example Code](https://github.com/sendgrid/smtpapi-python/tree/master/examples)

## Roadmap

If you are interested in the future direction of this project, please take a look at our [milestones](https://github.com/sendgrid/smtpapi-python/milestones). We would love to hear your feedback.

## How to Contribute

We encourage contribution to our projects, please see our [CONTRIBUTING](https://github.com/sendgrid/smtpapi-python/blob/master/CONTRIBUTING.md) guide for details.

Quick links:

- [Feature Request](https://github.com/sendgrid/smtpapi-python/blob/master/CONTRIBUTING.md#feature_request)
- [Bug Reports](https://github.com/sendgrid/smtpapi-python/blob/master/CONTRIBUTING.md#submit_a_bug_report)
- [Sign the CLA to Create a Pull Request](https://github.com/sendgrid/smtpapi-python/blob/master/CONTRIBUTING.md#cla)
- [Improvements to the Codebase](https://github.com/sendgrid/smtpapi-python/blob/master/CONTRIBUTING.md#improvements_to_the_codebase)

# About

smtpapi-python is guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

smtpapi-python is maintained and funded by SendGrid, Inc. The names and logos for smtpapi-python are trademarks of SendGrid, Inc.

![SendGrid Logo](https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)
