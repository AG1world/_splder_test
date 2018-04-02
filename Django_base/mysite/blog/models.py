from django.db import models

# Create your models here.


# 'creat table book(' \
# '   name varchar(20),' \
# '   price float(4,2),' \
# ')'



class Book(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    pub_date = models.DateField()
    author = models.CharField(max_length=30)
    # 一对多的外键　　ａｕｔｈ　对应　ｐｕｂｌｉｓｈ
    publish = models.ForeignKey('Publish')
    # 多对多的设置
    authors = models.ManyToManyField('Author')

    def __str__(self):
        return self.name

class Publish(models.Model):
    name = models.CharField(max_length=100)
    city  = models.CharField(max_length=35)

    def __str__(self):
        return self.name

# 手动创建第三张表 book_author <以手动创建第三张表并将数据多对多关系,并可以添加表间打关系;建立时manytomany键不需要>
# 多对多关系从表
# class book_authors(models.Model):
#     book = models.ForeignKey('Author')
#     author = models.ForeignKey('Book')



class Author(models.Model):
    au_name = models.CharField(max_length=30)
    au_age = models.IntegerField(default=None)


    def __str__(self):
        return self.au_name


