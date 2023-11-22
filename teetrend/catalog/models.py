from django.db import models



class Category(models.Model):
  MEN_TSHIRTS = 'MT'
  WOMEN_TSHIRTS = 'WT'
  KIDS_TSHIRTS = 'KT'
  CHARACTERS = 'CH'

  CATEGORY_CHOICES = [
    (MEN_TSHIRTS, 'Men T-Shirts'),
    (WOMEN_TSHIRTS, 'Women T-Shirts'),
    (KIDS_TSHIRTS, 'Kids T-Shirts'),
    (CHARACTERS, 'Characters'),
  ]

  categories = models.CharField(
    max_length=2,
    choices=CATEGORY_CHOICES,
    default=MEN_TSHIRTS,
  )

  def __str__(self):
    return self.get_categories_display()


class Tshirt(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField()
  price = models.DecimalField(max_digits=5, decimal_places=2)
  image = models.ImageField(upload_to='products/')  # To store product first image
  image1 = models.ImageField(upload_to='products/' , null=True, blank=True) # To store product 2nd image
  image2 = models.ImageField(upload_to='products/' , null=True, blank=True) # To store product 3rd image
  image3 = models.ImageField(upload_to='products/' , null=True, blank=True) # To store product 4th image
  image4 = models.ImageField(upload_to='products/' , null=True, blank=True) # To store product 5th image
  image5 = models.ImageField(upload_to='products/' , null=True, blank=True) # To store product 6th image
  image6 = models.ImageField(upload_to='products/' , null=True, blank=True) # To store product 7th image
  image7 = models.ImageField(upload_to='products/' , null=True, blank=True) # To store product 8th image
  category = models.ForeignKey(Category, on_delete=models.CASCADE)  # To categorize the product
  size = models.CharField(max_length=2)
  color = models.CharField(max_length=50)
  material = models.CharField(max_length=50)  # Material of the T-shirt
  brand = models.CharField(max_length=50)  # Brand of the T-shirt
  stock = models.IntegerField()  # To track the stock of the product
  discount = models.CharField(max_length=5, null=True, blank=True)  # Optional field for discounts
