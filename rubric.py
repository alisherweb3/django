class Rubric(models.Model):
  name = models.CharField(max_length=20, db_index=True, verbose_name='Name')
  
  rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Rubrica')
  
  def __str__(self): return self.name
  
  class Meta:
    verbose_name_plural = 'Rubrics'
    verbose_name = 'Rubrica'
    ordering = ('name')
