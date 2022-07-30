from django.db import models
from django.contrib.auth.models import User


class Channel(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(null=True, blank=True, upload_to='channel')

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    # class Meta:
    #     verbose_name = 'My image'
    #     verbose_name_plural = 'My images'

    @property
    def get_number_of_orders(self):
        number_of_orders = self.order.count()
        return number_of_orders

    @property
    def get_total_sales(self):
        total = sum([order.total or 0 for order in self.order.all()])  # we have a problem here
        return total

        # @property
    # def get_number_of_brands(self):
    #     number_of_brands = self.order.brand_branch.all().count()
    #     return number_of_brands


class kitchefy_user(models.Model):
    postion = models.CharField(max_length=40)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Fp(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    image = models.ImageField(null=True, blank=True, upload_to='FP')

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Fp__'


class Fp_branch(models.Model):
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    bilding_no = models.CharField(max_length=20)
    active = models.BooleanField()
    fp = models.ForeignKey(Fp, on_delete=models.CASCADE)
    multiplayer_forecast = models.DecimalField(max_digits=5, decimal_places=3)
    sales_tax = models.DecimalField(max_digits=5, decimal_places=3)
    revenue_percentage = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    def __str__(self):
        return self.fp.name + " " + self.area

    @property
    def get_total_tax(self):
        total_tax = self.get_total_sales * self.sales_tax
        return total_tax

    @property
    def get_number_of_orders(self):
        total = 0
        for brand in self.brand_branch.all():
            total += brand.get_number_of_orders
        return total

    @property
    def get_total_sales(self):
        total = 0
        for brand in self.brand_branch.all():
            total += brand.get_total_sales
        return total

    @property
    def get_total_fp_revenue(self):
        return (self.get_total_sales - self.get_total_tax) * self.revenue_percentage


class Brand(models.Model):
    name = models.CharField(max_length=50)
    fp_percentage = models.DecimalField(max_digits=4, decimal_places=2)
    partner_percentage = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    username = models.EmailField()
    password = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to='Brand')
    talabat_commission = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    careem_commission = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    cs_mena_subscription = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    ask_paper_subscription = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name

    @property
    def get_brand_partner_cost(self):
        return (self.get_total_sales - self.get_total_tax) * self.partner_percentage

    @property
    def get_total_tax(self):
        total = 0
        for brand in self.branch.all():
            total += brand.get_total_tax
        return total

    @property
    def get_number_of_orders(self):
        total = 0
        for brand in self.branch.all():
            total += brand.get_number_of_orders
        return total

    @property
    def get_total_sales(self):
        total = 0
        for brand in self.branch.all():
            total += brand.get_total_sales
        return total

    @property
    def get_talabat_total_sales(self):
        total = 0
        for brand in self.branch.all():
            total += brand.get_talabat_total_sales
        return total

    @property
    def get_careem_total_sales(self):
        total = 0
        for brand in self.branch.all():
            total += brand.get_careem_total_sales
        return total

    @property
    def get_talabat_commission(self):
        return self.get_talabat_total_sales * self.talabat_commission / 100

    @property
    def get_careem_commission(self):
        return self.get_careem_total_sales * self.careem_commission / 100


class Brand_branch(models.Model):
    Fp_branch = models.ForeignKey(Fp_branch, on_delete=models.CASCADE, null=True, related_name="brand_branch")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="branch")
    active = models.BooleanField()
    talabat_name = models.CharField(max_length=100)
    carem_id = models.IntegerField()
    csmena_name = models.CharField(max_length=50)
    askpaper_name = models.CharField(max_length=50)
    multiplayer_forecast = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self):
        return self.brand.name + " " + self.Fp_branch.fp.name

    @property
    def get_total_tax(self):
        total_tax = self.get_total_sales * self.Fp_branch.sales_tax
        return total_tax

    @property
    def get_number_of_orders(self):
        number_of_orders = self.order.count()
        return number_of_orders

    @property
    def get_total_sales(self):
        total = sum([order.total for order in self.order.all()])
        return total

    @property
    def get_talabat_total_sales(self):
        total = sum([order.total for order in self.order.filter(channel__name="Talabat")])
        return total

    @property
    def get_careem_total_sales(self):
        total = sum([order.total for order in self.order.filter(channel__name="Careem")])
        return total


class Status(models.Model):
    Brand_branch = models.ForeignKey(Brand_branch, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)
    datetime = models.DateTimeField(auto_now=True, null=True, blank=True)
    status = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.Brand.name + " " + self.channel.name


class Days(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Opening_hours(models.Model):
    start = models.TimeField()
    end = models.TimeField()
    day = models.ManyToManyField(Days)
    brand_branch = models.ForeignKey(Brand_branch, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.brand_branch.fp.name + "_" + self.brand_branch.brand.name


class Offers(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)
    status = models.BooleanField()
    brand_branch = models.ForeignKey(Brand_branch, on_delete=models.CASCADE, null=True)
    soft_delete = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Announcement_center(models.Model):
    date_time = models.DateTimeField(null=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand_branch = models.ForeignKey(Brand_branch, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.description


class Knowleddge_center_section(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Knowledge_center(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    # image =
    video_link = models.URLField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    knowledge_center_section = models.ForeignKey(Knowleddge_center_section, on_delete=models.CASCADE)
    fp = models.ForeignKey(Fp, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Type_rating(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self):
        return self.name


class Liability(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Incident_report(models.Model):
    type_rating = models.ForeignKey(Type_rating, on_delete=models.CASCADE)
    date_time = models.DateTimeField(null=True)
    brand_branch = models.ForeignKey(Brand_branch, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)
    case_date_time = models.DateTimeField(null=True)
    # incedent_level = #
    liability = models.ForeignKey(Liability, on_delete=models.CASCADE)
    message = models.CharField(max_length=100, null=True, blank=True)
    pdf_link = models.URLField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.brand_branch.fp.name + "_" + self.brand_branch.brand.name + "_" + self.date_time


class Order(models.Model):
    ########order_Item = models.ForeignKey('Order_Item', on_delete=models.CASCADE, blank=True, null=True)
    brand_branch = models.ForeignKey(Brand_branch, on_delete=models.CASCADE, blank=True, null=True,
                                     related_name="order")
    order_id = models.IntegerField(null=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    date_time = models.DateField(null=True)
    type = models.CharField(max_length=50, null=True)
    total = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    delivery_zone = models.CharField(max_length=50, null=True)
    details = models.CharField(max_length=500, null=True)
    customer_name = models.CharField(max_length=50, null=True)
    customer_mobile_number = models.CharField(max_length=50, null=True)
    payment_fees = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True, related_name="order")
    delivary_fee = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    payment_method = models.CharField(max_length=50, null=True)

    # add field al from finnance report
    def __str__(self):
        return str(self.brand_branch)

    @property
    def order_items(self):
        queryset = self.order_item_set.all().values_list('quantity', flat=True)
        return queryset


class Item(models.Model):
    name = models.CharField(max_length=500)
    cost = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def get_item_cost(self):
        total = sum([item.quantity for item in self.order_item_set.all()])
        return total * self.cost


class Order_Item(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,related_name="order_item")
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, related_name='order_item', on_delete=models.CASCADE)
    price =  models.DecimalField(max_digits=5, decimal_places=3, null=True)
    def __str__(self):
        return str(self.order.id)




class Add_ons(models.Model):
    name = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    def __str__(self):
        return self.name


class Order_item_add_ons(models.Model):
    order_item = models.ForeignKey(Order_Item, related_name='order_item_add_ons', on_delete=models.CASCADE, null=True, blank=True)
    Add_ons = models.ForeignKey(Add_ons, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    # def __str__(self):
    #     return self.Add_ons.name



