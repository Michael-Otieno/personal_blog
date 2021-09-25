import unittest
from app.models import User, Post


class PostModelTest(unittest.TestCase):
    def setUp(self):
        self.new_post = Post(id=1, title='Test', content='This is a test blog', user_id=self.new_user)
    
    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.title, 'Test')
        self.assertEquals(self.new_post.content, 'This is a test blog')
        self.assertEquals(self.new_post.user_id, self.new_user)

    def test_save_post(self):
        self.new_post.save()
        self.assertTrue(len(Post.query.all()) > 0)

    def test_get_post(self):
        self.new_post.save()
        get_post = Post.get_post(1)
        self.assertTrue(get_post is not None)
