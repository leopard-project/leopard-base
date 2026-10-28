# PROJECT KNOWLEDGE BASE — leopard-base

Leopard 基础数据包：目录骨架 + 默认配置（initrc / fstab / paths / profile）。

纯数据包，无二进制，产物 `leopard-base-*.xbps`。

## 内容
- `system/config/initrc` — 默认服务（启动期配置，引导分区，leopard-rc 读取）
- `system/config/fstab` — 挂载表（leopard-mountd 读取）
- 其余 paths/profile 等运行时配置

## 构建
    python3 gen_ninja.py && ninja pack
