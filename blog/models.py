from django.db import models
from utils.rands import slugfy_new
from django.contrib.auth.models import User

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default=None,
        null=True, blank=True, max_length=255,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugfy_new(self.slug, 6)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default=None,
        null=True, blank=True, max_length=255,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugfy_new(self.slug, 6)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class Page(models.Model):
    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    title = models.CharField(max_length=65,)
    slug = models.SlugField(
        unique=True, default=None,
        null=True, blank=True, max_length=255,
    )
    is_published = models.BooleanField(
        default=False,
        help_text='Necessário marcar para exibir publicamente.'
    )
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugfy_new(self.title, 6)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    

class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    title = models.CharField(max_length=65,)
    slug = models.SlugField(
        unique=True, default=None,
        null=True, blank=True, max_length=255,
    )
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(
        default=False,
        help_text='Necessário marcar para exibir publicamente.'
    )
    content = models.TextField()
    cover = models.ImageField(
        upload_to='posts/%Y/%m',
        blank=True, default=''
    )
    cover_in_post_content = models.BooleanField(
        default=True,
        help_text='Exibe a imagem de caapa também dentro do conteúdo do post.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    # quando fizer a consulta/relação inversa do USER para buscar os POSTS
    # fiaria assim : User.post_set.all() - igual seria no updated_by
    # e o Django retornaria um erro (conflito)
    # por isso a propriedade related_name
    # com related_name ficaria assim: User.post_created_by.all
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='post_created_by'
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    # quando fizer a consulta/relação inversa do USER para buscar os POSTS
    # fiaria assim : User.post_set.all() - igual seria no created_by
    # e o Django retornaria um erro (conflito)
    # por isso a propriedade related_name
    # com related_name ficaria assim: User.post_updated_by.all
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='post_updated_by'
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None
    )
    tags = models.ManyToManyField(Tag, blank=True, default=None)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugfy_new(self.title, 6)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title