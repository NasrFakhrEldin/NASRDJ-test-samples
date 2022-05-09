
from .models import Pic
from django import forms
from .humanize import naturalsize
from django.core.files.uploadedfile import InMemoryUploadedFile


class CreateForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)

    # Call this 'picture' so it gets copied from the form to the in-memory model
    # It will not be the "bytes", it will be the "InMemoryUploadedFile"
    # because we need to pull out things like content_type
    picture = forms.FileField(required=False, label='File to upload <= '+max_upload_limit_text)
    upload_field_name = 'picture'

    class Meta:
        model = Pic
        fields = ['title', 'text', 'picture']

    # Validate the size of the picture
    def clean(self):
        cleaned_data = super().clean()
        pic = cleaned_data.get('picture')
        if pic is None: return
        if len(pic) > self.max_upload_limit:
            self.add_error('picture', "File must be < "+self.max_upload_limit_text+" bytes")

    # Convert uploaded File object to a picture
    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)

        # We only need to adjust the picture if it is a freshly uploaded file
        f = instance.picture  # make a copy from model - Binary Field

        if isinstance(f, InMemoryUploadedFile): # Extract data from the form to the model
            bytearr = f.read()
            instance.picture = f.content_type
            instance.picture = bytearr # Overwrite with the actual image data

        if commit:
            instance.save()
        return instance