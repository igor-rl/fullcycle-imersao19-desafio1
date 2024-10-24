from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100, unique=True, verbose_name='Título')
  content = models.TextField(verbose_name='Conteúdo')
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação', editable=False)
  tags = models.ManyToManyField('Tag', related_name='posts', blank=True, verbose_name='Tags')

  class Meta:
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'
  
  def __str__(self):
    return self.title

class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True, verbose_name='Nome')

  class Meta:
    verbose_name = 'Tag'
    verbose_name_plural = 'Tags'

  def __str__(self):
    return self.name