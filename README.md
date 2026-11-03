# ConvertRules

Daveccx 的 mihomo 配置与规则集。公开仓库中不保存订阅链接、代理密码和控制器密钥。

## 目录

| 路径 | 用途 |
| --- | --- |
| `configs/` | Clash Verge、CMFA、FlClash 四端模板，以及完整 `mihomo.yaml` 主配置 |
| `rules/ALan.yaml` | 个人直连规则，人工维护 |
| `rules/myProxy_ip.yaml` | 个人代理规则，人工维护 |
| `rules/*.yaml` | 每日从 MetaCubeX 下载的公共规则 |
| `scripts/download-rules.py` | 规则下载脚本 |

## 使用

1. 从 `configs/` 下载对应客户端模板；需要完整 DNS、TUN、端口和策略组时使用 `mihomo.yaml`。
2. 在 `proxy-providers` 中填入自己的订阅 URL；这些 URL 只应保存在本机。
3. 默认端口：`mixed-port: 7890`；完整 `mihomo.yaml` 使用 `7890/7891/7892/7893/7894`。
4. Windows 客户端如果使用 TUN，请在客户端界面开启；FlClash/Verge 的界面开关会覆盖配置文件。FlClash 界面还可能覆盖 `find-process-mode`、DNS 和端口。
5. `ALan` 和 `myProxy_ip` 通过仓库 URL 引用；修改后客户端重新下载规则即可。
6. Actions 每天北京时间 04:00 更新公共规则，不会覆盖这两个个人文件。

Raw URL：

```text
https://cdn.jsdelivr.net/gh/Daveccx/ConvertRules@main/rules/ALan.yaml
https://cdn.jsdelivr.net/gh/Daveccx/ConvertRules@main/rules/myProxy_ip.yaml
```

## 安全

- 不要向本仓库提交真实订阅、节点、token、密码或 `secret`。
- 所有模板默认 `allow-lan: true`。这会把代理端口暴露给局域网；请只在本机配置 `authentication`，或在不共享时关闭 LAN。
- 所有模板都不含 `external-controller` 和 `secret`。
- 如果订阅已经泄露，请在订阅服务商处重置链接，而不只是从仓库删除文本。
