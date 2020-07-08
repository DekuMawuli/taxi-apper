from django.shortcuts import render

from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView

)
from .models import Post
# from image_upload.forms import ImageForm
from django.shortcuts import redirect
# from image_upload.models import Image




# views for video================================

#
# def showvideo(request):
#     lastvideo = Video.objects.last()
#
#
#
#     form = VideoForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#
#     context = {
#                'form': form
#                }
#     # 'videofile':videofile
#     return render(request, 'Blog/videos.html', context)

# homepage=================================
def home(request):
    context ={
        'posts': Post.objects.all()



    }
    return render(request, 'blog/blog.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = '-date_posted'
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 5
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/blog-details.html"


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



# for picture upload=====================================================

# def image_view(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return redirect('blog_images')
#     else:
#         form = ImageForm()
#     return render(request, 'image_upload.html', {'form': form})



# Python program to view
# for displaying images
#
# def display_images(request):
#     if request.method == 'GET':
#         # getting all the objects of hotel.
#         Images = Image.objects.all()
#         context={
#             'blog_images': Images
#         }
#         return render(request, 'image_display.html', context)
#
#

