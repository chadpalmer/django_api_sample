from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from axioms import views
from django.shortcuts import redirect


urlpatterns = [
    path('', lambda request: redirect('axioms/', permanent=True)),
    path('axioms/', views.index, name='index'),
    path('axioms/all/', views.AxiomList.as_view()),
    path('axioms/<int:pk>/', views.AxiomDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
