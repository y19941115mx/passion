from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField

# Create your models here.


class Banner(models.Model):
    class Meta:
        verbose_name = '轮播位'
        verbose_name_plural = verbose_name

    type_choices = (
        (0, '首页轮播图'),
        (1, '活动轮播图'),
    )
    desc = models.CharField('描述', max_length=50)
    type = models.IntegerField('类型', choices=type_choices, default=0)
    add_time = models.DateTimeField('添加时间', default=datetime.now())


class BannerItem(models.Model):
    class Meta:
        verbose_name = "轮播内容"
        verbose_name_plural = verbose_name
    url = models.CharField('跳转路径', max_length=50)
    detail = UEditorField(verbose_name=u"轮播详情",width=600, height=300, imagePath="courses/ueditor/",
                                         filePath="courses/ueditor/", default='略')
    banner = models.ForeignKey(Banner, verbose_name='轮播位', null=True)
    image = models.ImageField('图片', upload_to='Banner/%Y/%m', max_length=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now())

