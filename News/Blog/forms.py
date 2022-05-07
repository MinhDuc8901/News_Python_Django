from dataclasses import Field
from xml.etree.ElementTree import Comment
from django.forms import ModelForm
from Blog.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'