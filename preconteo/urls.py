from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    url(r'^$', 'counter.views.alcaldia', name='home'),
    url(r'^alcaldia$', 'counter.views.alcaldia', name='alcaldia'),
    url(r'^gobernacion$', 'counter.views.gobernacion', name='gobernacion'),
    url(r'^asamblea$', 'counter.views.asamblea', name='asamblea'),
    url(r'^concejo$', 'counter.views.concejo', name='concejo'),
    url(r'^jal$', 'counter.views.jal', name='jal'),
    url(r'^novedades$', 'counter.views.observaciones', name='novedades'),
    url(r'^admin/', include(admin.site.urls)),
]
