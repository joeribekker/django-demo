from django.http import HttpResponse
from django.views.generic import DetailView, View
from .models import Form, FormField, Submission

class FormDetailView(DetailView):
    model = Form
    template_name = "main.html"

class SubmissionView(View):

    # NOTE: This is very quick-and-dirty! Django can render forms and sanitize
    # the input in much more elegant ways. This code was added to make the
    # example functional and understandable.

    def post(self, request, *args, **kwargs):
        form_id = int(kwargs.get("pk"))

        # Store a submission object, that relates to the current form object.
        # The submission object is the container for all values for this form's 
        # fields.
        submission = Submission.objects.create(
            form = Form.objects.get(pk=form_id)
        )

        # Iterate over all values that were POSTed by the HTML-form.
        for form_field_id, value in request.POST.items():
            # Only process HTML-form keys that are integers and also assume
            # these match the primary key of a FormField object. If not, just
            # skip the HTML-form field.
            try:
                form_field_id = int(form_field_id)
            except ValueError:
                continue
            
            # Store the all values that were POSTed and link them to the proper
            # FormField that is part of the Form.
            submission.submissionfield_set.create(
                field = FormField.objects.get(pk=form_field_id),
                value = value
            )

        # Simply return the string "Thanks!" to the browser.
        return HttpResponse("Thanks!")
