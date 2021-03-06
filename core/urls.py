from django.conf.urls import patterns, url



from core.views.book_views import *
urlpatterns = patterns('',
    url(
        regex=r'^book/archive/$',
        view=BookArchiveIndexView.as_view(),
        name='core_book_archive_index'
    ),
    url(
        regex=r'^book/create/$',
        view=BookCreateView.as_view(),
        name='core_book_create'
    ),
    url(
        regex=r'^book/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=BookDateDetailView.as_view(),
        name='core_book_date_detail'
    ),
    url(
        regex=r'^book/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=BookDayArchiveView.as_view(),
        name='core_book_day_archive'
    ),
    url(
        regex=r'^book/(?P<pk>\d+?)/delete/$',
        view=BookDeleteView.as_view(),
        name='core_book_delete'
    ),
    url(
        regex=r'^book/(?P<pk>\d+?)/$',
        view=BookDetailView.as_view(),
        name='core_book_detail'
    ),
    url(
        regex=r'^book/$',
        view=BookListView.as_view(),
        name='core_book_list'
    ),
    url(
        regex=r'^book/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=BookMonthArchiveView.as_view(),
        name='core_book_month_archive'
    ),
    url(
        regex=r'^book/today/$',
        view=BookTodayArchiveView.as_view(),
        name='core_book_today_archive'
    ),
    url(
        regex=r'^book/(?P<pk>\d+?)/update/$',
        view=BookUpdateView.as_view(),
        name='core_book_update'
    ),
    url(
        regex=r'^book/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=BookWeekArchiveView.as_view(),
        name='core_book_week_archive'
    ),
    url(
        regex=r'^book/archive/(?P<year>\d{4})/$',
        view=BookYearArchiveView.as_view(),
        name='core_book_year_archive'
    ),
)


from core.views.publishinghouse_views import *
urlpatterns += patterns('',
    url(
        regex=r'^publishinghouse/archive/$',
        view=PublishingHouseArchiveIndexView.as_view(),
        name='core_publishinghouse_archive_index'
    ),
    url(
        regex=r'^publishinghouse/create/$',
        view=PublishingHouseCreateView.as_view(),
        name='core_publishinghouse_create'
    ),
    url(
        regex=r'^publishinghouse/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=PublishingHouseDateDetailView.as_view(),
        name='core_publishinghouse_date_detail'
    ),
    url(
        regex=r'^publishinghouse/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=PublishingHouseDayArchiveView.as_view(),
        name='core_publishinghouse_day_archive'
    ),
    url(
        regex=r'^publishinghouse/(?P<pk>\d+?)/delete/$',
        view=PublishingHouseDeleteView.as_view(),
        name='core_publishinghouse_delete'
    ),
    url(
        regex=r'^publishinghouse/(?P<pk>\d+?)/$',
        view=PublishingHouseDetailView.as_view(),
        name='core_publishinghouse_detail'
    ),
    url(
        regex=r'^publishinghouse/$',
        view=PublishingHouseListView.as_view(),
        name='core_publishinghouse_list'
    ),
    url(
        regex=r'^publishinghouse/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=PublishingHouseMonthArchiveView.as_view(),
        name='core_publishinghouse_month_archive'
    ),
    url(
        regex=r'^publishinghouse/today/$',
        view=PublishingHouseTodayArchiveView.as_view(),
        name='core_publishinghouse_today_archive'
    ),
    url(
        regex=r'^publishinghouse/(?P<pk>\d+?)/update/$',
        view=PublishingHouseUpdateView.as_view(),
        name='core_publishinghouse_update'
    ),
    url(
        regex=r'^publishinghouse/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=PublishingHouseWeekArchiveView.as_view(),
        name='core_publishinghouse_week_archive'
    ),
    url(
        regex=r'^publishinghouse/archive/(?P<year>\d{4})/$',
        view=PublishingHouseYearArchiveView.as_view(),
        name='core_publishinghouse_year_archive'
    ),
)


from core.views.author_views import *
urlpatterns += patterns('',
    url(
        regex=r'^author/archive/$',
        view=AuthorArchiveIndexView.as_view(),
        name='core_author_archive_index'
    ),
    url(
        regex=r'^author/create/$',
        view=AuthorCreateView.as_view(),
        name='core_author_create'
    ),
    url(
        regex=r'^author/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=AuthorDateDetailView.as_view(),
        name='core_author_date_detail'
    ),
    url(
        regex=r'^author/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=AuthorDayArchiveView.as_view(),
        name='core_author_day_archive'
    ),
    url(
        regex=r'^author/(?P<pk>\d+?)/delete/$',
        view=AuthorDeleteView.as_view(),
        name='core_author_delete'
    ),
    url(
        regex=r'^author/(?P<pk>\d+?)/$',
        view=AuthorDetailView.as_view(),
        name='core_author_detail'
    ),
    url(
        regex=r'^author/$',
        view=AuthorListView.as_view(),
        name='core_author_list'
    ),
    url(
        regex=r'^author/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=AuthorMonthArchiveView.as_view(),
        name='core_author_month_archive'
    ),
    url(
        regex=r'^author/today/$',
        view=AuthorTodayArchiveView.as_view(),
        name='core_author_today_archive'
    ),
    url(
        regex=r'^author/(?P<pk>\d+?)/update/$',
        view=AuthorUpdateView.as_view(),
        name='core_author_update'
    ),
    url(
        regex=r'^author/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=AuthorWeekArchiveView.as_view(),
        name='core_author_week_archive'
    ),
    url(
        regex=r'^author/archive/(?P<year>\d{4})/$',
        view=AuthorYearArchiveView.as_view(),
        name='core_author_year_archive'
    ),
)


from core.views.author_views import *
urlpatterns += patterns('',
    url(
        regex=r'^author/archive/$',
        view=AuthorArchiveIndexView.as_view(),
        name='core_author_archive_index'
    ),
    url(
        regex=r'^author/create/$',
        view=AuthorCreateView.as_view(),
        name='core_author_create'
    ),
    url(
        regex=r'^author/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=AuthorDateDetailView.as_view(),
        name='core_author_date_detail'
    ),
    url(
        regex=r'^author/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=AuthorDayArchiveView.as_view(),
        name='core_author_day_archive'
    ),
    url(
        regex=r'^author/(?P<pk>\d+?)/delete/$',
        view=AuthorDeleteView.as_view(),
        name='core_author_delete'
    ),
    url(
        regex=r'^author/(?P<pk>\d+?)/$',
        view=AuthorDetailView.as_view(),
        name='core_author_detail'
    ),
    url(
        regex=r'^author/$',
        view=AuthorListView.as_view(),
        name='core_author_list'
    ),
    url(
        regex=r'^author/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=AuthorMonthArchiveView.as_view(),
        name='core_author_month_archive'
    ),
    url(
        regex=r'^author/today/$',
        view=AuthorTodayArchiveView.as_view(),
        name='core_author_today_archive'
    ),
    url(
        regex=r'^author/(?P<pk>\d+?)/update/$',
        view=AuthorUpdateView.as_view(),
        name='core_author_update'
    ),
    url(
        regex=r'^author/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=AuthorWeekArchiveView.as_view(),
        name='core_author_week_archive'
    ),
    url(
        regex=r'^author/archive/(?P<year>\d{4})/$',
        view=AuthorYearArchiveView.as_view(),
        name='core_author_year_archive'
    ),
)
