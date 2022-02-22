from ckeditor.fields import RichTextField

from django.db import models


class Category(models.Model):
    name = models.CharField("Category Name", max_length=100, blank=False, null=False)
    status = models.BooleanField("Category status", default=True)
    creation_date = models.DateField("Creation Date", auto_now=False, auto_now_add=True)

    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]

    
    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    firstname = models.CharField("Firstname", max_length=255, blank=False, null=False)
    lastname = models.CharField("Lastname", max_length=255, blank=False, null=False)
    email = models.EmailField("Email", blank=False, null=False, unique=True)
    status = models.BooleanField("Author status", default=True)
    creation_date = models.DateField("Creation Date", auto_now=False, auto_now_add=True)
    facebook = models.URLField("Facebook author", null=True, blank=True)
    twitter = models.URLField("Twitter author", null=True, blank=True)
    instagram = models.URLField("Instagram author", null=True, blank=True)
    website = models.URLField("Website author", null=True, blank=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    
    def __str__(self) -> str:
        return f'{self.lastname}, {self.firstname}'


class Post(models.Model):
    title = models.CharField("Title post", max_length=100, blank=False, null=False)
    slug = models.CharField("Slug", max_length=50,blank=False, null=False)
    description = models.CharField("Description", max_length=110, blank=False, null=False)
    content = RichTextField() 
    image = models.URLField("Image url", blank=False, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.BooleanField("Status Post", default=True)
    creation_date = models.DateField("Creation Date", auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


    def __str__(self) -> str:
        return self.title