from django.forms.models import inlineformset_factory

from .models import Vehicle, Parts

VehiclePartsFormset = inlineformset_factory(Vehicle, Parts, fields=('title', 'quantity', 'delivered', 'fitted',))