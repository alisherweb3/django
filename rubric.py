class Rubric(models.Model):
  name = models.CharField(max_length=20, db_index=True, verbose_name='Name')
  
  class Meta:
    verbose_name_plural = 'Rubrics'
    verbose_name = 'Rubrica'
    ordering = ('name')
