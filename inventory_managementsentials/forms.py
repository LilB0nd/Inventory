from django import forms
from .models import Room, Beamer, Computer, Screen, SmartBoard, Canvas, SpeakerSet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'description',
            'location',
            'blackboard',
            'chair',
            'table'
        ]


class BeamerForm(forms.ModelForm):
    class Meta:
        model = Beamer
        fields = [
            'room',
            'description',
            'status',
            'HDMI',
            'VGA',
            'DVI',
            'DB',
            'USBTypeC',
            'serialnumber',
            'warranty_period',
            'date_of_purchase',
            'price',
            'brand',

        ]


class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = [
            'room',
            'description',
            'status',
            'serialnumber',
            'warranty_period',
            'date_of_purchase',
            'price',
            'brand',
        ]


class ScreenForm(forms.ModelForm):
    class Meta:
        model = Screen
        fields = [
            'room',
            'description',
            'status',
            'screen_format',
            'serialnumber',
            'warranty_period',
            'date_of_purchase',
            'price',
            'brand',
        ]


class SmartBoardForm(forms.ModelForm):
    class Meta:
        model = SmartBoard
        fields = [
            'room',
            'description',
            'status',
            'serialnumber',
            'warranty_period',
            'date_of_purchase',
            'price',
            'brand',
        ]


class CanvasForm(forms.ModelForm):
    class Meta:
        model = Canvas
        fields = [
            'room',
            'description',
            'status',
            'canvas_format',
            'serialnumber',
            'warranty_period',
            'date_of_purchase',
            'price',
            'brand',

        ]


class SpeakerSetForm(forms.ModelForm):
    class Meta:
        model = SpeakerSet
        fields = [
            'room',
            'quantity',
            'description',
            'status',
            'serialnumber',
            'warranty_period',
            'date_of_purchase',
            'price',
            'brand',
        ]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']



"""
class RawRoomForm(forms.Form):
    description = forms.CharField(required=True)
    location = forms.ChoiceField(choices=Location.BUILDING_IN_BUILDING_CHOICES, required=False)
    blackboard = forms.BooleanField(required=False)
    chair = forms.DecimalField(required=False)
    table = forms.DecimalField(required=False)
"""