##Django
* WSGI:python中web服务器与应用框架之间的接口
* 快速开发和DRY原则(Do not repeat yourself)
* MVT:M(数据库交互),V(接收请求进行处理),T(产生html页面)等价于MCV
* 虚拟环境,使用的python是复制的python,安装python包也在复制的里面
    * pip3 install virtualenv virtualenvwrapper 安装虚拟环境及扩展包
    * 创建:mkvirtualenv 虚拟环境名
    * 进入:workon xx
    * 退出:deactivate
    * 删除:rmvirtualenv
    * 查看安装的包：pip list/freeze
* Django
    * 创建：django-admin startproject 项目名
    * settings.py:项目配置文件
    * urls.py:进行url路由的配置
    * wsgi.py:web服务器和Django交互的入口
    * manage.py:项目的管理文件
* 一个项目由很多个应用组成，每个应用完成一个特定的功能
    * 创建应用：python manage.py startapp 应用名
        * model.py:写和数据库项目的内容
        * views.py:定义处理函数
        * tests.py:写测试代码的文件
        * admin.py:网站后台管理相关的文件