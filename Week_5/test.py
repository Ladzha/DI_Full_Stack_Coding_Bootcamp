# def clean_title(self):
#     title = self.cleaned_data['title']
#     if 'Django' in title:
#         raise forms.ValidationsError('Error in the title')
#     else: 
#         return title

# def clean(self):
#     clean_data=super().clean()
#     title = clean_data['title'] #v skopbkah potomu cho eto slovar
#     content = clean_data['content']
#     author = clean_data['author']
    
#     if author.user.is_staff and 'slovo' in content:
#         raise forms.ValidationsError('Cannot be admin and write about content')
#     else:
#         clean_data
        
#         # promitions comes from model


                # <!-- <a class="nav-link" href="{% url 'account/signup' %}">Sign up</a> -->
#V fomah
# CategoryFormSet = form.modelformset_factory(Category, form = CategoryForm)

# #potom v form
# def manage_categories(request):
#     #POST
#     if request.method = 'POST'
#     #GET
#     formset = CategoryFormSet(queryset = Category.objects.all())
#     context = {'formset': formset}
#     return render (request, 'manage_categories.html')



# in url
urlpatterns = [
    path('managepost/', manage_post, name = 'managepost'),
]

# in forms.py
PostFormSet = forms.modelformset_factory(model=Post, form = PostForm)

# in views.py 
def manage_post(request):
    #POST
    if request.method =='POST':
        formset = PostFormSet(request.POST, quaryset.Post.objects.all())
        if formset.is_valid():
           formset.save()
        else:
            print(formset.errors)     
    #GET
    formset = PostFormSet(queryset = Post.objects.all())
    context = {'form_set': formset}
    return render(request, 'manage_post.html', context)

#in manage_post.html
{%block content%}

<h1>Manage posts </h1>
<form method = 'post'>
{%csrf_token%}
{{formset.management_form}}
{%for form in form_set%} 
{{form.as_p}}
{%endfor%}
<button type='submit'> submit </button>
{/form}

{%endblock content%}


# CategoryRelationFormSet = forms.inlineformset_factory(Post, Category, form = CategoryForm, extra = 0 #not allow to create new category)
