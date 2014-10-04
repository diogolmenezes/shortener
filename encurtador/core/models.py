from django.db import models
from encurtador.core.shorter  import to_short

class Url(models.Model):
  original = models.CharField(max_length=200)
  short    = models.CharField(max_length=50)
  views    = models.IntegerField(default=0)


  class Meta:
    ordering = ['-views']

  def __unicode__(self):
    return self.short

  def save(self):
    self.short = to_short(self.original)
    super(Url, self).save()

