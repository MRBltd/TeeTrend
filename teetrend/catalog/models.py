from django.db import models

class Tshirt(models.Model):
  MEN_TSHIRTS = 'MT'
  WOMEN_TSHIRTS = 'WT'
  KIDS_TSHIRTS = 'KT'
  CHARACTERS = 'CT'

  CATEGORY_CHOICES = [
    (MEN_TSHIRTS, 'Men T-Shirts'),
    (WOMEN_TSHIRTS, 'Women T-Shirts'),
    (KIDS_TSHIRTS, 'Kids T-Shirts'),
    (CHARACTERS , 'Characters'),
  ]

  category = models.CharField(
    max_length=2,
    choices=CATEGORY_CHOICES,
    blank = True ,
  )

  SUBCATEGORIES = [
    ('PN', 'Polo Neck'),
    ('HS', 'Half Sleeves'),
    ('HLN', 'Henley Neck'),
    ('HD', 'Hoodies'),
    ('SL', 'Sleeveless'),
    ('SW', 'Sweatshirts'),
    ('LS', 'Long Sleeves'),
    ('PT', 'Printed T-Shirts'),
    ('CBT', 'Colorblock T-Shirts'),
    ('VN', 'V-Neck'),
    ('WN', 'Wide Neck Off Shoulder T-shirts'),
    ('YN', 'Yoke Neck T-shirts'),
    ('DB', 'Douche Bag Neck T-shirt'),
    ('CS', 'Cold Shoulder'),
    ('OS' , 'Off Shoulder'),
    ('HN', 'High Neck'),
    ('WT', 'White T-Shirts'),
    ('BT', 'Boyfriend tees'),
    ('ST', 'Striped T-Shirts'),
    ('KC', 'Knot Crop'),
    ('SN', 'Scoop Neck'),
    ('CN', 'Crew Neck'),
  ]

  subcategory = models.CharField(
    max_length=3,
    choices=SUBCATEGORIES,  # Change this based on the category
    blank = True ,
  )

  MARVEL = 'MR'
  DC_COMICS = 'DC'
  MOVIES_TV = 'MS'
  CARTOONS_ANIME = 'CA'
  WEB_SERIES = 'WS'

  CHARACTERS_SUBCATEGORIES = [
    (MARVEL, 'Marvel'),
    (DC_COMICS, 'DC Comics'),
    (MOVIES_TV, 'Movies & TV'),
    (CARTOONS_ANIME, 'Cartoons/Anime'),
    (WEB_SERIES, 'Web Series'),
  ]

  characters = models.CharField(
    max_length=2,
    choices=CHARACTERS_SUBCATEGORIES,
    blank=True,
  )

  # Subcategories for Marvel
  MARVEL_SUBCATEGORIES = [
    ('AVM' , 'Avengers') ,
    ('SMM' , 'Spider-Man') ,
    ('IMM' , 'Iron-Man') ,
    ('CAM' , 'Captain America') ,
    ('TM' , 'Thor') ,
    ('LM' , 'Loki') ,
    ('DSM' , 'Doctor Strange') ,
    ('DPM' , 'Dead Pool') ,
    ('HM' , 'Hulk') ,
    ('BWM' , 'Black Widow') ,
    ('VM' , 'Venom') ,
    ('WVM' , 'Wandavision') ,
    ('AMM' , 'Ant-Man') ,
    ('CMM' , 'Captain Marvel') ,
    ('SCM' , 'Shang Chi') ,
    ('TNM' , 'Thanos') ,
    ('BPM' , 'Black Panther') ,
    ('EM' , 'Eternals') ,
  ]

  marvel_subcategory = models.CharField(
    max_length=3,
    choices=MARVEL_SUBCATEGORIES,
    blank=True,
  )

  # Subcategories for Dc Comics
  DC_COMICS_SUBCATEGORIES = [
    ('BBD' , 'Blue Bleete') ,
    ('JLD' , 'Justice League') ,
    ('BMD' , 'Batman') ,
    ('TFD' , 'The Fish') ,
    ('SMD' , 'Super Man') ,
    ('WWD' , 'Wonder Woman') ,
    ('SD' , 'Shazam') ,
    ('JD' , 'Joker') ,
    ('AMD' , 'Aquaman') ,
    ('GLD' , 'Green Lantern') ,
    ('HQD' , 'Harley Quinn') ,
    ('BAD' , 'Black Adam') ,
    ('SSD' , 'Suide Sqaud') ,
  ]

  dc_comics_subcategory = models.CharField(
    max_length=3,
    choices=DC_COMICS_SUBCATEGORIES,
    blank=True,
  )

  # Subcategories for MOVIES&TV
  MOVIES_TV_SUBCATEGORIES = [
    ('HPM' , 'Harry Potter') ,
    ('FM' , 'Friends') ,
    ('SWM' , 'Star Wars') ,
    ('TMM' , 'The Mandalorian') ,
    ('HDM' , 'House of the Dragon') ,
    ('GTM' , 'Game of Thrones') ,
    ('LKM' , 'The Lion King') ,
  ]

  movies_tv_subcategory = models.CharField(
    max_length=3,
    choices=MOVIES_TV_SUBCATEGORIES,
    blank=True,
  )

  # Subcategories for Marvel
  CARTOONS_ANIME_SUBCATEGORIES = [
    ('SNC' , 'Snoopy') ,
    ('RMC' , 'Rick and Morty') ,
    ('LTC' , 'Looney Tunes') ,
    ('BBC' , 'Bugs Bunny') ,
    ('TC' , 'Tweety') ,
    ('SJC' , 'Space Jam') ,
    ('TJC' , 'Tom and Jerry') ,
    ('SDC' , 'Scooby Doo') ,
    ('DC' , 'Disney') ,
    ('MMC' , 'Mickey Mouse') ,
    ('DDC' , 'Donald Duck') ,
    ('SJ' , 'Samurai Jack') ,
    ('BC' , 'Ben 10') ,
    ('SBC' , 'Sponge Bob Square Pants') ,
    ('FDC' , 'Fidon Dido') ,
    ('CBC' , 'Chotta Beam') ,
    ('MPC' , 'Motu Patlu') ,
    ('MC' , 'Mowgli') ,
    ('DMC' , 'Doremon') ,
    ('JAC' , 'Jackiechan Adventure.') ,
    ('LKC' , 'Little krishna') ,
    ('SC' , 'Shiva') ,
    ('DEC' , 'Dora the Explorer') ,
  ]

  cartoons_anime_subcategory = models.CharField(
    max_length=3,
    choices=CARTOONS_ANIME_SUBCATEGORIES,
    blank=True,
  )

  # Subcategories for Marvel
  WEB_SERIES_SUBCATEGORIES = [
    ('STW' , 'Stranger Things') ,
    ('WW' , 'Wednesday') ,
    ('NHW' , 'Never Have I Ever') ,
    ('EW' , 'Elite') ,
    ('PBW' , 'Peaky Blinders') ,
    ('LW' , 'Lucifer') ,
    ('ADW' , 'All of us Are Dead') ,
    ('SEW' , 'Sex Education') ,
  ]

  web_series_subcategory = models.CharField(
    max_length=3,
    choices=WEB_SERIES_SUBCATEGORIES,
    blank=True,
  )

  title = models.CharField(max_length=200)
  name = models.CharField(max_length=500)
  retail_price = models.DecimalField(max_digits=10 , decimal_places=2)
  price = models.DecimalField(max_digits=5, decimal_places=2)
  image = models.ImageField(upload_to='products/')
  image1 = models.ImageField(upload_to='products/' , null=True, blank=True) # To store product 2nd image
  image2 = models.ImageField(upload_to='products/' , null=True, blank=True) # To store product 3rd image
  image3 = models.ImageField(upload_to='products/' , null=True, blank=True) # To store product 4th image
  image4 = models.ImageField(upload_to='products/' , null=True, blank=True) # To store product 5th image
  image5 = models.ImageField(upload_to='products/' , null=True, blank=True) # To store product 6th image
  image6 = models.ImageField(upload_to='products/' , null=True, blank=True) # To store product 7th image
  image7 = models.ImageField(upload_to='products/' , null=True, blank=True) # To store product 8th image
  AGE_CHOICES = [
    ('6-18m', '6-18m'),
    ('18-24m', '18-24m'),
    ('2-4y', '2-4y'),
    ('4-6y', '4-6y'),
    ('6-8y', '6-8y'),
    ('8-9y', '8-9y'),
    ('9-10y', '9-10y'),
    ('10-11y', '10-11y'),
    ('11-12y', '11-12y'),
    ('12-13y', '12-13y'),
    ('13-14y', '13-14y'),
    ('14-15y', '14-15y'),
    ('2-3y', '2-3y'),
    ('3-4y', '3-4y'),
    ('4-5y', '4-5y'),
    ('5-6y', '5-6y'),
    ('6-7y', '6-7y'),
    ('7-8y', '7-8y'),
    ('8-10y', '8-10y'),
    ('10-12y', '10-12y'),
    ('12-14y', '12-14y'),
    ('14-16y', '14-16y'),
  ]
  age = models.CharField(max_length=6, choices=AGE_CHOICES , blank=True)
  # Size field
  SIZE_CHOICES = [
    ('S', 'Small') ,
    ('M', 'Medium') ,
    ('L', 'Large') ,
    ('XL' , 'Extra Large') ,
    ('2XL' , '2X-Large') ,
    ('3XL' , '3X-Large') ,
    ('4XL' , '4X-Large') ,
  ]
  size = models.CharField(max_length=3 , choices=SIZE_CHOICES , blank=True)
  color = models.CharField(max_length=50)
  MATERIAL_CHOICES = [
    ('C', 'Cotton'),
    ('P', 'Polyester'),
    ('L', 'Linen'),
    ('R', 'Rayon'),
    ('S', 'Spandex'),
  ]
  material = models.CharField(max_length=1, choices=MATERIAL_CHOICES)  # Material of the T-shirt
  brand = models.CharField(max_length=50)  # Brand of the T-shirt
  stock = models.IntegerField()  # To track the stock of the product
  discount = models.CharField(max_length=5, null=True, blank=True)  # Optional field for discounts

  def __str__(self):
    return self.get_category_display()

  @staticmethod
  def get_full_name(choices, code):
    for choice_code, full_name in choices:
      if choice_code == code:
        return full_name
    return None  

  def get_subcategories(self):
    if self.characters == self.MARVEL:
        return self.MARVEL_SUBCATEGORIES
    elif self.characters == self.DC_COMICS:
        return self.DC_COMICS_SUBCATEGORIES
    elif self.characters == self.MOVIES_TV:
        return self.MOVIES_TV_SUBCATEGORIES
    elif self.characters == self.CARTOONS_ANIME:
        return self.CARTOONS_ANIME_SUBCATEGORIES
    elif self.characters == self.WEB_SERIES:
        return self.WEB_SERIES_SUBCATEGORIES
    else:
        return self.SUBCATEGORIES