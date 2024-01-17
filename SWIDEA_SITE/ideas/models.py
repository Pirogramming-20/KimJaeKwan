from django.db import models
from toolss.models import Tool

# Create your models here.
class Idea(models.Model):
    title = models.CharField('제목', max_length=24)
    photo = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')
    content = models.CharField('아이디어 설명', max_length=100)
    interestedNum = models.IntegerField('아이디어 관심도', default=0)

    def get_tool_choices():
        toolss = Tool.objects.all()
        return [(tool.name, tool.name) for tool in toolss]

    tool = models.CharField('예상 개발툴', max_length=24, choices=get_tool_choices())
    
    created_date = models.DateTimeField('작성일', auto_created=True, auto_now_add=True)
    updated_date = models.DateTimeField('수정일', auto_created=True, auto_now=True)

    star = models.BooleanField(default = False)