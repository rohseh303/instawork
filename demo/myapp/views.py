from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import TeamMember
from .forms import TeamMemberForm

class TeamMemberListView(ListView):
    model = TeamMember
    template_name = 'team_member_list.html'
    context_object_name = 'team_members'

class TeamMemberCreateView(CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'team_member_form.html'
    success_url = reverse_lazy('team_member_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TeamMemberUpdateView(UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'team_member_edit.html'
    context_object_name = 'member'
    success_url = reverse_lazy('team_member_list')

from django.http import HttpResponseRedirect

class TeamMemberDeleteView(DeleteView):
    model = TeamMember
    success_url = reverse_lazy('team_member_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.success_url)