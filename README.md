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

### [To](http://sendgrid.com/docs/API_Reference/SMTP_API/index.html)
```python
header.add_to('email@email.com')
header.set_tos(['email@email.com'])
```

### [Substitutions](http://sendgrid.com/docs/API_Reference/SMTP_API/substitution_tags.html)

```python
header.add_substitution('key', 'value')
header.set_substitutions({'key': ['value1', 'value2']})
```

### [Unique Arguments](http://sendgrid.com/docs/API_Reference/SMTP_API/unique_arguments.html)

```python
header.add_unique_arg('key', 'value')
header.set_unique_args({'key':'value'})
```
### [Categories](http://sendgrid.com/docs/API_Reference/SMTP_API/categories.html)

```python
header.add_category('category')
header.set_categories(['category1', 'category2'])
```

### [Sections](http://sendgrid.com/docs/API_Reference/SMTP_API/section_tags.html)

```python
header.add_section('key', 'section')
header.set_sections({'key1':'section1', 'key2':'section2'})
```

### [Filters](http://sendgrid.com/docs/API_Reference/SMTP_API/apps.html)

```python
header.add_filter('filter', 'setting', 'value')
```

### Get Headers

```python
header.json_string()
```

## MIT
