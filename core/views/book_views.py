from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from core.models import Book
from core.forms import BookForm


class BookView(object):
    model = Book
    form_class = BookForm

    def get_template_names(self):
        """Nest templates within book directory."""
        tpl = super(BookView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'book'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class BookDateView(BookView):
    date_field = 'created_at'
    month_format = '%m'


class BookBaseListView(BookView):
    paginate_by = 10


class BookArchiveIndexView(
    BookDateView, BookBaseListView, ArchiveIndexView):
    pass


class BookCreateView(BookView, CreateView):
    pass


class BookDateDetailView(BookDateView, DateDetailView):
    pass


class BookDayArchiveView(
    BookDateView, BookBaseListView, DayArchiveView):
    pass


class BookDeleteView(BookView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('core_book_list')


class BookDetailView(BookView, DetailView):
    pass


class BookListView(BookBaseListView, ListView):
    pass


class BookMonthArchiveView(
    BookDateView, BookBaseListView, MonthArchiveView):
    pass


class BookTodayArchiveView(
    BookDateView, BookBaseListView, TodayArchiveView):
    pass


class BookUpdateView(BookView, UpdateView):
    pass


class BookWeekArchiveView(
    BookDateView, BookBaseListView, WeekArchiveView):
    pass


class BookYearArchiveView(
    BookDateView, BookBaseListView, YearArchiveView):
    make_object_list = True



