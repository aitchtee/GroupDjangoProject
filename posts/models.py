from django.db import models
from datetime import datetime

# Create your models here.


class Meta:
    db_table = 'posts'

    
class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое', default='')
    timestamp = models.DateTimeField(verbose_name='Дата добавления', default=datetime.now())
    updated = models.DateTimeField(verbose_name='Дата обновления', default=datetime.now())
    id = models.AutoField(primary_key=True)
    post_likes = models.IntegerField(default=0, verbose_name='Понравилось')
    genre = (('r1', 'Роман'),
             ('p', 'Поэма'),
             ('r2', 'Рассказ'))
    genre = models.CharField(max_length=50, verbose_name='Жанр', choices=genre, default='r1')
    post_author = models.ForeignKey('Author', null=True, blank=True, verbose_name='автор поста')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    second_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(default='')

    def __unicode__(self):
        return self.second_name + ' ' + self.first_name

    def __str__(self):
        return self.second_name + ' ' + self.first_name


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    comment_text = models.TextField(verbose_name='Комментарий', default='')
    comment_article = models.ForeignKey(Post)

    def __unicode__(self):
        return self.comment_text[:10] + '... ' + str(self.comment_article)

    def __str__(self):
        return self.comment_text[:10] + '... ' + str(self.comment_article)
