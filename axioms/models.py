from django.db import models
from django.core.exceptions import ValidationError

class SingleInstanceMixin(object):
    """Makes sure that no more than one instance of a given model is created."""

    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and self.id != model.objects.get().id):
            raise ValidationError("Can only create 1 %s instance" % model.__name__)
        super(SingleInstanceMixin, self).clean()


class Axiom(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=200, blank=True, default='')
    text = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='axioms', on_delete=models.CASCADE)


    class Meta:
        ordering = ['pk']

    def __str__(self):
        return "ID: %s CATEGORY: %s Text: %s" %(str(self.pk), self.category, self.text)


class Intro(SingleInstanceMixin, models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    footer = models.CharField(max_length=500, blank=True, default='')

    def __str__(self):
        return "TITLE: %s" %(str(self.title))
