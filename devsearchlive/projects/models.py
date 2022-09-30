from django.db import models
import uuid

class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    # owner =
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # null is for database, blank is for django
    featured_image = models.ImageField(null=True, blank=True)
    demo_link = models.CharField(max_length=1000, null=True, blank=True)
    source_link = models.CharField(max_length=200, null=True, blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True) # Timestamp auto created
    tags = models.ManyToManyField('Tag', blank=True) # Creating a many-to-many relationship

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            img = self.featured_image.url
        except:
            img = ''
        return img


class Review(models.Model):

    VOTE_TYPE = (
        ('up','up'),
        ('down', 'down'),
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    # owner =
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    updated = models.DateTimeField(auto_now=True)  # Timestamp auto updated when entry updated
    created = models.DateTimeField(auto_now_add=True) # Timestamp auto created when entry created

    def __str__(self):
        return self.value


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)  # Timestamp auto created when entry created

    def __str__(self):
        return self.name
