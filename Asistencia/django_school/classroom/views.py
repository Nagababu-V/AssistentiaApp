
from classroom.forms import PostForm

def Tpost_form_upload(request):
    if request.method == 'GET':
        form1 = PostForm()
    else:
        # A POST request: Handle Form Upload
        form1 = PostForm(request.POST) # Bind data from request.POST into a PostForm

        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            classID = form.cleaned_data['classID']

            post1 = m.Post.objects.create(content=content,created_at=created_at)
            return HttpResponseRedirect(reverse('post_detail',
                                                kwargs={'post_id': post.id}))

    return render(request, 'classroom/TGetClassDetails.html', {
        'form1': form,
    })


def Gpost_form_upload(request):
    if request.method == 'GET':
        form2 = PostForm()
    else:
        # A POST request: Handle Form Upload
        form2 = PostForm(request.POST) # Bind data from request.POST into a PostForm

        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            classID = form.cleaned_data['classID']

            post2 = m.Post.objects.create(content=content,created_at=created_at)
            return HttpResponseRedirect(reverse('post_detail',
                                                kwargs={'post_id': post.id}))

    return render(request, 'classroom/GGetClassDetails.html', {
        'form2': form,
    })
