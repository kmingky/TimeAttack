from django.db import models
from user.models import User


# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "CATEGORY"

    def __str__(self):
        return self.category

    category = models.CharField(max_length=256, null=False, verbose_name="상품구분")


class OrderStatus(models.Model):
    class Meta:
        db_table = "ORDERSTATUS"

    def __str__(self):
        return self.orderstatus

    orderstatus = models.CharField(max_length=256, null=False, verbose_name="주문상태")


class ProductOrder(models.Model):
    class Meta:
        db_table = "PRODUCTORDER"

    def __str__(self):
        return self.productorder

    productorder = models.IntegerField(verbose_name="주문수량")


class Product(models.Model):
    class Meta:
        db_table = "PRODUCT"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=256, null=False, verbose_name="상품명")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="상품구분"
    )
    image = models.ImageField(upload_to="product_img", verbose_name="상품사진")
    description = models.TextField(verbose_name="상품설명")
    price = models.IntegerField(verbose_name="상품가격")
    stock = models.IntegerField(verbose_name="재고")
    productorder = models.ForeignKey(
        ProductOrder, on_delete=models.CASCADE, verbose_name="주문수량"
    )


class UserOrder(models.Model):
    class Meta:
        db_table = "USERORDER"

    def __str__(self):
        return self.username

    username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="주문자")
    productorder = models.ForeignKey(
        ProductOrder, on_delete=models.CASCADE, verbose_name="주문수량"
    )
    address = models.CharField(max_length=256, null=False, verbose_name="배송주소")
    order_date = models.DateTimeField(
        auto_now=True, auto_now_add=False, verbose_name="주문시간"
    )
    all_price = models.IntegerField(verbose_name="전체상품가격")
    sale = models.IntegerField(verbose_name="할인율")
    price_result = models.IntegerField(verbose_name="최종가격")
    bool = models.BooleanField(verbose_name="유효여부")
    orderstatus = models.ForeignKey(
        OrderStatus, on_delete=models.CASCADE, verbose_name="주문상태"
    )
