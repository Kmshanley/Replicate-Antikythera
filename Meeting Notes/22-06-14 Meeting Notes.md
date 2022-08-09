Erik is going to meet with Professor Rawlins tomorrow to ask clarifying questions
	What do you mean by "best methods to travel from point A to point B given a time frame and travel method"?
	Do we need to account for the planets elitical orbits?
	How involved do our eclipse calculations need to be
	Can we just query existing databases or do we have to model it ourselves
	
	

JPL's Horizons API
https://ssd-api.jpl.nasa.gov/doc/horizons.html
	NASA API
	Can be queried for information on solar bodies
	
Using PyGame for GUI?

Simple Model of the solar system
	Each Satellite object has:
		Distance to Sun				in km
		Lenght of year				in years (earth years)
		Angle on Epoch				in degrees
		
	Then you can model the relative position of any satellite on any date before or after the epoch
	Could be a reasonable predictor of aligments
		An aliignment would be when the satellites are within X degrees of each other
	Not nearly good enough to predict eclipses
	
	
		