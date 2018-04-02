#

name = '苍老师'
def outer(func):
    name = 'alex'
    func()
def show():
    print(name)

outer(show)   #结果  苍老师



