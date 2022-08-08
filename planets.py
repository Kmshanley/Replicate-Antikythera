import Orbit


class Body:
    def __init__(self, name, orbit, color, draw_size, parent=None):
        self.name = name
        self.orbit = orbit
        self.color = color
        self.draw_size = draw_size
        self.parent = parent
        self.x_path = []
        self.y_path = []


mercury_orbit = Orbit.Orbit(0.38709843, 0, 0.20563661, 0.00002123, 7.00559432, -0.00590158,
                            252.25166724, 149472.67486623, 77.45771895, 0.15940013, 48.33961819, -0.12214182)

venus_orbit = Orbit.Orbit(0.72332102, -0.00000026, 0.00676399, -0.00005107, 3.39777545, 0.00043494,
                          181.97970850, 58517.81560260, 131.76755713, 0.05679648, 76.67261496, -0.27274174)

earth_orbit = Orbit.Orbit(1.000000018, -0.00000003, 0.01671123, -0.00003661, -0.00054346, 0.01337178,
                          100.46691572, 35999.37306329, 102.93005885, 0.31795260, -5.11260389, -0.24123856)

mars_orbit = Orbit.Orbit(1.52371243, 0.00000097, 0.09336511, 0.00009149, 1.85181869, -0.00724757,
                         -4.56813164, 19140.29934243, -23.91744784, 0.45223625, 49.71320984, -0.26852431)

jupiter_orbit = Orbit.Orbit(5.20248019, -0.00002864, 0.04853590, 0.00018026, 1.29861416, -0.00322699,
                            34.33479152, 3034.90371757, 14.27495244, 0.18199196, 100.29282654, 0.13024619,
                            -0.00012452, 0.06064060, -0.35635438, 38.35125000)

saturn_orbit = Orbit.Orbit(9.54149883, -0.00003065, 0.05550825, -0.00032044, 2.49424102, 0.00451969,
                           50.07571329, 1222.11494724, 92.86136063, 0.54179478, 113.63998702, -0.25015002,
                           0.00025899, -0.13434469, 0.87320147, 38.35125000)

uranus_orbit = Orbit.Orbit(19.18797948, -0.00020455, 0.04685740, -0.00001550, 0.77298127, -0.00180155,
                           314.20276625, 428.49512595, 172.43404441, 0.09266985, 73.96250215, 0.05739699,
                           0.00058331, -0.97731848, 0.17689245, 7.67025000)

neptune_orbit = Orbit.Orbit(30.06952752, 0.00006447, 0.00895439, 0.00000818, 1.77005520, 0.00022400,
                            304.22289287, 218.46515314, 46.68158724, 0.01009938, 131.78635853, -0.00606302
                            - 0.00041348, 0.68346318, -0.10162547, 7.67025000)

mercury = Body("Mercury", mercury_orbit, "darkgoldenrod", 7)
venus = Body("Venus", venus_orbit, "bisque", 10)
earth = Body("Earth", earth_orbit, "skyblue", 10)
mars = Body("Mars", mars_orbit, "orangered", 9)
jupiter = Body("Jupiter", jupiter_orbit, "sandybrown", 20)
saturn = Body("Saturn", saturn_orbit, "darkkhaki", 15)
uranus = Body("Uranus", uranus_orbit, "lightcyan", 13)
neptune = Body("Neptune", neptune_orbit, "royalblue", 15)

rocky_planets = [mercury, venus, earth, mars]
gas_giants = [jupiter, saturn, uranus, neptune]
solar_system = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]