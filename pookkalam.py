# Submission - Code A Pookkalam
#
# Author: Adityakrishnan
# Organisation: Christ College of Engineering, Irinjalakuda
#
# This Pookkalam is divided into 10 Parts
#
# (i) Boundary Circles     (ii) 5 Colored Spiral Design
# (iii) Outer Spokes       (iv) Center Octagon
# (v) Outer Diamonds       (vi) Circle Flower
# (vii) Ellipse Flower     (viii) Inner Circle
# (ix) Inner Spokes        (x) Center Square Design


# <--- Basic Funtions ---> #

def Square(h, w, color, stroke):
    sq = rectangle(x=0, y=0, h=h, w=w, stroke_width=2, stroke=stroke, fill=color)
    return sq

def CCircle(x, y, r, color, stroke):
    cir = circle(x=x, y=y, r=r, fill=color, stroke=stroke)
    return cir

def CenterSpoke(color):
    s1 = point(0, 0)
    s2 = point(-15, 44)
    s3 = point(-44, 15)
    ccolor = color
    center_spoke = polygon([s1, s2, s3], fill=ccolor, stroke="none") + CCircle(-31, 31, 20, ccolor, "none")
    return center_spoke

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


# (i) Boundary Circle (x3)

outer_c1 = circle(x=0, y=0, stroke_width=3, r=152, fill="white", stroke="#9400D3")
outer_c2 = circle(x=0, y=0, stroke_width=0, r=150, fill="white")
outer_c3 = circle(x=0, y=0, stroke_width=2, r=147, fill="black")

outer_final = outer_c1 + outer_c2 + outer_c3
show(outer_final)


# (ii) Colored Design Spiral (x5)

des_spiral1 = rectangle(w=209, h=209, fill="red", stroke="none") | repeat(36, rotate(10))
des_spiral2 = rectangle(w=193, h=193, fill="orange", stroke="none") | rotate(15) | repeat(36, rotate(10))
des_spiral3 = rectangle(w=178, h=178, fill="#FFD700", stroke="none") | rotate(0) | repeat(36, rotate(10))
des_spiral4 = rectangle(w=165, h=165, fill="yellow", stroke="none") | rotate(15) | repeat(36, rotate(10))
des_spiral5 = rectangle(w=153, h=153, fill="black", stroke="none") | rotate(0) | repeat(15, rotate(10))

show(des_spiral1, des_spiral2, des_spiral3, des_spiral4, des_spiral5)


# (iii) Outer Spokes (x8)

os1 = point(0, 175)
os2 = point(20, 135)
os3 = point(-20, 135)

tria1 = polygon([os1, os2, os3], fill="#32CD32", stroke="green")
tria2 = CCircle(0, 135, 22, "#32CD32", "none")
tria3 = CCircle(0, 160, 1, "purple", "white") 
triain1 = polygon([os1, os2, os3], fill="#006400", stroke="white")
triain2 = CCircle(0, 135, 20, "#32CD32", "none")
triain3 = CCircle(0, 160, 1, "purple", "white") 

tria = tria1 + tria2 + tria3 | repeat(8, rotate(45))
triain = triain1 + triain2 + triain3 | repeat(8, rotate(45))

triaf = tria | scale(0.80)
triainf = triain | scale(0.75)
show(triaf, triainf)


# (iv) Center Octagon

deep_rectangle = Square(80, 197, "white", "none") | (rotate(22))
deeprf = deep_rectangle | repeat(4, rotate(45))
show(deeprf)


# (v) Outer Diamonds (x8)

d1 = point(0, 115)
d2 = point(5, 105)
d3 = point(0, 95)
d4 = point(-5, 105)

diamond = polygon([d1, d2, d3, d4], fill="#4B0082", stroke="none")
diamondf = diamond | repeat(8, rotate(45))
show(diamondf)


# (vi) Circle Flower

cradius = 47
cf1 = CCircle(-45, 20, cradius, "#FFE4B5", "none")
cf2 = CCircle(-45, 20, cradius-8, "#BA55D3", "none")
cf3 = CCircle(-45, 20, cradius-16, "#9400D3", "none")
cf4 = CCircle(-45, 20, cradius-24, "#4B0082", "none")

circle_flower = cf1 + cf2 + cf3 + cf4
deepcf = circle_flower | repeat(8, rotate(45)) | rotate(-65)
show(deepcf)


# (vii) Ellipse Flower

cradius = 47
ef1 = CEllipse("#FFE4B5", "none")
ef2 = CEllipse("#4B0082", "none") | scale(0.9)
ef3 = CEllipse("#9400D3", "none") | scale(0.8)
ef4 = CEllipse("#BA55D3", "none") | scale(0.73)

ellipse_flower = ef1 + ef2 + ef3 + ef4
deepcf = ellipse_flower | repeat(4, rotate(45)) | rotate(-68)
show(deepcf)


# (viii) Inner Circle

ic1 = CCircle(0, 0, 63, "white", "white")
ic2 = CCircle(0, 0, 55, "yellow", "yellow")
ic3 = CCircle(0, 0, 45, "#FFD700", "#FFD700")
ic4 = CCircle(0, 0, 35, "orange", "orange")
ic5 = CCircle(0, 0, 25, "red", "red")
ic6 = CCircle(0, 0, 15, "black", "black")
ic7 = CCircle(0, 0, 10, "#4B0082", "none")

inner_circle = ic1 + ic2 + ic3 + ic4 + ic5 + ic6 + ic7
show(inner_circle)


# (ix) Inner Spoke (x6)

is1 = CenterSpoke("black") | scale(1)
is2 = CenterSpoke("red") | scale(0.87)
is3 = CenterSpoke("orange") | scale(0.73)
is4 = CenterSpoke("#FFD700") | scale(0.60)
is5 = CenterSpoke("yellow") | scale(0.45)
is6 = CenterSpoke("white") | scale(0.32)

inner_spoke = is1 + is2 + is3 + is4 + is5 + is6
centerspokef = inner_spoke | repeat(5, rotate(72)) | rotate(-10)
show(centerspokef)


# (x) Center Square Design

square_design = Square(25, 25, "#4B0082", "white") | repeat(40, rotate(20) | scale(0.9))
show(square_design)


# <--- Happy Onam 2k21 ---> #
