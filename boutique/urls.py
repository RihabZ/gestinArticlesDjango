from django.urls import path
from. import views

urlpatterns =[
    path('', views.connect, name='connect'),
    path('login/login/', views.signIn, name='signIn'),
    path('login/', views.signIn, name='signIn'),
    path('disconnect/', views.signOut, name='disconnect'),

    path('boutique/', views.homepage,name='homepage'),
    #path('add/',views.add_model),
    #path('modif/<int:id',views.modif_model),
    path('boutique/addprod/', views.add, name='add'),
    path('boutique/addprod/add_prod/', views.add_prod, name='add_prod'),
    path('boutique/del_art/<int:id>', views.del_art, name='del_art'),
    path('boutique/update_typ/<int:id>', views.update_typ,name='update_typ'),
    path('boutique/update_typ/update/<int:id>',views.update, name='update'),
    



    
]