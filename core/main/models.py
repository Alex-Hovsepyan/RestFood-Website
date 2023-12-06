from django.db import models

# Create your models here.

class Header(models.Model):

    doc_title = models.CharField('Document Title', max_length=60)
    logo = models.ImageField('Logo')
    path1 = models.CharField('Path 1', max_length=40)
    path2 = models.CharField('Path 2', max_length=40)
    path3 = models.CharField('Path 3', max_length=40)
    path4 = models.CharField('Path 4', max_length=40)
    path5 = models.CharField('Path 5', max_length=40)
    path6 = models.CharField('Path 6', max_length=40)
    background = models.ImageField('Background')

    class Meta:

        verbose_name = 'Header'
        verbose_name_plural = 'Header'

class Home(models.Model):

    background = models.ImageField('Background')
    title = models.CharField('Title', max_length=50)
    text = models.TextField('Text')
    button = models.CharField('Button', max_length=30)

    class Meta:

        verbose_name = 'Home'
        verbose_name_plural = 'Home'

class Title(models.Model):

    img = models.ImageField('Image')
    title1 = models.CharField('Title 1', max_length=50)
    text1 = models.TextField('Text 1', blank=True)
    title2 = models.CharField('Title 2', max_length=50)
    text2 = models.TextField('Text 2', blank=True)
    title3 = models.CharField('Title 3', max_length=50)
    text3 = models.TextField('Text 3', blank=True)
    title4 = models.CharField('Title 4', max_length=50)
    text4 = models.TextField('Text 4', blank=True)
    title5 = models.CharField('Title 5', max_length=50)
    text5 = models.TextField('Text 5', blank=True)
    title6 = models.CharField('Title 6', max_length=50)
    text6 = models.TextField('Text 6', blank=True)
    title7 = models.CharField('Title 7', max_length=50)
    text7 = models.TextField('Text 7', blank=True)

class About(models.Model):

    img = models.ImageField('Image')
    video_url = models.URLField('Video Url')
    
    class Meta:

        verbose_name = 'About'
        verbose_name_plural = 'About'

class AboutContent(models.Model):

    text = models.TextField('Text')
    img = models.ImageField('Image')
    title = models.CharField('Title', max_length=50)

    class Meta:

        verbose_name = 'About Content'
        verbose_name_plural = 'About Content'

    def __str__(self) -> str:
        return self.title
    
class Offer(models.Model):

    background = models.ImageField('Background')
    title = models.CharField('Title', max_length=50)
    button = models.CharField('Button', max_length=30)
    
    class Meta:

        verbose_name = 'Offer'
        verbose_name_plural = 'Offer'

class Chef(models.Model):

    img = models.ImageField('Image')
    name = models.CharField('Name', max_length=50)
    position = models.CharField('Position', max_length=50)
    social1 = models.URLField('Social 1')
    social2 = models.URLField('Social 2')
    social3 = models.URLField('Social 3')

    def __str__(self) -> str:
        return f'{self.name} - {self.position}'

class Gallery(models.Model):

    img = models.ImageField('Image')

    class Meta:

        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'

class ReservationContent(models.Model):

    button = models.CharField('Button', max_length=30)
    title = models.CharField('Title', max_length=50)
    text = models.TextField('Text')

    class Meta:

        verbose_name = 'Reservation Content'
        verbose_name_plural = 'Reservation Content'

class OpenDays(models.Model):

    day = models.CharField('Title', max_length=40)
    time = models.CharField('Time', max_length=25)

    class Meta:

        verbose_name = 'Open Days'
        verbose_name_plural = 'Open Days'

    def __str__(self) -> str:
        return f'{self.day} - {self.time}'

class Reservation(models.Model):

    res_name = models.CharField('Username', max_length=50)
    res_lastname = models.CharField('Surname', max_length=60)
    res_phone = models.CharField('Phone Number', max_length=25)
    res_email = models.EmailField('User Email')
    res_date = models.CharField('Date', max_length=10)
    res_time = models.CharField('Time', max_length=5)

    def __str__(self) -> str:
        return f'{self.res_name} {self.res_lastname} - {self.res_phone}'

class ContactContent(models.Model):

    icon = models.CharField('Icon', max_length=50)
    title = models.CharField('Title', max_length=40)
    info = models.CharField('Info', max_length=80)
    
    class Meta:

        verbose_name = 'Contact Content'
        verbose_name_plural = 'Contact Content'

    def __str__(self) -> str:
        return f'{self.title} - {self.info}'
    
class ContactInfo(models.Model):

    social1 = models.URLField('Social 1')
    social2 = models.URLField('Social 2')
    social3 = models.URLField('Social 3')
    social4 = models.URLField('Social 4')
    google_map = models.TextField('Google Map')

    class Meta:

        verbose_name = 'Contact Info'
        verbose_name_plural = 'Contact Info'

class Menu(models.Model):

    title = models.CharField('Title', max_length=50)

    class Meta:

        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

    def __str__(self) -> str:
        return self.title
    
class Product(models.Model):

    category = models.ForeignKey(Menu, on_delete=models.CASCADE)
    img = models.ImageField('Image')
    name = models.CharField('Name', max_length=60)
    text = models.TextField('Info')
    price = models.FloatField('Price')
    special = models.BooleanField('Special yes/no', blank=True)

    def __str__(self) -> str:
        return f'{self.category} - {self.name} {self.price}'