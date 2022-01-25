from django.db import models

# Create your models here.


class Books(models.Model):
    Description = models.TextField('Описание книги')
    Year = models.PositiveIntegerField('Год написания')
    PopularityRating = models.PositiveIntegerField('Место в рейтинге')
    BookTitle = models.TextField('Название книги')
    Author = models.TextField('Автор')
    Genre = models.TextField('Жанр')
    FirstPoblicationYear = models.PositiveIntegerField('Год первой публикации')
    Publisher = models.TextField('Издательство, опубликовавшее книгу')
    OriginalLanguage = models.TextField('Оригинальный язык')
    Country = models.TextField('Страна в которой написана книга')

    def __str__(self):
        return self.BookTitle

    def get_absolute_url(self):
        return f"/detail/{self.id}/"

    class Meta:
        ordering = ['PopularityRating']
