from haystack import indexes
from phones.models import Person, Unit, Phone, PositionInUnit


class PersonIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.SearchField(document=True, use_template=True)
    last_name = indexes.CharField(model_attr='last_name')
    first_name = indexes.CharField(model_attr='first_name')
    middle_name = indexes.CharField(model_attr='middle_name')
    slug = indexes.CharField(model_attr='slug')
    phone = indexes.CharField(model_attr='get_first_phone_main')

    last_name_auto = indexes.EdgeNgramField(model_attr='last_name')

    def get_model(self):
        return Person

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class UnitIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.SearchField(document=True, use_template=True)
    unit_name = indexes.CharField(model_attr='unit_name')
    unit_short_name = indexes.CharField(model_attr='unit_short_name')

    unit_name_auto = indexes.EdgeNgramField(model_attr='unit_name')

    def get_model(self):
        return Unit

    def index_queryset(self, using=None):
        return self.get_model().objects.all().order_by('unit_name')


class PhoneIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.SearchField(document=True, use_template=True)

    def get_model(self):
        return Phone

    def index_queryset(self, using=None):
        return self.get_model().objects.all().order_by('number')

    def prepare_person(self, obj):
        # Store a list of id's for filtering
        return [person for person in obj.positioninunit.all()]
