from hstore_flattenfields.forms import *

from core.models import *

class AuthorForm(HStoreContentPaneModelForm):
    class Meta:
        model = Author


class BookForm(HStoreModelForm):
    class Meta:
        model = Book


class PublishingHouseForm(HStoreModelForm):
    class Meta:
        model = PublishingHouse
