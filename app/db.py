from databases import Database


def setup_db(app):
    app.ctx.db = Database(app.config["DB_ADDR"])

    @app.after_server_start
    async def connect(*args, **kwargs):
        await app.ctx.db.connect()

    @app.after_server_stop
    async def disconnect(*args, **kwargs):
        await app.ctx.db.disconnect()