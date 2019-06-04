# document
![version](https://img.shields.io/badge/architecture-C/S/O-DAC9A6.svg)

### 环境说明
对于标准的 devops 流程而言，工程上线通常会经历如下几个环境  

<table>
    <tbody>
        <tr>
            <td width=150 align=center>环境类型</td>
            <td width=200 align=center>环境标识</td>
            <td width=548 align=center>环境说明</td>
        </tr>
        <tr>
            <td width=150 align=center>测试环境</td>
            <td width=200 align=center>test</td>
            <td width=548>可以推送不同的源代码分支</td>
        </tr>
        <tr>
            <td width=150 align=center>预发布环境</td>
            <td width=200 align=center>prelease</td>
            <td width=548>仅能够推送 master 源代码分支（或其他固定的正式分支）</td>
        </tr>
        <tr>
            <td width=150 align=center>灰度环境</td>
            <td width=200 align=center>gray</td>
            <td width=548>拉取预发布环境内已经被验证过的编译文件</td>
        </tr>
        <tr>
            <td width=150 align=center>生产环境</td>
            <td width=200 align=center>prod</td>
            <td width=548>拉取灰度环境内已经被验证过的编译文件</td>
        </tr>
    </tbody>
</table>