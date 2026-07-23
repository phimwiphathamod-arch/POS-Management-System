from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect ,get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .models import Category, Manufacturer,Product,Supplier
from .forms import  CategoryForm, RegisterForm,UpdateUserForm
from .models import Product, Category,Brand,Manufacturer, Cart, CartItem, Product , Order, OrderItem ,Product, Category
from .decorators import admin_only


User = get_user_model()

# Register
def create_user(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']

            # เช็ค email ซ้ำ
            if User.objects.filter(email=email).exists():

                return render(
                    request,
                    'register.html',
                    {
                        'form': form,
                        'error': 'Email already exists'
                    }
                )

            user = form.save(commit=False)

            # hash password
            user.password = make_password(
                form.cleaned_data['password']
            )

            user.users_role = 'user'

            user.user_status = 'active'

            user.save()

            return redirect('login')

    else:

        form = RegisterForm()

    return render(
        request,
        'register.html',
        {'form': form}
    )
#create admin
def create_admin(request):

    check_admin = User.objects.filter(
        username='admin'
    ).first()

    if check_admin:
        return HttpResponse('admin already exists')

    admin_user = User.objects.create_superuser(
        username='admin',
        password='1234',
        email='admin@gmail.com'
    )

    admin_user.users_role = 'admin'
    admin_user.user_status = 'active'

    admin_user.save()

    return HttpResponse('admin created')

    
# Login
def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        # ใช้ authenticate ของ Django
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            # สำคัญมาก
            login(request, user)
 
            # ADMIN
            if user.is_superuser:
                return redirect('dashboard')
            # USER
            return redirect('home')

        else:

            return render(
                request,
                'login.html',
                {'error': 'username or password incorrect'}
            )

    return render(request, 'login.html')

# Logout
def logout_view(request):

    logout(request)

    return redirect('login')

# Home
def home(request):

    if not request.user.is_authenticated:
        return redirect('login')

    products = Product.objects.filter(
        is_active=True
    )

    categories = Category.objects.filter(
        categ_status='active'
    )

    context = {
        'user': request.user,
        'products': products,
        'categories': categories,

        'product_count': Product.objects.count(),
        'category_count': Category.objects.count(),
        'brand_count': Brand.objects.count(),
        'manufacturer_count': Manufacturer.objects.count(),
    }

    return render(
        request,
        'home.html',
        context
    )
# Update User
def update_user(request, id):

    user = User.objects.get(id=id)

    if request.method == "POST":

        form = UpdateUserForm(
            request.POST,
            instance=user
        )

        if form.is_valid():

            form.save()

            return redirect('home')

    else:

        form = UpdateUserForm(
            instance=user
        )

    return render(
        request,
        'update_user.html',
        {
            'form': form,
            'user': user
        }
    )

@admin_only
def dashboard(request):

    user = request.user

    product_count = Product.objects.count()
    category_count = Category.objects.count()
    supplier_count = Supplier.objects.count()
    user_count = User.objects.count()

    context = {
        'user': user,
        'product_count': product_count,
        'category_count': category_count,
        'supplier_count': supplier_count,
        'user_count': user_count,
    }

    return render(
        request,
        'dashboard.html',
        context
    )
@admin_only
def create_category(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('category_list')

    else:
        form = CategoryForm()

    return render(request, 'create_category.html', {'form': form})

@admin_only
def category_list(request):

    categories = Category.objects.all()

    return render(request, 'category_list.html', {
        'categories': categories
    }) 
@admin_only
def user_list(request):

    users = User.objects.all()

    return render(
        request,
        'user_list.html',
        {
            'users': users
        }
    )
def profile(request):

    if not request.user.is_authenticated:
        return redirect('login')

    return render(
        request,
        'profile.html',
        {
            'user': request.user
        }
    )
def cart_view(request):

    if not request.user.is_authenticated:
        return redirect("login")

    cart = Cart.objects.filter(user=request.user).first()

    cart_items = []
    total_price = 0

    if cart:
        cart_items = cart.items.select_related("product").all()

        for item in cart_items:
            # ราคารวมของสินค้ารายการนั้น
            item.total_price = item.product.sell_price * item.quantity

        # ราคารวมทั้งหมด
        total_price = sum(item.total_price for item in cart_items)

    return render(
        request,
        "cart.html",
        {
            "cart": cart,
            "cart_items": cart_items,
            "total_price": total_price,
        },
    )


def add_to_cart(request, product_id):

    if not request.user.is_authenticated:
        return redirect("login")

    user = request.user
    product = Product.objects.get(id=product_id)

    cart, created = Cart.objects.get_or_create(
        user=user
    )

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        item.quantity += 1
        item.save()

    messages.success(request, "เพิ่มลงตะกร้าแล้ว")
    return redirect("cart")


def remove_from_cart(request, item_id):

    if not request.user.is_authenticated:
        return redirect("login")

    item = CartItem.objects.filter(id=item_id, cart__user=request.user).first()

    if item:
        item.delete()
        messages.success(request, "ลบสินค้าออกจากตะกร้าแล้ว")

    return redirect("cart")

def increase_quantity(request, item_id):

    item = get_object_or_404(CartItem, id=item_id)

    item.quantity += 1
    item.save()

    return redirect("cart")


def decrease_quantity(request, item_id):

    item = get_object_or_404(CartItem, id=item_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect("cart")

def checkout(request):

    if "user_id" not in request.session:
        return redirect("login")

    user = User.objects.get(id=request.session["user_id"])

    cart = Cart.objects.filter(user=user).first()

    if not cart:
        messages.error(request, "ไม่มีสินค้าในตะกร้า")
        return redirect("cart")

    items = cart.items.all()

    if not items:
        messages.error(request, "ไม่มีสินค้าในตะกร้า")
        return redirect("cart")

    total = 0

    order = Order.objects.create(
        user=user,
        total_price=0
    )

    for item in items:
    # ตรวจสอบว่าสินค้าเพียงพอหรือไม่
      if item.quantity > item.product.stock_qty:

        messages.error(
            request,
            f"สินค้า {item.product.product_name} มีเหลือเพียง {item.product.stock_qty} ชิ้น"
        )
        # ลบ Order ที่เพิ่งสร้าง เพราะ Checkout ไม่สำเร็จ
        order.delete()

        return redirect("cart")

    subtotal = item.product.sell_price * item.quantity

    OrderItem.objects.create(
        order=order,
        product=item.product,
        quantity=item.quantity,
        price=item.product.sell_price,
        subtotal=subtotal
    )
    # ตัด Stock
    item.product.stock_qty = max(
        0,
        item.product.stock_qty - item.quantity
    )

    item.product.save()

    total += subtotal

    order.total_price = total
    order.save()

    # ล้างตะกร้า
    items.delete()

    messages.success(request, "ชำระเงินสำเร็จ")

    return redirect("home")

def products(request):

    products = Product.objects.filter(
        is_active=True
    )

    categories = Category.objects.filter(
        categ_status="active"
    )

    context = {
        "products": products,
        "categories": categories,
    }

    return render(
        request,
        "products.html",
        context
    )
def category_products(request, id):

    category = Category.objects.get(id=id)

    products = Product.objects.filter(
        category=category,
        is_active=True
    )

    context = {
        "category": category,
        "products": products,
    }

    return render(
        request,
        "category_products.html",
        context
    )