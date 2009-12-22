# -*- coding: utf-8 -*-


# profile contains

# Account
# Hi Rohit
#
# Delivery Address
# password


# General Settings
# First Name
# Last Name
# Email address
# password
# phone number


# Delivery Settings
# Delivery Address

#

# Notification Settings
# phone
# SMS
# Email


# Food Details
# Allergic to XYZ


# I am Green
# Is worried about the environment

# Payment Details
# Credit Card Details


from django.db.models import permalink, signals
from google.appengine.ext import db
from ragendja.dbutils import cleanup_relations

class User_Account(db.Model):
    """Basic user profile with personal details."""
    first_name = db.StringProperty(required=True)
    last_name = db.StringProperty(required=True)
    email = db.EmailProperty(required=True)
    phone = db.PhoneNumberProperty(required=True)
    
    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

#     @permalink
#     def get_absolute_url(self):
#         return ('myapp.views.show_person', (), {'key': self.key()})

signals.pre_delete.connect(cleanup_relations, sender=Person)



