from import_export import fields
from import_export import resources
from import_export import widgets
from occasion.models import *
from import_export.widgets import Widget
from occasion.models import Occasion
from import_export import widgets

class ClothingResource(resources.ModelResource):
    clothing_occasion = fields.Field(
        column_name='clothing_occasion',
        attribute='clothing_occasion',
        widget=widgets.ManyToManyWidget(model=Occasion, separator=',', field='occasion'),
    )

    class Meta:
        model = Clothing
        fields = ['id', 'Clothing', 'clothing_gender', 'clothing_temp', 'clothing_activity', 'clothing_occasion']


