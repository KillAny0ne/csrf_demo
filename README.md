# 项目介绍

- normal.py模拟正常网站业务逻辑
- hack.py模拟csrf攻击者构造页面
- 详情见代码

# 项目目的

- 采用简单场景便于初学者理解csrf攻击原理

- 可在下方代码检验段进行验证完善

  ```
  if(request.headers.get('Referer')!='http://192.168.17.134:5565'):
              name += '\nYou are Just Attacked by someone!Please check it!'
              return "No CSRF Attack !"
  ```

- 可进一步添加csrf-token或双cookie的逻辑代码尝试防御csrf攻击

## 项目启动

直接python3 xxx.py启动即可，启动后默认搭建在5555与5556端口