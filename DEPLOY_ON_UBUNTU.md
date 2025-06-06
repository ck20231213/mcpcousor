# 🐧 Ubuntu 部署指南

本文档介绍如何在 **Ubuntu 18.04 及以上** 系统上部署 [mcp-feedback-collector-web](https://github.com/sanshao85/mcp-feedback-collector-web)。

## 1. 安装基础环境
1. **安装 Node.js 18+ 与 Git**
   ```bash
   curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
   sudo apt-get install -y nodejs git
   ```
   安装完成后使用 `node -v`、`npm -v` 确认版本。

## 2. 获取项目代码（可选）
若仅需运行，可跳过此步骤直接使用 `npx`。如需本地开发或自定义部署，可执行：
```bash
git clone https://github.com/sanshao85/mcp-feedback-collector-web.git
cd mcp-feedback-collector-web
```
随后安装依赖并构建：
```bash
npm install
npm run build    # 生成 dist 目录
```

## 3. 配置环境变量
在项目根目录创建 `.env` 文件，示例如下：
```bash
# AI API 配置
MCP_API_KEY="your_api_key_here"
MCP_API_BASE_URL="https://api.ssopen.top"
MCP_DEFAULT_MODEL="grok-3"

# Web 服务器
MCP_WEB_PORT="5000"
MCP_DIALOG_TIMEOUT="60000"  # 范围 10~60000 秒

# 功能开关
MCP_ENABLE_CHAT="true"

# URL 与端口设置
MCP_USE_FIXED_URL="true"
MCP_FORCE_PORT="false"
MCP_KILL_PORT_PROCESS="false"
MCP_CLEANUP_PORT_ON_START="true"
```

## 4. 启动服务
### 方式一：直接运行（推荐）
```bash
npx mcp-feedback-collector
```

### 方式二：全局安装后运行
```bash
npm install -g mcp-feedback-collector
mcp-feedback-collector
```

### 方式三：运行构建后的源码
在第 2 步完成后使用：
```bash
npm start       # 默认端口 5000
# 如需自定义端口
npm start -- --port 5050
```

启动成功后，在浏览器访问 `http://localhost:5000` 即可进入反馈界面。

## 5. 常用命令
```bash
mcp-feedback-collector health   # 健康检查
mcp-feedback-collector config   # 查看当前配置
npm test                        # 运行测试 (源码模式)
```

## 6. 故障排除
- **端口被占用**：检查占用情况并更换端口，或启用 `MCP_KILL_PORT_PROCESS=true`。
- **环境变量未生效**：确认 `.env` 文件位置正确，或在启动命令前设置环境变量。
- 更多问题可参考仓库的 `TROUBLESHOOTING.md` 文档。

---
部署完成后即可开始使用 `mcp-feedback-collector-web` 收集反馈。祝使用顺利！
