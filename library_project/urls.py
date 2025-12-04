from django.urls import path
from library_app import views
from django.contrib import admin

urlpatterns = [
    path("", views.home, name="home"),

    # auth
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("forgot-password/", views.forgot_password, name="forgot_password"),

    # books
    path("books/", views.book_list, name="book_list"),
    path("books/add/", views.add_book, name="add_book"),
    path("books/<str:book_id>/edit/", views.update_book, name="update_book"),
    path("books/<str:book_id>/delete/", views.delete_book, name="delete_book"),

    # members
    path("members/", views.member_list, name="member_list"),
    path("members/add/", views.add_member, name="add_member"),
    path("members/<str:member_id>/edit/", views.update_member, name="update_member"),
    path("members/<str:member_id>/delete/", views.delete_member, name="delete_member"),
    path("forgot-password/", views.forgot_password, name="forgot_password"),


    # borrowing
    path("borrow/", views.borrow_book, name="borrow_book"),
    path("borrowed/", views.borrowed_books, name="borrowed_books"),
    path("transactions/", views.transactions_view, name="transactions"),


    # shop & purchases
    path("shop/", views.shop_books, name="shop_books"),
    path("shop/buy/<str:book_id>/", views.buy_book, name="buy_book"),
    path("shop/buy/title/<str:title>/", views.buy_book_by_title, name="buy_book_by_title"),
    path("purchases/", views.purchase_history, name="purchase_history"),

    # rating
    path("rate/", views.rate_system, name="rate_system"),
    path("ratings/", views.ratings, name="ratings"),
    path("admin/", admin.site.urls),
]
