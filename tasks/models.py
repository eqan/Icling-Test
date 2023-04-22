from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    order = models.IntegerField()
    description = models.TextField()
    TASK_TYPES = (
        ('SURVEY', 'Survey'),
        ('DISCUSSION', 'Discussion'),
        ('DIARY', 'Diary'),
    )
    type = models.CharField(max_length=10, choices=TASK_TYPES)

    def __str__(self):
        return self.title


class Tile(models.Model):
    launch_date = models.DateField()
    TILE_STATUSES = (
        ('LIVE', 'Live'),
        ('PENDING', 'Pending'),
        ('ARCHIVED', 'Archived'),
    )
    status = models.CharField(max_length=10, choices=TILE_STATUSES)
    tasks = models.ManyToManyField(Task, related_name='tiles')

    def __str__(self):
        return f'Tile {self.id}'
