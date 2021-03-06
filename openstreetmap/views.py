from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import reverse
from django.template.loader import render_to_string
from django.views.generic import CreateView, ListView, DetailView, DeleteView, FormView

from .forms import MyOsmForm, ContactForm
from .models import MyOsm, Customer


class MyOsmView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "openstreetmap/myosm_form.html"
    form_class = MyOsmForm
    model = MyOsm
    success_message = "Centre ajouté"

    def get_success_url(self):
        return reverse("index")


class MyOsmDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = "openstreetmap/myosm_delete.html"
    model = MyOsm
    success_message = 'centre supprimé'
    success_url = '/'


class IndexListView(ListView):
    model = MyOsm
    template_name = 'index.html'


class ContactFormView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_message = 'Votre message a été envoyé'
    success_url = '/'

    # def get_center(self):
    #    center= MyOsm.objects.filter(location=self.kwargs['pk'])
    #    return center

    def form_valid(self, form):
        obj = form.save(commit=False)
        form['center'] = Customer.objects.get(id=self.kwargs['pk'])
        obj.save()
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('name')
        message = form.cleaned_data.get('message')
        send_mail(
            subject, message, email, ['contact@onlineformapro.com']
        )
        feedback = render_to_string('confirm.html', {'name': subject})
        email_conf = EmailMessage("Your request is in process", feedback, settings.EMAIL_HOST_USER, [email])
        email_conf.send()
        return super(ContactFormView, self).form_valid(form)


class CenterMessagesListView(LoginRequiredMixin, ListView):
    template_name = 'centermessages.html'
    model = Customer
    ordering = ['-date']


class CenterMessagesDetailView(LoginRequiredMixin, DetailView):
    template_name = 'message_detail.html'
    model = Customer


class CenterMessagesDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'message_delete.html'
    model = Customer
    success_url = '/messages/'
