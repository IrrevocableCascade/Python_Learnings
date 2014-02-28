__author__ = 'Irrevocable Cascade'

from bottle import route, run, template
import mycalendar

c = mycalendar.HTMLCalendar(2014)

@route('/')
def index(name='year'):
    return template(c.printmonth(3, True), name=name)

run(host='localhost', port=8090)


