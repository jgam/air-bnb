from django import forms
from django_countries.widgets import CountryField
from . import models

# this is form field


class SearchForm(forms.Form):
    city = forms.CharField(initial="Anywhere")
    country = CountryField().formfield(default="KR")
    price = forms.IntegerField(required=False)
    room_type = forms.ModelChoiceField(
        required=False, empty_label="Any kind", queryset=models.RoomType.objects.all())
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(requred=False)
    superhost = forms.BooleanField(requred=False)
    amenities = forms.ModelMultipleChoiceField(
        queryset=models.Amenity.objects.all(), widget=forms.CheckboxSelectMultiple)
    facilities = forms.ModelMultipleChoiceField(
        queryset=models.Facility.objects.all(), widget=forms.CheckboxSelectMultiple)
