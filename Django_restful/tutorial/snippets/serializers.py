# 当需要在模块内运行程序,加上下面的环境变量

import os,django



os.environ.update({"DJANGO_SETTINGS_MODULE": "tutorial.settings"})
django.setup()

# 在数据库迁移完成后进行序列化操作
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # 利用字段控制序列化渲染到html页面时的显示模板

    code = serializers.CharField(style={'base_templates':'textarea.html'})

    linenos = serializers.BooleanField(required=False)

    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,default='python',)

    style = serializers.ChoiceField(choices=STYLE_CHOICES,default='friendly',)

    # 给定经过验证的数据,创建并返回一个新的Snipper 实例
    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)

    # 给定经过验证的数据,更新并返回一个已经存在的Snippet实例
    def update(self, instance, vaildated_data):
        if instance:
            instance.title = vaildated_data.get('title', instance.title)
            instance.code = vaildated_data.get('code', instance.code)
            instance.linenos = vaildated_data.get('linenos', instance.linenos)
            instance.language = vaildated_data.get('language', instance.language)
            instance.style = vaildated_data.get('title', instance.style)
            instance.save()
            return instance
        return Snippet(**vaildated_data)



if __name__=="__main__":
    from snippets.models import Snippet
    from snippets.serializers import SnippetSerializer

    from rest_framework.parsers import JSONParser
    # 1. 将对象序列化
    snippet = Snippet(code='print "hello, world"\n')
    snippet.save()
    serializer = SnippetSerializer(snippet)
    print(serializer.data)
    #  {'title': '', 'id': 6, 'style': 'friendly',
    # 'code': 'print "hello, world"\n', 'language': 'python',
    #  'linenos': False}

    # 2. 将数据反向序列化成对象
    from django.utils.six import BytesIO

    content = "{'title': '', 'code': 'print 'hello, world'\n', 'id': 7, 'linenos': False, 'style': 'friendly', 'language': 'python'}"
    stream = BytesIO(content)
    data = JSONParser().parse(stream)

    serializer = SnippetSerializer(data=data)
    print(serializer.is_valid())

    d = serializer.validated_data
    print(d)

    serializer.save()
    print(serializer)




# 1. restore_object() 3.0以上版本不支持已经被create()和update()方法代替,源码如下：
# Serializer `%s.%s` has old-style version 2 `.restore_object()` '
    'that is no longer compatible with REST framework 3. '
    'Use the new-style `.create()` and `.update()` methods instead.'

# 2. django应使用1.10.7版本才不会出现奇怪的错误