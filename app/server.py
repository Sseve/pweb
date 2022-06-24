from sanic import Sanic
from db import setup_db
from config import setting
from api.sysview import sys_bp


app = Sanic(__name__)
# 加载配置
app.config.update_config(setting)
# 数据库连接
setup_db(app)
#添加路由视图
app.blueprint(sys_bp)


# 启动app实例
app.run(
    host=app.config["APP_HOST"],
    port=app.config["APP_PORT"],
    debug=app.config["APP_DEBUG"],
    auto_reload=app.config["APP_RELOAD"]
    )