
try:
	 #from app import *
	exec(open("app.python",'r').read())
except Exception as ex:
	print(ex)
	#from unchangable_app import *

	exec(open("unchangable_app.python",'r').read())
	
	
	
