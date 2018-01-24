

# 面向对象 往房子里面添加家具

# 房子属性：剩余面积和添加家具
class House(object):
    def __init__(self,area):
        self.area = area
        self.containsItem= []
    # 添加家具：修改房子占地面积，房子属性家具多的物件
    def contain_fur(self,item):
        if self.area >=item.occ_area:
            self.area = self.area - item.occ_area
            self.containsItem.append(item.name)
        else:
            raise AreaErr('添加%s面积大于房子剩余面积' % item)

    # 返回 剩余面积和添加的家具
    def __str__(self):
        msg = '房间面积剩余'+str(self.area)+','
        if len(self.containsItem)>0:
            msg = msg + '添加家具有：'
            for i in self.containsItem:
                msg= msg +str(i)+' '
        return msg

class Furniture(object):
    def __init__(self,name,occ_area):
        self.name = name
        self.occ_area = occ_area
    def __str__(self):
        return self.name

class AreaErr(Exception):
    def __init__(self,err_msg):
        self.err_msg = err_msg
    def __str__(self):
        return self.err_msg



if __name__ == '__main__':

    tizi = Furniture('梯子', 200)
    house = House(500)

    house.contain_fur(tizi)
    bed = Furniture('床', 200)
    house.contain_fur(bed)
    print(house)

# //TODO  优化参数传入方式

# //TODO  俩个类的关系就是通过 house_area 与 fur_area 之间的比较和修改剩余关系
# 手动传参
# tizi = Furniture('梯子',200)
# print(tizi)
# house = House(300)
# print(house)
# house.contain_fur(tizi)
# print(house)
# bed = Furniture('床',100)
# house.contain_fur(bed)
# print(house)