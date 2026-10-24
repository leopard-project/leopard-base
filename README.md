# leopard-base

Leopard 基础数据包：目录骨架 + 默认配置文件（initrc / paths / profile）。

纯数据包，无二进制，产物：`leopard-base-1.0_1.x86_64.xbps`。

## 内容
- `system/etc/leopard/initrc`  — 默认服务（默认 enable getty）
- `system/etc/leopard/paths`  — 默认命令搜索路径
- `system/etc/leopard/profile` — 默认 shell profile

## 构建
```
python3 gen_ninja.py && ninja pack
```
