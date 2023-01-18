from django.db import models

from django.contrib.auth.models import User
from users.models import UserProfile

# Create your models here.

class Board(models.Model):
    '''Доска задач'''
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='owned_boards')
    name_board = models.CharField(max_length=100)
    date_create = models.DateTimeField(auto_now_add=True, editable=False)
    members = models.ManyToManyField(User, related_name='boards', blank=True)

    class Meta:
        verbose_name = 'Доска'
        verbose_name_plural = 'Доски'
        ordering = ['-date_create']

    def __str__(self):
        return self.name


class Column(models.Model):
    '''Колонка доски'''
    board = models.ForeignKey(Board, related_name='columns', on_delete=models.CASCADE)
    name_column = models.CharField(max_length=255)
    date_create = models.DateTimeField(auto_now_add=True, editable=False)

    # class Meta:
    #     verbose_name = 'Колонка'
    #     verbose_name_plural = 'Колонки'


class Tasks(models.Model):
    tittle = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    column = models.ForeignKey(Column, related_name='tasks', on_delete=models.PROTECT)

    # class Meta:
    #     verbose_name = 'Задача'
    #     verbose_name_plural = 'Задачи'
