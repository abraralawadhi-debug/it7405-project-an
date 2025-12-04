from djongo import models


# ----------------- BOOKS (Mongo: books) -----------------
class Book(models.Model):
    _id = models.ObjectIdField(primary_key=True)   # maps to MongoDB _id
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "books"  # existing "books" collection
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return f"{self.title} ({self.author})"


# ----------------- MEMBERS (Mongo: members) -----------------
class Member(models.Model):
    _id = models.ObjectIdField(primary_key=True)   # maps to MongoDB _id
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=255, blank=True)  # plain for now

    class Meta:
        db_table = "members"
        verbose_name = "Member"
        verbose_name_plural = "Members"

    def __str__(self):
        return f"{self.name} <{self.email}>"


# ----------------- TRANSACTIONS (Mongo: transactions) -----------------
class Transaction(models.Model):
    _id = models.ObjectIdField(primary_key=True)

    # store the related Mongo _id values as strings
    member_id = models.CharField(max_length=255)     # ObjectId of member as string
    book_id = models.CharField(max_length=255)       # ObjectId of book as string

    borrow_date = models.CharField(max_length=50, blank=True)
    return_date = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = "transactions"
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        return f"Transaction {self._id}"


# ----------------- PURCHASES (Mongo: purchases) -----------------
class Purchase(models.Model):
    _id = models.ObjectIdField(primary_key=True)

    member_id = models.CharField(max_length=255)     # ObjectId of member as string
    book_id = models.CharField(max_length=255)       # ObjectId of book as string

    quantity = models.IntegerField()
    purchase_date = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = "purchases"
        verbose_name = "Purchase"
        verbose_name_plural = "Purchases"

    def __str__(self):
        return f"Purchase {self._id}"


# ----------------- RATINGS (Mongo: ratings) -----------------
class Rating(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)

    # who submitted the rating
    member_name = models.CharField(max_length=255, blank=True)
    member_email = models.EmailField(max_length=255, blank=True)

    class Meta:
        db_table = "ratings"
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

    def __str__(self):
        return f"{self.rating} by {self.member_name or 'Unknown'}"
