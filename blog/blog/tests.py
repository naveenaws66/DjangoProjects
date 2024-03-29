from django.contrib.auth import get_user_model

from django.test import TestCase

from django.urls import reverse

from .models import Post

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'testuser@email.com',
            password = 'password'
        )
        self.post = Post.objects.create(
            title = 'testpost',
            body =  'test body content',
            author = self.user
        )

    def test_string_representation(self):
        post = Post(title = 'a sample title')
        self.assertEqual(str(post), post.title)
    
    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'testpost')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'test body content')
    
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test body content')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 301)
        self.assertContains(response, 'testpost')
        self.assertTemplateUsed(response, 'post_detail.html')
    
    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title' : 'createviewtest',
            'body'  : 'bodycreateviewtest',
            'author' : self.user
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'createviewtest')
        self.assertContains(response, 'bodycreateviewtest')
    
    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title' : 'updated title',
            'body'  : 'updated text',
        })
        self.assertEqual(response.status_code, 302)
    
    def test_post_delete_view(self):
        response = self.client.get(reverse('post_delete', args ='1'))
        self.assertEqual(response.status_code, 200)
