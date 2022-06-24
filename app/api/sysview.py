import sanic
from sanic.response import json
from sanic.views import HTTPMethodView
from service.syshandler import UserHandler


sys_bp = sanic.Blueprint("sysbp", url_prefix="/api")


class LoginView(HTTPMethodView):
    async def get(self, request):
        """用户列表"""
        return json({"method": "get"})

    async def post(self, request: sanic.Request):
        """用户登录"""
        user_handler = UserHandler(request.app.ctx.db)
        user = request.body.decode()
        if await user_handler.check_user(user):
            return json({"code": 200, "msg": "登录成功!"})
        return json({"code": 400, "msg": "登录失败"})


class UserView(HTTPMethodView):
    """user view"""
    async def get(self, request):
        return json({"method": "get"})

    async def post(self, request: sanic.Request):
        return json({"method": "post"})

    async def delete(self, request):
        return json({"method": "delete"})

    async def patch(self, request):
        return json({"method": "patch"})

    async def put(self, request):
        return json({"method": "put"})


class RoleView(HTTPMethodView):
    """role view"""
    async def get(self, request):
        return json({"method": "get"})

    async def post(self, request):
        return json({"method": "post"})

    async def delete(self, request):
        return json({"method": "delete"})

    async def patch(self, request):
        return json({"method": "patch"})

    async def put(self, request):
        return json({"method": "put"})


class MenuView(HTTPMethodView):
    """menu view"""
    async def get(self, request):
        return json({"method": "get"})

    async def post(self, request):
        return json({"method": "post"})

    async def delete(self, request):
        return json({"method": "delete"})

    async def patch(self, request):
        return json({"method": "patch"})

    async def put(self, request):
        return json({"method": "put"})


sys_bp.add_route(LoginView.as_view(), "/user/login")
sys_bp.add_route(UserView.as_view(), "/user")
sys_bp.add_route(RoleView.as_view(), "/role")
sys_bp.add_route(MenuView.as_view(), "/menu")