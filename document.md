# document
![architecture](https://img.shields.io/badge/architecture-speical-E1A679.svg)  
  
  
### 架构理念
首先，我们从一个运维开发工程师的视角，先给 devops 平台下一个定义  
  
> devops 平台即是具有流程化特性的，各种开发和运维工具的封装体
  
那么，根据以上的定义我们知道  

+ devops 平台应当是工具化的，并带有流程属性的，能够帮助我们完成主机资产管理，产品自动化上线或下线等任务  
+ devops 平台应当整合企业原有的，已经用于开发和运维工作中的中间件或工具，形成一个统一的封装体  

由此可见，真正决定企业 devops 架构的，是 devops 封装体之下的环境配置方式，中间件和其他运维开发工具的组织形态  
这些工具可能会包括 

<table>
    <tbody>
        <tr><td width=200>jira</td>
            <td width=698>项目管理工具，用于事务跟踪，任务追述和流程审批等工作</td></tr>
        <tr><td>gitlab</td>
            <td>源代码托管工具</td></tr>
        <tr><td>jenkins</td>
            <td>源代码构建工作管理工具，在传统架构中配合 sync 归档主机一起使用</td></tr>
        <tr><td>openstack</td>
            <td>虚拟机编排管理工具</td></tr>
        <tr><td>kubernetes</td>
            <td>容器编排管理工具</td></tr>
        <tr><td>zabbix</td>
            <td>虚拟机状态监测工具，通常在生产环境中使用，其客户端内置于所有生产环境主机节点内</td></tr>
        <tr><td>elk</td>
            <td>实时的日志采集存储和分析工具，通常在生产环境中使用</td></tr>
        <tr><td>nginx</td>
            <td>互联网协议请求的反向代理工具</td></tr>
    </tbody>
</table>
