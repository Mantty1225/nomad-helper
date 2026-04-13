# 部署指南

## 方案一：Render（推荐）

### 步骤1：创建GitHub仓库
1. 在GitHub上创建新仓库，名为`nomad-helper`
2. 将本项目文件上传到该仓库

### 步骤2：部署到Render
1. 访问 https://render.com
2. 注册/登录账号
3. 点击 "New Web Service"
4. 选择GitHub仓库`nomad-helper`
5. 配置：
   - **Name**: nomad-helper
   - **Environment**: Python
   - **Build Command**: pip install -r requirements.txt
   - **Start Command**: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
   - **Instance Type**: Free
6. 点击 "Create Web Service"
7. 等待部署完成（约2-3分钟）

### 步骤3：访问应用
部署完成后，Render会提供一个URL，比如`https://nomad-helper.onrender.com`

---

## 方案二：Streamlit Cloud

### 步骤1：上传到GitHub
（同上）

### 步骤2：部署到Streamlit Cloud
1. 访问 https://streamlit.io/cloud
2. 使用GitHub账号登录
3. 点击 "New app"
4. 选择GitHub仓库`nomad-helper`
5. 点击 "Deploy!"
6. 等待部署（约1-2分钟）

### 步骤3：访问
Streamlit会提供URL，比如`https://nomad-helper.streamlit.app`

---

## 快速部署（推荐）

使用以下命令将代码推送到GitHub：

```bash
# 初始化Git仓库
git init
git add .
git commit -m "Initial commit: Digital Nomad Visa Helper"

# 连接GitHub
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/nomad-helper.git

# 推送
git push -u origin main
```

---

## 验证部署

部署后，请测试：
1. 打开网址
2. 填写测试信息：
   - 职业：程序员
   - 月收入：25000
   - 目标大洲：欧洲
   - 偏好：安全、网络好
   - 家庭情况：单躿
3. 点击"获取推荐"
4. 确认能看到推荐结果

---

## 问题排查

如果部署失败：
1. 检查requirements.txt是否存在
2. 检查app.py是否有语法错误
3. 检查日志中的错误信息
4. 确保依赖包版本兼容

---

**✅ 部署完成后，请将URL发给我，我会验证并优化！**
