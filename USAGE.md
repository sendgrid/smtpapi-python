This documentation is based on our [API_Reference](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html)

# INITIALIZATION

## Simple Way

```python
from smtpapi import SMTPAPIHeader

header = SMTPAPIHeader()
header.set_tos(['test1@example.com', 'test2@example.com'])
print(header.json_string())
```

or

## With Several SMTP-API Methods

```python

from smtpapi import SMTPAPIHeader

header = SMTPAPIHeader()
header.set_tos(['test1@example.com', 'test2@example.com'])
header.set_categories(['category1', 'category2'])
header.set_send_at(int(time.time())
header.set_sections({'key1':'section1', 'key2':'section2'})
header.set_substitutions({'key': ['value1', 'value2']})
header.set_asm_group_id('value')
header.set_unique_args({'key':'value'})
print(header.json_string())
```

# Table of Contents

* [Using the SMTP API](#use-smtp-api)
* [Settings](#settings)
* [Categories](#categories)
* [Scheduling Parameters](#scheduling-parameters)
* [Section Tags](#section-tags)
* [Substitution Tags](#substitution-tags)
* [Suppression Groups](#suppression-groups)
* [Unique Arguments](#unique-arguments)

<a name="use-smtp-api"></a> 
# Using the SMTP API

**This endpoint allows you to add as many of the SMTP API methods as you want to a single large JSON string, and pass that JSON string to SendGrid with your messages.**

You can add as many of the SMTP API methods as you want to a single large JSON string, and pass that JSON string to SendGrid with your messages. To do this, add the JSON string to your message under a header named “X-SMTPAPI” like this:

```python
{
  "to": [
    "ben@sendgrid.com",
    "joe@sendgrid.com"
  ],
  "sub": {
    "%name%": [
      "Ben",
      "Joe"
    ],
    "%role%": [
      "%sellerSection%",
      "%buyerSection%"
    ]
  },
  "section": {
    "%sellerSection%": "Seller information for: %name%",
    "%buyerSection%": "Buyer information for: %name%"
  },
  "category": [
    "Orders"
  ],
  "unique_args": {
    "orderNumber": "12345",
    "eventID": "6789"
  },
  "filters": {
    "footer": {
      "settings": {
        "enable": 1,
        "text/plain": "Thank you for your business"
      }
    }
  },
  "send_at": 1409348513
}
```
The above example is formatted for readability. Headers must be wrapped to keep the line length under 72. By RFC 821 no line can be longer than 1,000, so if you are going to generate this string yourself it is a good idea to make sure that you wrap it.

## Requirements and Limitations
While there is a hard limit of 10,000 addresses that can be sent to in a multiple recipient e-mail, it is best to split up large jobs to around 1,000 recipients, to better allow for the processing load to be distributed. Furthermore, if you have a large number of additional substitutions or sections in the headers, it is best to split the send into even smaller groups.

<a name="settings"></a>
# Settings (Filters)

Following are the settings that can be specified in the filters section of the X-SMTPAPI header. All filters and setting names must be lowercase.

* If you’re enabling a Setting, also called a filter, via SMTPAPI, you are required to define all of the parameters for that Setting.
* Setting enabled status will always default to your settings on the website, unless otherwise defined in your X-SMTPAPI header
* If you enable a disabled setting, our system will not pull your settings for the disabled setting. You will need to define the settings in your X-SMTPAPI header Example: If you have a footer designed but disabled, you can’t just enable it via the API; you need to define the footer in the API call itself.
* All filter names and setting names must be lowercase.

## Filter: `bcc`
Sends a BCC copy of the email created in this transaction to the address specified.
```python
{
  "filters" : {
    "bcc" : {
      "settings" : {
        "enable" : 1,
        "email" : "you@example.com"
      }
    }
  }
}
```

Sends a BCC copy of the email created in this transaction to the address specified.

<a name="categories"></a>
# Categories
**This endpoint allows you to add categories to the X-SMTPAPI header of the emails you send via SendGrid**

By adding categories to the X-SMTPAPI header of the emails that you send via SendGrid you can to track emails based on your categorization system.

Categories must be in 7bit encoding using the US-ASCII character set, and should be used to group messages together by broad topic. If you need to attach unique data or identifiers to a message, use [Unique Arguments](https://sendgrid.com/docs/API_Reference/SMTP_API/unique_arguments.html) instead.

## Example
You can use SendGrid’s SMTP API to add these categories to your email. The following should be added to the email’s header:

### Example Category Header
```python
{
  "category": "Example Category"
}
```
In this example, SendGrid would associate statistics for the email containing that header with the category Example Category.

### Limitations
You can assign up to 10 categories per message:
```python
{
  "category": [
    "dogs",
    "animals",
    "pets",
    "mammals"
  ]
}
```

<a name="scheduling-parameters"></a>
# Scheduling Parameters
**This endpoint allows you to send large volumes of email in queued batches or target individual recipients by specifying a custom UNIX timestamp parameter.**

This parameter allows SendGrid to begin processing a customer’s email requests before sending. SendGrid will then queue those messages and release them when the timestamp is exceeded. This technique allows for a more efficient way to distribute large email requests and can improve overall mail delivery time performance. 

The scheduling parameters functionality:

* Improves efficiency of processing and distributing large volumes of email.
* Reduces email pre-processing time.
* Enables user to set email arrival time to increase open rates.

Using the parameters defined below, you can queue batches of emails targeting individual recipients.

**Note: Using both send_at and send_each_at is not valid and will cause your request to be dropped.**

### Send At
To schedule a send request for a large batch of emails, use the send_at parameter which will send all emails at approximately the same time. send_at is a UNIX timestamp.

Example of **`send_at`** email header

```python
{
  "send_at": 1409348513
}
```

### Send Each At
To schedule a send request for individual recipients; use send_each_at to send emails to each recipient at the specified time. send_each_at is a sequence of UNIX timestamps, provided as an array. There must be one timestamp per email you wish to send.

Example of **`send_each_at`** email header

```python
{
  "to": [
    "<ben@example.com>",
    "john@example.com",
    "mike@example.com"
  ],
  "send_each_at": [
    1409348513,
    1409348514,
    1409348515
  ]
}
```

<a name="section-tags"></a>
# Section Tags
Section tags are similar to substitution tags in how they’re built, but are specific to the message, not the recipient. You have to have a substitution tag value for each recipient, but you can have any number of section tags. Section tags can then contain Substitution tags for the recipient if needed. Section tags have to be contained within a Substitution tag, since SendGrid needs to know which data to populate for the recipient.

The format of the SMTP API section tag has the form:
```python
{
  "section": {
    ":sectionName1": "section 1 text",
    ":sectionName2": "section 2 text"
  }
}
```

<a name="substitution-tags"></a>
# Substitution Tags

**This endpoint allows you to easily generate dynamic content for each recipient on your list.**

 When you send to a list of recipients over SMTP API you can specify substitution tags specific to each recipient. For example, a first name that will then be inserted into an opening greeting like the following, where each recipient sees -firstName- replaced with their first name.

`"Dear -firstName-"`

These tags can also be used in more complex scenarios. For example, you could use a -customerID- to build a custom URL that is specific to that user.

A customer specific ID can replace -customerID- in the URL within your email
`<a href="http://example.com/customerOffer?id=-customerID-">Claim your offer!</a>`

## Substitution Tag Example

Email HTML content:
```
<html>
  <head></head>
  <body>
    <p>Hello -name-,<br>
       Thank you for your interest in our products. I have set up an appointment
             to call you at -time- EST to discuss your needs in more detail. If you would
             like to reschedule this call please visit the following link:
             <a href="http://example.com/reschedule?id=-customerID-">reschedule</a>

                Regards,

                -salesContact-
                -contactPhoneNumber-<br>
    </p>
  </body>
</html>
```

An accompanying SMTP API JSON header might look something like this:
```
{
  "to": [
    "john.doe@gmail.com",
    "jane.doe@hotmail.com"
  ],
  "sub": {
    "-name-": [
      "John",
      "Jane"
    ],
    "-customerID-": [
      "1234",
      "5678"
    ],
    "-salesContact-": [
      "Jared",
      "Ben"
    ],
    "-contactPhoneNumber-": [
      "555.555.5555",
      "777.777.7777"
    ],
    "-time-": [
      "3:00pm",
      "5:15pm"
    ]
  }
}
```

The resulting email for John would look like this:
```
<html>
  <head></head>
  <body>
    <p>Hello John,<br>
       Thank you for your interest in our products. I have set up an appointment
             to call you at 3:00pm EST to discuss your needs in more detail. If you would
             like to reschedule this call please visit the following link:
             <a href="http://example.com/reschedule?id=1234">reschedule</a>

                Regards,

                Jared
                555.555.5555<br>
    </p>
  </body>
</html>
```

<a name="suppression-groups"></a>
# Suppression Groups

## Defining an Unsubscribe Group When Sending

**This endpoint allows you to specify an unsubscribe group for an email depends on how you will be sending that email.**

Precaution:

* When sending an SMTP message, add the group’s ID to the X-SMTPAPI header.
* When sending an email via the Web API v2, add the group’s ID in the `x-smtpapi` parameter.
* When sending an email via the Web API v3, define the group’s ID in the `asm.group_id` parameter.

You may only specify one group per send, and you should wait one minute after creating the group before sending with it.

```python
{
  "asm_group_id": 1
}
```

Defining Unsubscribe Groups to display on the Manage Preferences page
To specify which groups to display on the Manage Preferences page of an email, add the group IDs to the X-SMTPAPI header of an SMTP message, or in the x-smtpapi parameter of a mail.send API call. If the asm_groups_to_display header is omitted, your default groups will be shown on the Manage Preferences page instead.

You can specify up to 25 groups to display.
```python
{
  "asm_groups_to_display": [1, 2, 3]
}
```

## Groups
You can find your group IDs by looking at the Group ID column in the Unsubscribe Groups UI, or by calling the [GET method](https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/groups.html#-GET) of the groups resource.

<a name="unique-arguments"></a>
# Unique Arguments

The SMTP API JSON string allows you to attach an unlimited number of unique arguments to your email up to 10,000 bytes. The arguments are used only for tracking. They can be retrieved through the Event API or the Email Activity page.

These arguments can be added using a JSON string like this:
```
{
  "unique_args": {
    "customerAccountNumber": "55555",
    "activationAttempt": "1",
    "New Argument 1": "New Value 1",
    "New Argument 2": "New Value 2",
    "New Argument 3": "New Value 3",
    "New Argument 4": "New Value 4"
  }
}
```

These arguments can then be seen in posts from the SendGrid Event Webhook. The contents of one of these POST requests would look something like this:

## Example Webhook Post Data

```
{
  "sg_message_id": "145cea24eb8.1c420.57425.filter-132.3382.5368192A3.0",
  "New Argument 1": "New Value 1",
  "event": "processed",
  "New Argument 4": "New Value 4",
  "email": "user@example.com",
  "smtp-id": "<145cea24eb8.1c420.57425@localhost.localdomain>",
  "timestamp": 1399331116,
  "New Argument 2": "New Value 2",
  "New Argument 3": "New Value 3",
  "customerAccountNumber": "55555",
  "activationAttempt": "1"
}
```
Unique Arguments will also be shown in the Email Activity tab of your account.

To apply different unique arguments to individual emails, you may use substitution tags. An example of this would look like:
```
{
  "sub": {
    "-account_number-": [
      "314159",
      "271828"
    ]
  },
  "unique_args": {
    "customerAccountNumber": "-account_number-"
  }
}
``` 
