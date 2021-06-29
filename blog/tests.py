from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


class Test_Create_post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testusere1 = User.objects.create_user(
            username='testuser1', password='123456789')
        test_post = Post.objects.create(category_id=1, title='Post title', excerpt='Post Excerpt',
                                        content='Post Content', slug='post-title', author_id=1, status='published')

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Post title')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'Post title')
        self.assertEqual(str(cat), 'django')
