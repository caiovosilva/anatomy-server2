"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import ClienteViewSet, ModalityViewSet, AnatomicalRegionViewSet, AnatomyImageViewSet, AnswerViewSet, AssignmentViewSet, QuestionViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'modalities', ModalityViewSet)
router.register(r'anatomicalRegions', AnatomicalRegionViewSet)
router.register(r'anatomyImages', AnatomyImageViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'questions', QuestionViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
