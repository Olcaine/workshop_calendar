from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import ListView
from django.conf import settings
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from django.conf.urls.static import static

from schedule.views import *
from schedule.models import Calendar

admin.autodiscover()

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
     url(r'^', include(router.urls)),
     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^fullcalendar/(?P<calendar_slug>[-\w]+)/$',
        FullCalendarView.as_view(),
        name='fullcalendar'),

    # Event Urls
    url(r'^event/create/(?P<calendar_slug>[-\w]+)/$',
        CreateEventView.as_view(),
        name='calendar_create_event'),
    url(r'^event/edit/(?P<calendar_slug>[-\w]+)/(?P<event_id>\d+)/$',
        EditEventView.as_view(),
        name='edit_event'),
    url(r'^event/(?P<event_id>\d+)/$',
        EventView.as_view(),
        name='event'),
    url(r'^event/delete/(?P<event_id>\d+)/$',
        DeleteEventView.as_view(),
        name='delete_event'),

    # urls for already persisted occurrences
    url(r'^occurrence/(?P<event_id>\d+)/(?P<occurrence_id>\d+)/$',
        OccurrenceView.as_view(),
        name='occurrence'),
    url(r'^occurrence/cancel/(?P<event_id>\d+)/(?P<occurrence_id>\d+)/$',
        CancelOccurrenceView.as_view(),
        name='cancel_occurrence'),
    url(r'^occurrence/edit/(?P<event_id>\d+)/(?P<occurrence_id>\d+)/$',
        EditOccurrenceView.as_view(),
        name='edit_occurrence'),

    # urls for unpersisted occurrences
    url(r'^occurrence/(?P<event_id>\d+)/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<hour>\d+)/(?P<minute>\d+)/(?P<second>\d+)/$',
        OccurrencePreview.as_view(),
        name='occurrence_by_date'),
    url(r'^occurrence/cancel/(?P<event_id>\d+)/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<hour>\d+)/(?P<minute>\d+)/(?P<second>\d+)/$',
        CancelOccurrenceView.as_view(),
        name='cancel_occurrence_by_date'),
    url(r'^occurrence/edit/(?P<event_id>\d+)/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<hour>\d+)/(?P<minute>\d+)/(?P<second>\d+)/$',
        CreateOccurrenceView.as_view(),
        name='edit_occurrence_by_date'),

    # api urls
    url(r'^api/occurrences', api_occurrences, name='api_occurrences'),
    url(r'^api/move_or_resize/$',
        api_move_or_resize_by_code,
        name='api_move_or_resize'),
    url(r'^api/select_create/$',
        api_select_create,
        name='api_select_create'),
    url(r'^$', ListView.as_view(queryset=Calendar.objects.all()), name='schedule'),
]
