from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from core.models import Author
from core.forms import AuthorForm


class AuthorView(object):
    model = Author
    form_class = AuthorForm

    def get_template_names(self):
        """Nest templates within author directory."""
        tpl = super(AuthorView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'author'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class AuthorDateView(AuthorView):
    date_field = 'created_at'
    month_format = '%m'


class AuthorBaseListView(AuthorView):
    paginate_by = 10


class AuthorArchiveIndexView(
    AuthorDateView, AuthorBaseListView, ArchiveIndexView):
    pass


class AuthorCreateView(AuthorView, CreateView):
    pass


class AuthorDateDetailView(AuthorDateView, DateDetailView):
    pass


class AuthorDayArchiveView(
    AuthorDateView, AuthorBaseListView, DayArchiveView):
    pass


class AuthorDeleteView(AuthorView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('core_author_list')


class AuthorDetailView(AuthorView, DetailView):
    pass


class AuthorListView(AuthorBaseListView, ListView):
    pass


class AuthorMonthArchiveView(
    AuthorDateView, AuthorBaseListView, MonthArchiveView):
    pass


class AuthorTodayArchiveView(
    AuthorDateView, AuthorBaseListView, TodayArchiveView):
    pass


class AuthorUpdateView(AuthorView, UpdateView):
    pass


class AuthorWeekArchiveView(
    AuthorDateView, AuthorBaseListView, WeekArchiveView):
    pass


class AuthorYearArchiveView(
    AuthorDateView, AuthorBaseListView, YearArchiveView):
    make_object_list = True



