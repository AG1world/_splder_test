# 装饰器实现验证登录功能
# 1.通过对用户名和密码的匹配，来修改默认login=Flase的状态
# 2.当用户的用户名 和登录状态为True即可直接跳转到主页，跳过输入账号
user_dict = [{'name': 'sb', 'passkw': 123}, {'name': 'caiji', 'passkw': 123}]


# 通过对全局变量的修改来实现状态的保持
current_dict = {'name': None, 'login': 'Flase'}


def auth_func(func):
    def wrapper(*args, **kwargs):
        # 在执行验证时，先获取保留状态
        if current_dict['name'] and current_dict['login']:
            res = func(*args, **kwargs)
            return res
        # 输入账号和密码
        name = input('请输入账号：').strip()
        passkw = input('请输入密码:').strip()
        for i in user_dict:
            if i['name'] == name and i['passkw'] == int(passkw):
                current_dict['name'] = name
                current_dict['login'] = True
                res = func(*args, **kwargs)
                return res

        else:
            # 当验证之后，账号和密码皆不符合
            print('账号或密码不正确')

    return wrapper


@auth_func
def index():
    print('欢迎来到JD')


@auth_func
def home():
    print('欢迎来到机器人之家')


@auth_func
def gan():
    print('欢迎来到实干出真知')


index()
home()
gan()

