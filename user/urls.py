from django.urls import path
from user import views

urlpatterns = [
    path("", views.create_user, name="create_user"),
    path("login/", views.login_view, name="login"),
    path("home/", views.home, name="home"),

    path("update/<int:id>/", views.update_user, name="update_user"),

    path("create_admin/", views.create_admin, name="create_admin"),


    path("category/create/", views.create_category, name="create_category"),
    path("category/list/", views.category_list, name="category_list"),

    path("dashboard/", views.dashboard, name="dashboard"),

   path("user/", views.user_list, name="user_list"),
   path("profile/", views.profile, name="profile"),
   path("logout/", views.logout_view, name="logout"),
   path("cart/", views.cart_view, name="cart"),
   path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
   path("cart/remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
   path("cart/increase/<int:item_id>/", views.increase_quantity, name="increase_quantity"),
   path("cart/decrease/<int:item_id>/", views.decrease_quantity, name="decrease_quantity"),
   path("checkout/", views.checkout, name="checkout"),
   path("products/", views.products, name="products"),
   path("category/<int:id>/",views.category_products,name="category_products"),


]
