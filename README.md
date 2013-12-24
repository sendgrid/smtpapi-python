# SMTPAPI for Python

This module will let you build SendGrid's SMTP API headers with simplicity.

## Installing

```bash
pip install smtpapi
```

## Examples

### Create headers

```python
from smtpapi import SMTPAPIHeader

header = SMTPAPIHeader()

```

### [Substitutions](http://sendgrid.com/docs/API_Reference/SMTP_API/substitution_tags.html)

```python
header.add_substitution('key', 'value')
header.set_substitution('key', ['value1', 'value2'])
```

### [Unique Arguments](http://sendgrid.com/docs/API_Reference/SMTP_API/unique_arguments.html)

```python
header.add_unique_args('key', 'value')
header.set_unique_args({'key':'value'})
```
### [Categories](http://sendgrid.com/docs/API_Reference/SMTP_API/categories.html)

```python
header.add_category('category')
header.set_category(['category1', 'category2'])
```

### [Sections](http://sendgrid.com/docs/API_Reference/SMTP_API/section_tags.html)

```python
header.add_section('key', 'section')
header.set_section({'key1':'section1', 'key2':'section2'})
```

### [Filters](http://sendgrid.com/docs/API_Reference/SMTP_API/apps.html)

```python
header.add_filter('filter', 'setting', 'value')
```

### Get Headers

```python
header.api_header_as_json()
```

## MIT
