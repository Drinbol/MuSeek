# MuSeek

写作语料素材库：用于收集、管理写作素材的 Web 应用。

## 技术栈

**后端**（`Backend/`）：Python + FastAPI

```
api/        路由与接口
crud/       数据库增删改查
models/     ORM 模型
schemas/    Pydantic 模型
init.sql    数据库初始化脚本
```

**前端**（`Frontend/`）：Vue 3 + Vite

- ant-design-vue 4 组件库
- axios / vue-router / vue-request

## 本地运行

### 后端

```bash
cd Backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 前端

```bash
cd Frontend
npm install
npm run dev
```
