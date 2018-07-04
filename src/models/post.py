__author__ = "abhishekmadhu"

import uuid
from src.common.database import Database
import datetime
__author__ = "abhishekmadhu"


class Post(object):
    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self._id = uuid.uuid4().hex if _id is None else _id
        self.created_date = created_date

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return {
            '_id': self._id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @staticmethod
    def from_mongo(cls, _id):
        # Post.from_mongo('123')
        post_data = Database.find_one(collection='posts',
                                      data={'_id': _id})
        return cls(**post_data)

    # this is equivalent to the following --
    # return cls(blog_id=post_data['blog_id'],
    #                    title=post_data['title'],
    #                    content=post_data['content'],
    #                    author=post_data['author'],
    #                    created_date=post_data['created_date'],
    #                    _id=post_data['_id'])

    @staticmethod
    def from_blog(_id):  # blog _id for all posts by one person is same
        return [post for post in Database.find(collection='posts',
                                               data={'blog_id': _id})]