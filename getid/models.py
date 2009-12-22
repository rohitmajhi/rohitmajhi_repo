from google.appengine.ext import db

class InterestedPerson(db.Model):
    """Basic user profile with personal details."""
    email=db.EmailProperty(required=True)
    pub_date = db.DateTimeProperty(auto_now=True)
    
    def __unicode__(self):
        return '%s %s' % (self.email, self.pub_date)
