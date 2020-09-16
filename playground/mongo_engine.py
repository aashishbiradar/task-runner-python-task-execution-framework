from mongoengine import *
import datetime
connect('tastrunner')

class BlogPost(Document):
    title = StringField(required=True, max_length=200)
    posted = DateTimeField(default=datetime.datetime.utcnow)
    tags = ListField(StringField(max_length=50))
    meta = {'allow_inheritance': True}

class TextPost(BlogPost):
    content = StringField(required=True)

class LinkPost(BlogPost):
    url = StringField(required=True)

if __name__ == "__main__":
    # Create a text-based post
    post1 = TextPost(title='Using MongoEngine', content='See the tutorial')
    post1.tags = ['mongodb', 'mongoengine']
    post1.save()

    # Create a link-based post
    post2 = LinkPost(title='MongoEngine Docs', url='hmarr.com/mongoengine')
    post2.tags = ['mongoengine', 'documentation']
    post2.save()