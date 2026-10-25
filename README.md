# leopard-base

Leopard 基础数据包：目录骨架 + 默认配置文件（initrc / fstab / paths / profile）。

纯数据包，无二进制，产物：`leopard-base-1.0_1.x86_64.xbps`。

## 内容
- `system/config/initrc`  — 默认服务（启动期配置，引导分区，leopard-rc 读取）
- `system/config/fstab`   — 挂载表（启动期配置，引导分区，leopard-mountd 读取）
- `config/paths`          — 默认命令搜索路径（非启动期配置）
- `config/profile`        — 默认 shell profile（非启动期配置）

配置目录约定：
- **启动期配置**（initrc/fstab，启动就要读）→ `/system/config/`
- **非启动期配置**（paths/profile/xbps.d 等）→ `/config/`

## 构建
```
python3 gen_ninja.py && ninja pack
```
