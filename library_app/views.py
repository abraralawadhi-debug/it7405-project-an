from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from bson import ObjectId
from .mongo_connection import get_db


# ----------------- HOME PAGE -----------------
def home(request):
    return render(request, "home.html")


# ----------------- BOOKS -----------------
def book_list(request):
    db = get_db()
    books_col = db["books"]

    books = []
    for b in books_col.find():
        b["id"] = str(b["_id"])   
        books.append(b)

    return render(request, "book_list.html", {"books": books})


def add_book(request):
    db = get_db()
    books_col = db["books"]

    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        year = request.POST.get("year")

        try:
            year = int(year)
        except (TypeError, ValueError):
            year = None

        books_col.insert_one({
            "title": title,
            "author": author,
            "year": year,
        })

        return redirect("book_list")

    return render(request, "add_book.html")


def update_book(request, book_id):
    db = get_db()
    books_col = db["books"]

    try:
        mongo_id = ObjectId(book_id)
    except Exception:
        return redirect("book_list")

    book = books_col.find_one({"_id": mongo_id})
    if not book:
        return redirect("book_list")

    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        year = request.POST.get("year")

        try:
            year = int(year)
        except (TypeError, ValueError):
            year = None

        books_col.update_one(
            {"_id": mongo_id},
            {"$set": {
                "title": title,
                "author": author,
                "year": year,
            }}
        )

        return redirect("book_list")

    return render(request, "edit_book.html", {"book": book, "book_id": book_id})


def delete_book(request, book_id):
    db = get_db()
    books_col = db["books"]

    books_col.delete_one({"_id": ObjectId(book_id)})
    return redirect("book_list")


# ----------------- MEMBERS -----------------
def member_list(request):
    db = get_db()
    members_col = db["members"]

    members = []
    for m in members_col.find():
        m["id"] = str(m["_id"])
        members.append(m)

    return render(request, "member_list.html", {"members": members})


def add_member(request):
    db = get_db()
    members_col = db["members"]

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        members_col.insert_one({
            "name": name,
            "email": email,
        })
        return redirect("member_list")

    return render(request, "add_member.html")


def update_member(request, member_id):
    db = get_db()
    members_col = db["members"]

    try:
        mongo_id = ObjectId(member_id)
    except Exception:
        return redirect("member_list")

    member = members_col.find_one({"_id": mongo_id})
    if not member:
        return redirect("member_list")

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        members_col.update_one(
            {"_id": mongo_id},
            {"$set": {
                "name": name,
                "email": email,
            }}
        )
        return redirect("member_list")

    return render(request, "edit_member.html", {"member": member, "member_id": member_id})


def delete_member(request, member_id):
    db = get_db()
    members_col = db["members"]

    members_col.delete_one({"_id": ObjectId(member_id)})
    return redirect("member_list")


# ----------------- BORROW BOOK -----------------
def borrow_book(request):
    db = get_db()
    books_col = db["books"]
    members_col = db["members"]
    transactions_col = db["transactions"]

    if request.method == "POST":
        member_id = request.POST.get("member_id")
        book_id = request.POST.get("book_id")
        borrow_date = request.POST.get("borrow_date")

        # Insert a new transaction document in MongoDB
        try:
            transactions_col.insert_one({
                "member_id": ObjectId(member_id),
                "book_id": ObjectId(book_id),
                "borrow_date": borrow_date,
                "return_date": None,
            })
        except Exception:
            
            pass

        # 🔹 after borrowing, go to the transactions page
        return redirect("transactions")

    # GET: show the borrow form
    members = []
    for m in members_col.find():
        m["id"] = str(m["_id"])
        members.append(m)

    books = []
    for b in books_col.find():
        b["id"] = str(b["_id"])
        books.append(b)

    return render(request, "borrow_book.html", {
        "members": members,
        "books": books,
    })


# ----------------- RETURN BOOK -----------------
def return_book(request, transaction_id):
    db = get_db()
    transactions_col = db["transactions"]

    if request.method == "POST":
        return_date = request.POST.get("return_date")

        try:
            transactions_col.update_one(
                {"_id": ObjectId(transaction_id)},
                {"$set": {"return_date": return_date}},
            )
        except Exception:
            pass

        # 🔹 after returning, also go to the transactions page
        return redirect("transactions")

    return render(request, "return_book.html")



# ----------------- LIST BORROWED BOOKS -----------------
def borrowed_books(request):
    db = get_db()
    books_col = db["books"]
    members_col = db["members"]
    transactions_col = db["transactions"]

    results = []

    for tx in transactions_col.find():
        member = members_col.find_one({"_id": tx["member_id"]})
        book = books_col.find_one({"_id": tx["book_id"]})

        results.append({
            "id": str(tx["_id"]),
            "member_name": member["name"] if member else "Unknown",
            "book_title": book["title"] if book else "Unknown",
            "borrow_date": tx.get("borrow_date"),
            "return_date": tx.get("return_date"),
        })

    return render(request, "borrowed_books.html", {"transactions": results})


# ----------------- RETURN BOOK -----------------
def return_book(request, transaction_id):
    db = get_db()
    transactions_col = db["transactions"]

    if request.method == "POST":
        return_date = request.POST.get("return_date")

        transactions_col.update_one(
            {"_id": ObjectId(transaction_id)},
            {"$set": {"return_date": return_date}},
        )
        return redirect("borrowed_books")

    return render(request, "return_book.html")


# ----------------- SHOP -----------------
def shop_books(request):
    return render(request, "shop_books.html")


# ----------------- BUY ONE BOOK (by ObjectId) -----------------
def buy_book(request, book_id):
    db = get_db()
    books_col = db["books"]
    members_col = db["members"]
    purchases_col = db["purchases"]

    try:
        mongo_id = ObjectId(book_id)
    except Exception:
        return redirect("shop_books")

    book = books_col.find_one({"_id": mongo_id})
    if not book:
        return redirect("shop_books")

    members = []
    for m in members_col.find():
        m["id"] = str(m["_id"])
        members.append(m)

    if request.method == "POST":
        member_id = request.POST.get("member_id")
        quantity = int(request.POST.get("quantity"))
        purchase_date = request.POST.get("purchase_date")

        purchases_col.insert_one({
            "member_id": ObjectId(member_id),
            "book_id": book["_id"],
            "quantity": quantity,
            "purchase_date": purchase_date,
        })

        return redirect("purchase_history")

    return render(request, "buy_book.html", {
        "title": f"Buy {book.get('title', '')}",
        "book": book,
        "members": members,
    })


# ----------------- BUY BOOK BY TITLE -----------------
def buy_book_by_title(request, title):
    db = get_db()
    books_col = db["books"]

    book = books_col.find_one({"title": title})
    if not book:
        return redirect("shop_books")

    return buy_book(request, str(book["_id"]))


# ----------------- PURCHASE HISTORY -----------------
def purchase_history(request):
    db = get_db()
    books_col = db["books"]
    members_col = db["members"]
    purchases_col = db["purchases"]

    records = []

    for p in purchases_col.find():
        member = members_col.find_one({"_id": p["member_id"]})
        book = books_col.find_one({"_id": p["book_id"]})

        records.append({
            "member_name": member["name"] if member else "Unknown",
            "book_title": book["title"] if book else "Unknown",
            "quantity": p.get("quantity"),
            "purchase_date": p.get("purchase_date"),
        })

    return render(request, "purchase_history.html", {"purchases": records})


# ----------------- RATING SYSTEM -----------------
from django.contrib import messages
from bson import ObjectId
from .mongo_connection import get_db


def rate_system(request):
    """
    Let ONLY logged-in members rate the system.
    Save rating + comment + member name + email into MongoDB (ratings collection).
    """
    
    if "member_id" not in request.session:
        messages.error(request, "Please login first to rate the system.")
        return redirect("login")

    db = get_db()
    ratings_col = db["ratings"]
    members_col = db["members"]

    if request.method == "POST":
        # rating value (1-5) and optional comment
        rating = int(request.POST.get("rating"))
        comment = request.POST.get("comment", "").strip()

        
        member_id = request.session.get("member_id")
        member_name = request.session.get("member_name", "")
        member_email = ""

        try:
            member_doc = members_col.find_one({"_id": ObjectId(member_id)})
            if member_doc:
                if not member_name:
                    member_name = member_doc.get("name", "") or ""
                member_email = member_doc.get("email", "") or ""
        except Exception:
            
            pass

        # 3) Save rating document with member details
        ratings_col.insert_one({
            "rating": rating,
            "comment": comment,
            "member_name": member_name,
            "member_email": member_email,
        })

        messages.success(request, "Thank you for your feedback!")
        return redirect("ratings")

    # GET request -> show the rating form
    return render(request, "rate_system.html")


def ratings(request):
    """
    List all ratings (used by the /ratings/ page).
    """
    db = get_db()
    ratings_col = db["ratings"]

    ratings_list = []
    for r in ratings_col.find():
        r["id"] = str(r["_id"])
        ratings_list.append(r)

    return render(request, "ratings.html", {"ratings": ratings_list})
 



# ----------------- AUTH: REGISTER / LOGIN / LOGOUT -----------------
def register(request):
    db = get_db()
    members_collection = db["members"]

    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip().lower()
        phone = request.POST.get("phone", "").strip()
        password = request.POST.get("password", "").strip()
        confirm_password = request.POST.get("confirm_password", "").strip()

        if not full_name or not email or not phone or not password:
            messages.error(request, "Please fill in all the fields.")
            return render(request, "register.html")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "register.html")

        existing = members_collection.find_one({"email": email})
        if existing:
            messages.error(request, "This email is already registered. Please login instead.")
            return redirect("login")

        new_member = {
            "name": full_name,
            "email": email,
            "phone": phone,
            "password": password,
        }

        result = members_collection.insert_one(new_member)

        request.session["member_id"] = str(result.inserted_id)
        request.session["member_name"] = full_name

        messages.success(request, "Account created successfully! You are now logged in.")
        return redirect("home")

    return render(request, "register.html")


def login_view(request):
    db = get_db()
    members_collection = db["members"]

    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "").strip()

        member = members_collection.find_one({"email": email, "password": password})
        if member:
            request.session["member_id"] = str(member["_id"])
            request.session["member_name"] = member.get("name", "")
            messages.success(request, f"Welcome back, {member.get('name', 'Member')}!")
            return redirect("home")
        else:
            messages.error(request, "Invalid email or password.")
            return render(request, "login.html")

    return render(request, "login.html")


def logout_view(request):
    request.session.flush()
    messages.info(request, "You have been logged out.")
    return redirect("login")


def forgot_password(request):
    """
    Simple page telling the user how to reset their password.
    """
    return render(request, "forgot_password.html")



# ----------------- DASHBOARD -----------------
def dashboard(request):
    if "member_id" not in request.session:
        messages.error(request, "Please login first to access the dashboard.")
        return redirect("login")

    db = get_db()
    books_col = db["books"]
    members_col = db["members"]
    transactions_col = db["transactions"]

    total_books = books_col.count_documents({})
    total_members = members_col.count_documents({})
    total_borrowed = transactions_col.count_documents({"return_date": None})
    total_available = max(total_books - total_borrowed, 0)

    latest_transactions = []
    for tx in transactions_col.find().sort("_id", -1).limit(5):
        member = members_col.find_one({"_id": tx["member_id"]})
        book = books_col.find_one({"_id": tx["book_id"]})

        latest_transactions.append({
            "member_name": (member.get("name") if member else "Unknown"),
            "book_title": (book.get("title") if book else "Unknown"),
            "borrow_date": tx.get("borrow_date"),
            "return_date": tx.get("return_date"),
        })

    context = {
        "total_books": total_books,
        "total_members": total_members,
        "total_borrowed": total_borrowed,
        "total_available": total_available,
        "latest_transactions": latest_transactions,
    }

    return render(request, "dashboard.html", context)
    # ----------------- LIST ALL TRANSACTIONS PAGE -----------------
def transactions_view(request):
    """
    Show all borrowing transactions (member + book details)
    in the transactions.html template.
    """
    db = get_db()
    books_col = db["books"]
    members_col = db["members"]
    transactions_col = db["transactions"]

    results = []

    for tx in transactions_col.find():
        member = members_col.find_one({"_id": tx["member_id"]})
        book = books_col.find_one({"_id": tx["book_id"]})

        results.append({
            "id": str(tx["_id"]),
            "member_name": member["name"] if member else "Unknown",
            "member_email": member.get("email", "") if member else "",
            "book_title": book["title"] if book else "Unknown",
            "borrow_date": tx.get("borrow_date"),
            "return_date": tx.get("return_date"),
        })

    return render(request, "transactions.html", {"transactions": results})

    

