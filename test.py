#Using glowscript, https://trinket.io/glowscript/, and the following code you get a model of the moon orbiting the earth. need to integrate glowscript, vpython, into vis studio code
GlowScript 2.9 VPython
tgraph=graph(xtitle="Time [s]",ytitle="y-momentum [kg*m/s]")
Fe=gcurve(color=color.blue, label="Earth")
Fm=gcurve(label="moon")
scene.lights=[distant_light(direction=vector(0,1,0), color=vector(1,1,1))]
RE=6.371e6
ME=5.972e24
G=6.67e-11
RM=1.7371e6
MM=7.348e22
REM=384400e3
earth=sphere(pos=vector(-REM/2,0,0),radius=RE,texture=textures.earth, make_trail=True)
moon=sphere(pos=vector(REM/2,0,0), radius=RM, texture=textures.stucco, make_trail=True)
moon.m=MM
moon.p=moon.m*vector(0,1000,0)
earth.m=ME
#earth.p=earth.m*vector(0,0,0)
earth.p=-moon.p
t=0
dt=100
while t<1e6:
  rate(1000)
  r=moon.pos-earth.pos
  F=-G*earth.m*moon.m*norm(r)/mag(r)**2
  moon.p=moon.p+F*dt
  earth.p=earth.p-F*dt
  moon.pos=moon.pos+moon.p*dt/moon.m
  earth.pos=earth.pos+earth.p*dt/earth.m
  Fe.plot(t,earth.p.y)
  Fm.plot(t,moon.p.y)
  #Fe.plot(earth.pos.x, earth.pos.y)
  t=t+dt