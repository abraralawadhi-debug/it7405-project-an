from django.contrib import admin
from .models import Book, Member, Transaction, Purchase, Rating


# ========== BOOKS ==========
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "year")
    search_fields = ("title", "author")
    list_filter = ("year",)


# ========== MEMBERS ==========
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")
    search_fields = ("name", "email")
    list_filter = ()


# ========== TRANSACTIONS (Borrowed Books) ==========
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "member_name_display",
        "book_title_display",
        "borrow_date",
        "return_date",
    )
    list_filter = ("borrow_date", "return_date")
    search_fields = ("borrow_date", "return_date")

    
    def member_name_display(self, obj):
        # obj.member_id is an ObjectId; we stored the real Member separately in Mongo.
        # In admin, Djongo loads Transaction as a normal model, so we can join via Member pk.
        member = Member.objects.filter(pk=obj.member_id).first()
        return member.name if member else "—"

    member_name_display.short_description = "Member"

    def book_title_display(self, obj):
        from .models import Book  

        book = Book.objects.filter(pk=obj.book_id).first()
        return book.title if book else "—"

    book_title_display.short_description = "Book"


# ========== PURCHASES ==========
@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = (
        "member_name_display",
        "book_title_display",
        "quantity",
        "purchase_date",
    )
    list_filter = ("purchase_date",)
    search_fields = ("purchase_date",)

    def member_name_display(self, obj):
        member = Member.objects.filter(pk=obj.member_id).first()
        return member.name if member else "—"

    member_name_display.short_description = "Member"

    def book_title_display(self, obj):
        from .models import Book

        book = Book.objects.filter(pk=obj.book_id).first()
        return book.title if book else "—"

    book_title_display.short_description = "Book"


# ========== RATINGS ==========
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    
    list_display = ("member_name", "member_email", "rating", "comment")
    list_filter = ("rating",)
    search_fields = ("member_name", "member_email", "comment")

    
