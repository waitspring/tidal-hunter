# tidal hunter
![version](https://img.shields.io/badge/version-alpha_0.01-666699.svg)
![python3](https://img.shields.io/badge/python3-3.6.7-336699.svg)
![django](https://img.shields.io/badge/django-1.11.18-FF0033.svg)

> 这是一个自动化运维平台的示例项目  

### 运行环境
* 系统环境: ubuntu 18.04.2 LTS
* 服务环境: python 3.6.7
* 框架环境: django 1.11.18
* 数据库环境: postgresql 10.6

运行潮汐猎人服务前，需要使用 apt-get 工具和 pip3 工具配置如下模块

```bash
hostname$ sudo pip3 install Django==1.11.18
hostname$ sudo pip3 install gunicorn==19.3.0
hostname$ sudo pip3 install Pillow==5.1.0
hostname$ sudo pip3 install Markdown==2.6.2
hostname$ sudo pip3 install psycopg2==2.7.6.1
hostname$ sudo pip3 install psycopg2-binary==2.7.7
```

此外，我们还应当检查项目数据库环境的准备情况  
请确认 postgresql 数据库内已经存在数据库实例 tidal\_hunter，且当前主机用户对 tidal\_hunter 实例可读可写  

```bash
hostname$ psql --version
hostname$ psql -d tidal_hunter
```

在 postgresql 内需要执行的 sql 语句如下

```
postgres=# CREATE DATABASE tidal_hunter template template0;
postgres=# GRANT ALL ON DATABASE tidal_hunter TO user_name;
```

若潮汐猎人的运行环境已经配置完成，则使用如下命令启动服务，并使用 chrome 浏览器默认通过 8000 端口访问内容  

```bash
hostname$ python3 hunter.py makemigrations
hostname$ python3 hunter.py migrate
hostname$ python3 hunter.py runserver
```


### 目录结构
##### [account/](https://github.com/waitspring/tidal-hunter/tree/master/account)
平台账户相关的功能应用
##### [board/](https://github.com/waitspring/tidal-hunter/tree/master/board)
平台首页面板相关的功能应用，对应到平台的侧边导航栏为数据看板功能
##### [engineering/](https://github.com/waitspring/tidal-hunter/tree/master/engineering)
平台项目管理相关的功能应用，对应到平台的侧边导航栏为项目管理功能
##### [static/](https://github.com/waitspring/tidal-hunter/tree/master/static)
存放潮汐猎人项目中，需要用到的所有静态资源文件  
##### [templates/](https://github.com/waitspring/tidal-hunter/tree/master/templates)
存放潮汐猎人项目中，所有的 html5 网页模板资源文件，该目录下的子目录和各个应用模块对应  
##### [tide/](https://github.com/waitspring/tidal-hunter/tree/master/tide)
潮汐猎人项目的根配置文件，符合 django 框架标准，存放 settings.py urls.py wsgi.py 等文件  
##### [hunter.py](https://github.com/waitspring/tidal-hunter/blob/master/hunter.py)
潮汐猎人的项目管理文件，和普通 django 项目中的 manage.py 文件起相同的作用  

### 书写规范
在潮汐猎人项目的源码文件中，我们将严格按照以下书写规范  

<table>
    <tbody>
        <tr>
            <td width=150>模块</td>
            <td width=548>使用小写单词加下划线叙事的方式命名模块</td>
            <td width=200>my_example.py</td>
        </tr>
        <tr>
            <td width=150>类</td>
            <td width=548>使用强驼峰的方式命名类</td>
            <td width=200>MyExample</td>
        </tr>
        <tr>
            <td width=150>对象</td>
            <td width=548>使用小写单词加下划线叙事的方式命名对象</td>
            <td width=200>my_example</td>
        </tr>
        <tr>
            <td width=150>方法和属性</td>
            <td width=548>使用小写单词加下划线叙事的方式命名方法和属性</td>
            <td width=200>my_example</td>
        </tr>
        <tr>
            <td width=150>函数</td>
            <td width=548>使用小写单词加下划线叙事的方式命名函数</td>
            <td width=200>my_example</td>
        </tr>
        <tr>
            <td width=150>变量</td>
            <td width=548>使用小写单词加下划线叙事的方式命名变量</td>
            <td width=200>my_example</td>
        </tr>
        <tr>
            <td width=150>常量</td>
            <td width=548>使用小写单词加下划线叙事的方式命名常量</td>
            <td width=200>my_example</td>
        </tr>
        <tr>
            <td width=150>字段</td>
            <td width=548>使用弱驼峰的方式命名字典内的字段</td>
            <td width=200>myExample</td>
        </tr>
        <tr>
            <td width=150>异常类</td>
            <td width=548>使用强驼峰的方式命名异常类，结尾单词 Error</td>
            <td width=200>MyExampleError</td>
        </tr>
    </tbody>
</table>

  

### 其他说明
  
tidal hunter&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[&nbsp;&nbsp;n.&nbsp;&nbsp;]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;潮汐猎人  
  
tidal hunter 是经典电子竞技游戏 dota 中的一个英雄名称，中国玩家称呼这个英雄为潮汐猎人，简称潮汐  
潮汐猎人在 dota 游戏中的定位是控制和辅助，能够承担战场伤害，同时控制对方英雄，为队友创造输出环境  
这样的游戏定位和 devops 平台在软件项目开发过程中的定位很类似  
  
潮汐猎人仍然会使用传统的 mvc 开发架构  
其中所反映出的项目管理流程理念和功能模块的划分规则来自于我个人长期任职的八戒元创运维开发团队  
此外，潮汐猎人还借鉴了 github 上已有的自动化运维项目 [adminset](https://github.com/guohongze/adminset)  
  
关于潮汐猎人的任何疑问，都可以发送邮件到 newsfuxuanming@foxmail.com 来和我沟通  
如果对 django 的基本知识缺乏了解，我们建议可以先查阅 [scrum](https://github.com/waitspring/scrum) 项目  
  
  
最后，送给大家一句《滕王阁序》中的诗文:  
> 老当益壮，宁移白首之心  
> 穷且益坚，不坠青云之志
  
  
