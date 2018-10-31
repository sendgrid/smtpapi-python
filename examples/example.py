# Python 2/3 compatible codebase
from __future__ import absolute_import, division, print_function
from smtpapi import SMTPAPIHeader

import time

if __name__ == '__main__' and __package__ is None:
    from os import sys, path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from smtpapi import SMTPAPIHeader

header = SMTPAPIHeader()

# [To](http://sendgrid.com/docs/API_Reference/SMTP_API/index.html)
# header.add_to('test@example.com')
header.set_tos(['test1@example.com', 'test2@example.com'])

# [Substitutions](http://sendgrid.com/docs/API_Reference/SMTP_API/substitution_tags.html)
# header.add_substitution('key', 'value')
header.set_substitutions({'key': ['value1', 'value2']})

# [Unique Arguments](http://sendgrid.com/docs/API_Reference/SMTP_API/unique_arguments.html)
# header.add_unique_arg('key', 'value')
header.set_unique_args({'key': 'value'})

# [Categories](http://sendgrid.com/docs/API_Reference/SMTP_API/categories.html)
# header.add_category('category')
header.set_categories(['category1', 'category2'])

# [Sections](http://sendgrid.com/docs/API_Reference/SMTP_API/section_tags.html)
# header.add_section('key', 'section')
header.set_sections({'key1': 'section1', 'key2': 'section2'})

# [Filters](http://sendgrid.com/docs/API_Reference/SMTP_API/apps.html)
header.add_filter('filter', 'setting', 'value')

# [ASM Group ID](https://sendgrid.com/docs/User_Guide/advanced_suppression_manager.html)
header.set_asm_group_id('value')

# [IP Pools](https://sendgrid.com/docs/API_Reference/Web_API_v3/IP_Management/ip_pools.html)
header.set_ip_pool("testPool")

# [Scheduling Parameters](https://sendgrid.com/docs/API_Reference/SMTP_API/scheduling_parameters.html)
# header.add_send_each_at(unix_timestamp) #  must be a unix timestamp
# header.set_send_each_at([]) #  must be a unix timestamp
header.set_send_at(int(time.time()))  # must be a unix timestamp

print(header.json_string())
