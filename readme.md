# tidal-hunter
![version](https://img.shields.io/badge/version-alpha_0.02-666699.svg)
![python3](https://img.shields.io/badge/python3-3.6.7-336699.svg)
![django](https://img.shields.io/badge/django-1.11.18-FF0033.svg)
  
  
### 项目导航
+ [compass](https://github.com/waitspring/tidal-hunter/blob/master/compass.md)：服务端和客户端搭建指南  
+ [account](https://github.com/waitspring/tidal-hunter/tree/master/account)：和用户管理相关的后端源文件目录
+ [board](https://github.com/waitspring/tidal-hunter/tree/master/board)：潮汐猎人项目中，和首页统计面板相关的后端源文件目录
+ [engineering](https://github.com/waitspring/tidal-hunter/tree/master/engineering)：潮汐猎人项目中，和项目管理相关的后端源文件目录
+ [scripts](https://github.com/waitspring/tidal-hunter/tree/master/scripts)：潮汐猎人的 `shell` 脚本目录，这些脚本在后端源文件中被调用
+ [static](https://github.com/waitspring/tidal-hunter/tree/master/static)：潮汐猎人的静态资源目录
+ [templates](https://github.com/waitspring/tidal-hunter/tree/master/templates)：潮汐猎人的 `html5` 模板文件目录
+ [tidal](https://github.com/waitspring/tidal-hunter/tree/master/tidal)：潮汐猎人的根应用目录
  

### 书写规范
在潮汐猎人项目中，我们使用中文文字来编写所有的 readme.md 文件，并使用英文文字来编写所有的源代码文件  
其中，源代码文件严格遵守如下规范  

   
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
   

