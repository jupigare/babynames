from django import forms
from ..faves.models import Frequency

# class FilterForm(forms.Form):
# 	year = forms.CharField(max_length=4, label = "Year")
# 	state = forms.CharField(max_length=2, label = "State")
# 	gender = forms.CharField(max_length=1, label = "Gender")

	# class Meta:
	# 	model = Frequency

class FilterMixin(object):

    def get_queryset_filters(self):
        filters = {}
        for item in self.allowed_filters:
            if item in self.request.GET:
                 filters[self.allowed_filters[item]] = self.request.GET[item]
        return filters

    def get_queryset(self):
        return super(FilterMixin, self).get_queryset()\
              .filter(**self.get_queryset_filters())


class NameListView(FilterMixin, ListView):

    allowed_filters = {
        'gender': 'gender',
        'state': 'state',
        'year': 'year',
    }
    # no need to override get_queryset