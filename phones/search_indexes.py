from haystack import indexes
from phones.models import Person, Unit, Position


class PersonIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.SearchField(document=True, use_template=True)
    content_auto = indexes.EdgeNgramField(model_attr='last_name')


    def get_model(self):
        return Person

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class UnitIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.SearchField(document=True, use_template=True)

    def get_model(self):
        return Unit

    def index_queryset(self, using=None):
        return self.get_model().objects.all().order_by('unit_name')


