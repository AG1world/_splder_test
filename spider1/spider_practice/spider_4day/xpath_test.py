# -*- coding:utf-8 -*-

from lxml import etree



text = '''
    <div>
        <ul>
            <li class="item-1"><a href="link1.html"></a></li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-inactive"><a href="link3.html">third item</a></li>
            <li class="item-1"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a>
        </ul>
    </div>
'''

# 将html文件创建element对象
html = etree.HTML(text)
# 查看文件的对象和方法
print(dir(html))

bytes_data = etree.tostring(html)
# 生成二进制xml 字符串型数据，且会补全html文件<例如 少的标签括号>
print(bytes_data)
print(bytes_data.decode('utf-8'))

# 通过xpath匹配规则来获取列表
xpath_text= html.xpath('//ul/li/a/text()')
xpath_herf= html.xpath('//ul/li/a/@href')

# 获取a标签对象列表
xpath_list = html.xpath('//ul/li/a')
print(xpath_list)

# 获取俩个列表值
for node in xpath_list:
    text = node.xpath('./text()')if len(node.xpath('./text()')) else None
    href = node.xpath('./@href')if len(node.xpath('./@href')) else None
    print(text,href)

