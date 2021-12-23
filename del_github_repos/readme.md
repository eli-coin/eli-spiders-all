#1.新建del_repos.txt
分行存放需要删除的库名，以下csy1993为github账号名，test1和test2为库名

csy1993/test1  
csy1993/test2

#2.获取github相关token
登陆github，访问https://github.com/settings/tokens
点击“Generate new token”
“Note”自定义，在“delete_repo”前打钩，新建一个具有删除库权限的token
复制token值


#3.运行批量任务
进入del_repos.txt所在目录，将下列命令中xxx更换为步骤2中获取的token值

##Linux
右击桌面空白区域，“打开终端”，输入以下指令。
```
while read r;do curl -XDELETE -H 'Authorization: token xxx' "https://api.github.com/repos/$r ";done < del_repos.txt
```
####注意:curl 可能报错,直接转换为curl xxx;curl xxx;curl xxx多个命令执行就Ok了

##Windows
按“windows键”，输入关键字“power”，打开“Windows PowerShell”，输入以下指令。

```
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 
get-content del_repos.txt | ForEach-Object { Invoke-WebRequest -Uri https://api.github.com/repos/$_ -Method “DELETE” -Headers @{"Authorization"="token xxx"} }
```

详情参考官方文档:  
https://docs.github.com/en/rest/reference/repos#delete-a-repository