# Submission - Code A Pookkalam
#
# Author: Adityakrishnan
# Organisation: Christ College of Engineering, Irinjalakuda
#
# This Pookkalam is divided into 12 Parts
#
# (i) Boundary Circles          (ii) 5 Colored Spiral Design
# (iii) Outer Spokes            (iv) Outer Spiral Round
# (v) Center Octagon            (vi) Outer Diamonds
# (vii) Circle Flower           (viii) Ellipse Flower
# (ix) Inner Circle             (x) Inner Spokes
# (xi) Center Square Design     (xii) Center Theme


# <--- Basic Funtions ---> #

def CRectangle(h, w, color, stroke):
    sq = rectangle(x=0, y=0, h=h, w=w, stroke_width=2, stroke=stroke, fill=color)
    return sq

def CCircle(x, y, r, color, stroke):
    cir = circle(x=x, y=y, r=r, fill=color, stroke=stroke)
    return cir

def CenterSpoke(color):
    cs = point(0, 0)
    cs11 = point(-25, 44)
    cs12 = point(-59, 30)
    cs21 = point(-44, 25)
    cs22 = point(-30, 59)
    ccolor = color
    center_spoke1 = polygon([cs, cs11, cs12], fill=ccolor, stroke="none")
    center_spoke2 = polygon([cs, cs21, cs22], fill=ccolor, stroke="none")
    center_circle = CCircle(-31, 31, 20, ccolor, "none")
    return center_spoke1 + center_spoke2 + center_circle

def Triangle(color):
    s1 = point(0, 0)
    s2 = point(-30, 55)
    s3 = point(-55, 30)
    ccolor = color
    center_spoke = polygon([s1, s2, s3], fill=ccolor, stroke="none")
    return center_spoke

def CEllipse(color, stroke):
    elli = ellipse(0, 0, 60, 190, fill=color, stroke=stroke)
    return elli

# (i) Boundary Circle (x3) | Outer Circle (oc)

    #initialising 3 boundary circles
oc1 = circle(x=0, y=0, stroke_width=4, r=150, fill="white", stroke="#9400D3")
oc2 = circle(x=0, y=0, stroke_width=0, r=150, fill="white")
oc3 = circle(x=0, y=0, stroke_width=2, r=146, fill="black")
    #combining circles
boundary_circle = oc1 + oc2 + oc3
show(boundary_circle)


# (ii) 5 Colored Design Spiral (x5) | Design Spiral (ds)

    #initialising 5 rectangles and repeated rotation
ds1 = CRectangle(203, 203, "red", "none") | repeat(36, rotate(10))
ds2 = CRectangle(193, 193, "orange", "none") | rotate(15) | repeat(36, rotate(10))
ds3 = CRectangle(178, 178, "#FFD700", "none") | rotate(0) | repeat(36, rotate(10))
ds4 = CRectangle(168, 168, "yellow", "none") | rotate(15) | repeat(36, rotate(10))
ds5 = CRectangle(153, 153, "white", "none") | rotate(0) | repeat(36, rotate(10))
    #combining 5 rectangles
design_spiral = ds1 + ds2 + ds3 + ds4 + ds5
show(design_spiral)

# (iii) Outer Spokes (x12) | Outer Spokes (os) | triangle (tria) | final(triaf)

    #points for spokes
os1 = point(0, 140)
os2 = point(10, 130)
os3 = point(5, 115)
os4 = point(-5, 115)
os5 = point(-10, 130)
    #joining the points
tria1 = polygon([os1, os2, os3, os4, os5], fill="white", stroke="none")
tria2 = polygon([os1, os2, os3, os4, os5], fill="#32CD32", stroke="none")
tria3 = polygon([os1, os2, os3, os4, os5], fill="#228B22", stroke="none")
tria4 = polygon([os1, os2, os3, os4, os5], fill="#008000", stroke="none")
    #repeated rotation and scaling for filling circle
triaf1 = tria1  | repeat(12, rotate(30))
triaf2 = tria2 | repeat(12, rotate(30)) | scale(0.95)
triaf3 = tria3 | repeat(12, rotate(30)) | scale(0.90)
triaf4 = tria4 | repeat(12, rotate(30)) | scale(0.85)
    #combining shapes
outer_spoke = triaf1 + triaf2 + triaf3 + triaf4
show(outer_spoke)

#(iv) Outer Spiral Round (x12)

    #initializing circles | repeating and rotating it simultaneously with 2 different colours
desc = circle(x=0, y=110, r=50, fill="#4B0082", stroke="white", stroke_width=5) | repeat(36*4, rotate(10)|scale(0.97))
desa = circle(x=0, y=110, r=50, fill="#4B0082", stroke="white", stroke_width=5) | repeat(36*4, rotate(-10)|scale(0.97))
descb = circle(x=0, y=110, r=50, fill="#0000CD", stroke="white", stroke_width=5) | repeat(36*4, rotate(10)|scale(0.97))
desab = circle(x=0, y=110, r=50, fill="#0000CD", stroke="white", stroke_width=5) | repeat(36*4, rotate(-10)|scale(0.97))
    #scaling, translatig,  Rotating as to fill circle
des2 = desc | scale(0.13) | translate(111.5, -35) | rotate(120)
des3 = desa | scale(0.13) | translate(-111.5, -35) | rotate(-120)
des2b = descb | scale(0.13) | translate(111.5, -35) | rotate(120)
des3b = desab | scale(0.13) | translate(-111.5, -35) | rotate(-120)
    #combining the outputs
des23f = des2 + des3
des23fb = des2b + des3b
    #repeated rotation
des6 = des23f | repeat(3, rotate(120))
des7 = des23fb | repeat(3, rotate(120)) | rotate(60)
show(des7 + des6)

#(v) Center Octagon

    #initializing rectangle and rotating it 4 times
deep_rectangle = CRectangle(80, 197, "black", "none") | (rotate(22))
center_octagon = deep_rectangle | repeat(4, rotate(45))
show(center_octagon)

#(vi) Outer Diamonds (x8) | Diamond (d)

    #points for a diamond
d1 = point(0, 113)
d2 = point(5, 108)
d3 = point(0, 95)
d4 = point(-5, 108)
    #joining the points repeated rotation for circle
diamonds = polygon([d1, d2, d3, d4], fill="#00FF00", stroke="none")
outer_diamonds = diamonds | repeat(12, rotate(30))
show(outer_diamonds)

#(vii) Circle Flower (cf)

    #initializing 4 circles
cradius = 47
cf1 = CCircle(-45, 20, cradius, "white", "none")
cf2 = CCircle(-45, 20, cradius-8, "#000080", "none")
cf3 = CCircle(-45, 20, cradius-16, "#0000CD", "none")
cf4 = CCircle(-45, 20, cradius-24, "#1E90FF", "none")
    #repeated rotation for circular appearance
circle_flower = cf1 + cf2 + cf3 + cf4
deepcf = circle_flower | repeat(8, rotate(45)) | rotate(-65)
show(deepcf)

#(viii) Ellipse Flower (ef)

    #initializing 4 ellipses
cradius = 47
ef1 = CEllipse("#FFE4B5", "none")
ef2 = CEllipse("#4B0082", "none") | scale(0.9)
ef3 = CEllipse("#9400D3", "none") | scale(0.8)
ef4 = CEllipse("#BA55D3", "none") | scale(0.73)
    #repeated rotation for circular appearance
ellipse_flower = ef1 + ef2 + ef3 + ef4
deepcf = ellipse_flower | repeat(4, rotate(45)) | rotate(-68)
show(deepcf)

#(ix) Inner Circle (ic)

    #initializing 7 circles
ic1 = CCircle(0, 0, 63, "white", "none")
ic2 = CCircle(0, 0, 58, "yellow", "none")
ic3 = CCircle(0, 0, 50, "orange", "none")
ic4 = CCircle(0, 0, 38, "white", "none")
ic5 = CCircle(0, 0, 28, "red", "none")
ic6 = CCircle(0, 0, 40, "black", "none")
ic7 = CCircle(0, 0, 20, "#4B0082", "none")
    #combining 7 circles
inner_circle = ic1 + ic2 + ic3 + ic4 + ic5 + ic6 + ic7
show(inner_circle)

#(x) Inner Spoke (x6) | Inner Spoke (is)

    #initializing 6 circles
is1 = CenterSpoke("black") | scale(1)
is2 = CenterSpoke("red") | scale(0.87)
is3 = CenterSpoke("orange") | scale(0.73)
is4 = CenterSpoke("#FFD700") | scale(0.60)
is5 = CenterSpoke("yellow") | scale(0.45)
is6 = CenterSpoke("white") | scale(0.32)
    #repeated rotation and scaling for a decreasing spoke
inner_spoke = is1 + is2 + is3 + is4 + is5 + is6
centerspokef = inner_spoke | repeat(6, rotate(60)) | rotate(-20) | scale(0.93)
show(centerspokef)

#(xi) Center Square Design | Square Design (sd)

    #initializing rectangle
sd = CRectangle(50, 50, "#4B0082", "white")
square_designf = sd | repeat(40, rotate(20) | scale(0.9))
show(square_designf)

#(xii) Center Theme

    #initializing background
cdes = CCircle(0, 0, 22, "white", "none")
show(cdes)
    #points for vanji(boat)
tp1 = point(-20, 10)
tp2 = point(-20, 0)
tp3 = point(20, 0)
tp4 = point(40, 40)
tp5 = point(10, 25)
tp6 = point(25, 25)
tp7 = point(15, 10)
l1 = line(x1=-10, y1= 15, x2=10, y2=-10, stroke="black")
l2 = l1 | translate(10, 0)
    #initializing orange background and sun
bg = CCircle(0, 0, 20, "orange", "yellow")
show(bg)
sun = CCircle(-2,-2, 5, "#FFD700", "yellow") | translate(5, 10)
show(sun)
    #joining dots for vanji(boat)
tpf = polygon([tp1, tp2, tp3, tp4, tp5, tp6, tp7], fill = "black")
theme = tpf + l1 + l2 | scale(0.5) | translate(-5, -6)
    #scaling, translating and combining
themef = theme | scale(0.95)
final =  themef | scale(1.1) | translate(-1, -3)
show(final)


# <--- Happy Onam 2k21 ---> #
