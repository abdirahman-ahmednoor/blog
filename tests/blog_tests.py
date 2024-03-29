import unittest
from app.models import Blog,User
from app import db


class BlogTest(unittest.TestCase):
    def setUp(self):
        self.userAhmed= User(username='Ahmed', password='123', email='ahmedabdi@gmail.com')
        self.new_blog = Blog(id=1, title='Hustler', content='Testing', user_id=self.userPreston.id)

    def tearDown(self):
        Blog.query.deleteBlog()
        User.query.deleteBlog()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'Hustle')
        self.assertEquals(self.new_blog.content, 'Testing')
        self.assertEquals(self.new_blog.user_id, self.userAhmed.id)

    def test_save_blog(self):
        self.new_blog.saveBlog()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog(self):
        self.new_blog.save()
        got_blog = Blog.getallBlogs(1)
        self.assertTrue(got_blog is not None)