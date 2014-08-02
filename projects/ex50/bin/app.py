import web

urls = (
  '/', 'index'

)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
    def GET(self):
        greeting = "Hello World"
        return render.index(greeting = greeting)


class stuff:
    def GET(self):
        greeting = "you found stuff"
        return greeting


if __name__ == "__main__":
    app.run()
