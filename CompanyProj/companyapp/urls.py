from django.conf.urls import url, include
from rest_framework import routers
from .views import CompanyViewSet, EmployeeDetailsViewSet, JobOpeningsViewViewSet, SearchFilterView

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'employee', EmployeeDetailsViewSet)
router.register(r'jobs', JobOpeningsViewViewSet)
#router.register(r'search', SearchQuery)

#urlpatterns = router.urls
urlpatterns = [
	url(r'^search/', SearchFilterView.as_view()),
        url(r'^', include(router.urls)),        
]
