def index(request):
  bbs = Bb.objects.all()
  rubrics = Rubric.object.all()
  context = {'bbs': bbs, 'rubrics': rubrics}
  return render(request, 'bboard/index.html', context)
