import asyncio
import tornado

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

async def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8888)
    await asyncio.Event().wait()

if _name_ == "_main_":
    asyncio.run(main())