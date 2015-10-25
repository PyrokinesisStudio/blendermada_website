from django.conf.urls import url

from . import recievers
from .views import UploadView, UploadDetailView, StuffView, UploadApproveView


urlpatterns = [

    url(r'^upload/$', UploadView.as_view(), name='uploads_upload'),
    url(r'^detail/(?P<pk>\d+)/$', UploadDetailView.as_view(), name='uploads_detail'),
    url(r'^approve/(?P<pk>\d+)/$', UploadApproveView.as_view(), name='uploads_approve'),
    url(r'^stuff/$', StuffView.as_view(), name='uploads_stuff')

]
