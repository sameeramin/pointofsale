from django.db import models


class UOM(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Pack(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    TYPE = (
        ('raw', 'Raw Item'),
        ('finished', 'Finished Item'),
    )
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    uom = models.ForeignKey(UOM, on_delete=models.RESTRICT)
    pack = models.ForeignKey(Pack, on_delete=models.RESTRICT)
    p_price = models.DecimalField(max_digits=20, decimal_places=2)
    s_price = models.DecimalField(max_digits=20, decimal_places=2)
    type = models.CharField(max_length=20, choices=TYPE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)
    status = models.BooleanField(default=True)
    created_by = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=20, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)
    status = models.BooleanField(default=True)
    created_by = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=20, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SaleMST(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    date = models.DateField()
    desc = models.CharField(max_length=200, blank=True, null=True)
    disc = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    created_by = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=20, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer.name

    # This retrive details of voucher
    # def get_sale(self):
    #     return self.saledtl_set.all()


class SaleDTL(models.Model):
    mst = models.ForeignKey(SaleMST, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    desc = models.CharField(max_length=200, blank=True, null=True)
    rate = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    disc = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    qty = models.IntegerField()

    def __str__(self):
        return self.product.name


class PurchaseMST(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    date = models.DateField()
    desc = models.CharField(max_length=200, blank=True, null=True)
    disc = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    created_by = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=20, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer.name

    # This retrive details of voucher
    # def get_sale(self):
    #     return self.saledtl_set.all()


class PurchaseDTL(models.Model):
    mst = models.ForeignKey(SaleMST, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    desc = models.CharField(max_length=200, blank=True, null=True)
    rate = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    disc = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    qty = models.IntegerField()

    def __str__(self):
        return self.product.name
