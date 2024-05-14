from django.test import TestCase
from django.urls import reverse
from .models import Post

class ViewsTest(TestCase):

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_list.html')

    def test_add_post_view(self):
        response = self.client.post(reverse('add_post'), {'title': 'New Post', 'content': 'New Content'})
        self.assertEqual(response.status_code, 302)  # Should redirect after adding a post
        self.assertTrue(Post.objects.filter(title='New Post').exists())

    def test_update_post_view(self):
        new_title = 'Updated Title'
        response = self.client.post(reverse('update_blog', kwargs={'pk': self.post.pk}),
                                    {'title': new_title, 'content': 'Updated Content'})
        self.assertEqual(response.status_code, 302)  # Should redirect after updating a post
        updated_post = Post.objects.get(pk=self.post.pk)
        self.assertEqual(updated_post.title, new_title)

    def test_delete_post_view(self):
        response = self.client.post(reverse('delete_post', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 302)  # Should redirect after deleting a post
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())


