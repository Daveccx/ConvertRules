# ConvertRules

Daveccx 的 mihomo 配置与规则集。公开仓库中不保存订阅链接、代理密码和控制器密钥。

## 目录

| 路径 | 用途 |
| --- | --- |
| `configs/` | Clash Verge、CMFA、FlClash 四端脱敏模板 |
| `rules/ALan.yaml` | 个人直连规则，人工维护 |
| `rules/myProxy_ip.yaml` | 个人代理规则，人工维护 |
| `rules/*.yaml` | 每日从 MetaCubeX 下载的公共规则 |
| `scripts/download-rules.py` | 规则下载脚本 |

## 使用

1. 从 `configs/` 下载对应客户端模板。
2. 在 `proxy-providers` 中填入自己的订阅 URL。
3. Windows 客户端如果使用 TUN，请在客户端界面开启，并按需设置端口。
4. `ALan` 和 `myProxy_ip` 通过仓库 Raw URL 引用；修改后客户端重新下载规则即可。
5. Actions 每天北京时间 04:00 更新公共规则，不会覆盖这两个个人文件。

Raw URL：

```text
https://raw.githubusercontent.com/Daveccx/ConvertRules/main/rules/ALan.yaml
https://raw.githubusercontent.com/Daveccx/ConvertRules/main/rules/myProxy_ip.yaml
```

## 安全

- 不要向本仓库提交真实订阅、节点、token、密码或 `secret`。
- 模板默认 `allow-lan: false`，且不含 `external-controller`。
- 如果订阅已经泄露，请在订阅服务商处重置链接，而不只是从仓库删除文本。
