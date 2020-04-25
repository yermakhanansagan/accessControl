from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']

class User(models.Model):
    STATUS = (
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )
    name = models.CharField(max_length=30, null=True)
    surname = models.CharField(max_length=30, null=True)
    status = models.CharField(max_length=30, null=True, choices=STATUS)
    student_id = models.CharField(max_length=30, blank=True, unique=True, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name

class Access(models.Model):
    card_id = models.CharField(primary_key=True, max_length=30, blank=True, unique=True, null=False)
    access = models.BooleanField(blank=True, default=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.card_id


class History(models.Model):
    STATUS = (
        ('IN', 'IN'),
        ('OUT', 'OUT'),
    )
    status = models.CharField(max_length=30, null=True, choices=STATUS)
    entry_date = models.DateTimeField(auto_now_add=True, null=True)
    card = models.ForeignKey(Access, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.status