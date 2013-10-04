from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from core.models import PublishingHouse
from core.forms import PublishingHouseForm


class PublishingHouseView(object):
    model = PublishingHouse
    form_class = PublishingHouseForm

    def get_template_names(self):
        """Nest templates within publishinghouse directory."""
        tpl = super(PublishingHouseView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'publishinghouse'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class PublishingHouseDateView(PublishingHouseView):
    date_field = 'created_at'
    month_format = '%m'


class PublishingHouseBaseListView(PublishingHouseView):
    paginate_by = 10


class PublishingHouseArchiveIndexView(
    PublishingHouseDateView, PublishingHouseBaseListView, ArchiveIndexView):
    pass


class PublishingHouseCreateView(PublishingHouseView, CreateView):
    pass


class PublishingHouseDateDetailView(PublishingHouseDateView, DateDetailView):
    pass


class PublishingHouseDayArchiveView(
    PublishingHouseDateView, PublishingHouseBaseListView, DayArchiveView):
    pass


class PublishingHouseDeleteView(PublishingHouseView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('core_publishinghouse_list')


class PublishingHouseDetailView(PublishingHouseView, DetailView):
    pass


class PublishingHouseListView(PublishingHouseBaseListView, ListView):
    pass


class PublishingHouseMonthArchiveView(
    PublishingHouseDateView, PublishingHouseBaseListView, MonthArchiveView):
    pass


class PublishingHouseTodayArchiveView(
    PublishingHouseDateView, PublishingHouseBaseListView, TodayArchiveView):
    pass


class PublishingHouseUpdateView(PublishingHouseView, UpdateView):
    pass


class PublishingHouseWeekArchiveView(
    PublishingHouseDateView, PublishingHouseBaseListView, WeekArchiveView):
    pass


class PublishingHouseYearArchiveView(
    PublishingHouseDateView, PublishingHouseBaseListView, YearArchiveView):
    make_object_list = True



