from django import modelform_factory
from django import modelForm
from DjangoStack.models import Category, Request, Available

#Create the form class
class CatergoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['Category Name']

#Creating a form to add an article
form = CategoryForm

#Creating a form to change an existing category
Category = Category.objects.get(pk=1)               #Anthony will need to update 1 for dynamic reference
form = CategoryForm(instance=article)

#Model form factory function - for front end facing forms
CategoryForm = modelform_factory(Category, fields=("category_name", "username"))
RequestForm = modelform_factory(Request, fields=("time_in_hours", "category_name", "number_of_people","user_name"))
Available = modelform_factory(Available, fields=("username", "is_available"))
