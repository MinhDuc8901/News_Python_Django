from dataclasses import field
from django.forms import ModelForm
from Blog.models import Room
from Blog.models import Topic


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'

