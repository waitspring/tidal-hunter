# document
![architecture](https://img.shields.io/badge/architecture-speical-E1A679.svg)  
  
  
### 架构理念
  
> devops 平台即是具有流程化特性的，各种开发和运维工具的封装体
  
以上是我们从运维开发工程师的视角，给 devops 平台所下的定义  
那么，根据以上的定义我们知道  
  
+ devops 平台应当是工具化的，并带有流程属性的，能够帮助我们完成主机资产管理，产品自动化上线或下线等任务  
+ devops 平台应当整合企业原有的，已经用于开发和运维工作中的中间件或工具，形成一个统一的封装体  
  
由此可见，真正决定企业 devops 架构的，是 devops 封装体之下的环境配置方式，中间件和其他运维开发工具的组织形态  
这些工具可能会包括 

<table>
    <tbody>
        <tr><td width=200 align=center>jira</td>
            <td width=698>项目管理工具，用于事务跟踪，任务追述和流程审批等工作</td></tr>
        <tr><td align=center>gitlab</td>
            <td>源代码托管工具</td></tr>
        <tr><td align=center>jenkins</td>
            <td>源代码构建工作管理工具，在传统架构中配合 sync 归档主机一起使用</td></tr>
        <tr><td align=center>sync</td>
            <td>统一归档环境内所有项目的源代码构建结果</td></tr>
        <tr><td align=center>openstack</td>
            <td>虚拟机编排管理工具</td></tr>
        <tr><td align=center>kubernetes</td>
            <td>容器编排管理工具</td></tr>
        <tr><td align=center>zabbix</td>
            <td>虚拟机状态监测工具，通常在生产环境中使用，其客户端内置于所有生产环境主机节点内</td></tr>
        <tr><td align=center>elk</td>
            <td>实时的日志采集存储和分析工具，通常在生产环境中使用</td></tr>
        <tr><td align=center>nginx</td>
            <td>互联网协议请求的反向代理工具</td></tr>
        <tr><td align=center>dns</td>
            <td>域名解析工具，搭建线下的 dns 可以保持域名在各个环境中的一致性</td></tr>
    </tbody>
</table>

### 架构设计
为布局潮汐猎人项目，我们建议将企业的环境架构进行如下设计  

<table>
    <tbody>
        <tr><td width=200 align=center>service</td>
            <td width=698>服务环境</td></tr>
        <tr><td align=center>test</td>
            <td>测试环境</td></tr>
        <tr><td align=center>prelease</td>
            <td>预发布环境</td></tr>
        <tr><td align=center>gray</td>
            <td>灰度环境</td></tr>
        <tr><td align=center>prod</td>
            <td>生产环境</td></tr>
    </tbody>
</table>

其中，test | prelease | gray 在内的每个环境都应配置有独立的，服务于业务的中间件工具，这些工具包括  

+ `dns`
+ `nginx`
+ `jenkins`
+ `sync`

此外，在服务环境内，还应配置有公用的中间件工具，例如  

+ `configure center`
+ `gitlab`
