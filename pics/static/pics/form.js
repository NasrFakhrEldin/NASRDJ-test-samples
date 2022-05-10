// <!-- https://stackoverflow.com/questions/2472422/django-file-upload-size-limit -->

// <!-- The problem with only having server-side validation is that
// the validation only happens after the upload is complete.
// Imagine, uploading a huge file, waiting for ages, only to be told afterwards that the file is too big.
// Wouldn't it be nicer if the browser could let me know beforehand that the file is too big?

// Well, there is a way to this client side, using HTML5 File API!

// Here's the required Javascript (depending on JQuery): -->

$("#upload_form").submit(function() {
  console.log('Checking file size');
  if (window.File && window.FileReader && window.FileList && window.Blob) {
      var file = $('#id_{{ form.upload_field_name }}')[0].files[0];
      if (file && file.size > {{ form.max_upload_limit }} ) {
          alert("File " + file.name + " of type " + file.type + " must be < {{ form.max_upload_limit_text }}");
      return false;
    }
  }
});