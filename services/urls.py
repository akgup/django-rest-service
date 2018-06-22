from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from services.views import genericview

urlpatterns = [

    url(r'^employees/$', genericview.SnippetList.as_view()),
    url(r'^employees/(?P<pk>[0-9]+)$', genericview.SnippetDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
