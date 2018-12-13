import cherrypy
from classes import *

c = Station('Dhwani','2015','01054')
#c.managing_json()

class app(object):

    @cherrypy.expose
    def index(self):
	return "Learning classes in python"
        
    @cherrypy.expose
    def init_station(self):
	
	temp1 = c.init_station()
	return "HELLLOO"

    @cherrypy.expose
    def execute_routine(self,routine_id):
	print(routine_id)
	temp3 = c.execute_routine(routine_id)
	return "Byeee"


    @cherrypy.expose
    def shutdown_station(self):
	
	temp2 = c.shutdown_station()
	return "Worlldddd"


if __name__ == '__main__':
    cherrypy.quickstart(app())
    
