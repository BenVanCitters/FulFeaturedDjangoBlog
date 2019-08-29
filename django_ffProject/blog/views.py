from django.shortcuts import render


posts = [
    {
        'author':'BenMS',
          'title': 'Blog Post',
          'content': 'First post content',
          'date_posted': 'August 29, 2019'
     },
    {
        'author': 'Jane dost',
        'title': 'Blog post2',
        'content': 'second post content',
        'date_posted': 'August 35, 2019'
    }

]
def home(request):
    context = {'posts':posts}
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html', {'title': 'about page title'})
