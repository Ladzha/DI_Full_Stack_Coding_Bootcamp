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
