#Basic Funtions
def Square(h, w, color, stroke):
    sq = rectangle(x =0, y =0, h = h, w= w, stroke_width = 2, stroke= stroke, fill = color)
    return sq

def CCircle(x, y, r, color, stroke):
    cir = circle(x = x, y= y, r=r, fill = color, stroke = stroke)
    return cir

def CenterSpoke(color):
    s1 = point(0, 0)
    s2 = point(-15, 44)
    s3 = point(-44, 15)
    ccolor = color
    center_spoke = polygon([s1, s2, s3], fill = ccolor, stroke= "none") + CCircle(-31, 31, 20, ccolor, "none")
    return center_spoke

def Triangle(color):
    s1 = point(0, 0)
    s2 = point(-30, 55)
    s3 = point(-55, 30)
    ccolor = color
    center_spoke = polygon([s1, s2, s3], fill = ccolor, stroke= "none") 
    return center_spoke

def CEllipse(color, stroke):
    elli = ellipse(0, 0, 60, 190, fill = color, stroke = stroke)
    return elli
    
#Outer Circle
p1 = point(-50, 50)
p2 = point(-120, 90)
p3 = point(-90, 120)

tria = polygon([p1, p2, p3], fill = "#32CD32", stroke = "#32CD32") | repeat(8, rotate(45))
triain = polygon([p1, p2, p3], fill = "	#008000", stroke = "green") | repeat(8, rotate(45))
triainin = polygon([p1, p2, p3], fill = "#006400", stroke = "green") | repeat(8, rotate(45))

triaf = tria | scale(0.80)
triainf = triain | scale(0.75)
triaininf = triainin | scale(0.70)

outer_c = circle(x=0, y=0, stroke_width = 3, r= 152, fill = "white", stroke = "#9400D3") + circle(x=0, y=0, stroke_width = 0, r= 150, fill=color(r=255, g=255, b=255, a=0.6)) + circle(x=0, y=0, stroke_width = 2, r= 147, fill = "black") 
 


show(outer_c)

#Design Spiral
des_spiral1 = rectangle(w=209,h=209,fill="red", stroke = "none") |repeat (36,rotate(10))
des_spiral2 = rectangle(w=193,h=193,fill="orange", stroke = "none")|rotate(15) | repeat (36,rotate(10))
des_spiral3 = rectangle(w=178,h=178,fill="#FFD700", stroke = "none")|rotate(0) | repeat (36,rotate(10))
des_spiral4 = rectangle(w=165,h=165,fill="yellow", stroke = "none")|rotate(15) | repeat (36,rotate(10))
des_spiral5 = rectangle(w=153,h=153,fill="black", stroke = "none")|rotate(0) | repeat (15,rotate(10))
#middle layer

show(des_spiral1, des_spiral2, des_spiral3, des_spiral4, des_spiral5 )
show(triaf, triainf, triaininf)


# #Inner Square

# inner_square = Square(0, 0, 197, 197, "none", "red") | repeat(2, rotate(45)) 
# inner_squaref = inner_square | rotate(22)
# # innner_square2 = InnerSquare(0, 0, 250, 250) | rotate(-45)
# #show(inner_squaref)

#Deepest Rectangle * 3

deep_rectangle = Square(80, 197, "white", "none") | (rotate(22))
deeprf = deep_rectangle | repeat(4, rotate(45))
show(deeprf)

#Diamonds * 8
d1 = point(0, 115)
d2 = point(5, 105)
d3 = point(0, 95)
d4 = point(-5, 105)
diamond = polygon([d1, d2, d3, d4], fill = "#4B0082", stroke ="none")
diamondf = diamond | repeat(8, rotate(45))
show(diamondf)


#Deepest Circle * 8
cradius = 47
deep_circle = CCircle(-45, 20, cradius, "#FFE4B5", "none") + CCircle(-45, 20, cradius-8, "#BA55D3", "none") + CCircle(-45, 20, cradius -16, "#9400D3", "none")+  CCircle(-45, 20, cradius-24, "#4B0082", "none")
deepcf = deep_circle | repeat(8, rotate(45)) | rotate(-65)

show(deepcf)


#Deepest Ellipse * 4
cradius = 47
deep_ellipse1 = CEllipse("#FFE4B5", "none")
deep_ellipse2 = CEllipse("#4B0082", "none") | scale(0.9)
deep_ellipse3 = CEllipse("#9400D3", "none") | scale(0.8)
deep_ellipse4 = CEllipse("#BA55D3", "none") | scale(0.73)

deep_ellipse = deep_ellipse1 + deep_ellipse2 + deep_ellipse3 + deep_ellipse4
deepcf = deep_ellipse | repeat(4, rotate(45)) | rotate(-68)

show(deepcf)




#Center Circle
center_circle = CCircle(0, 0, 63, "white", "white" ) + CCircle(0, 0, 55, "yellow", "yellow") + CCircle(0, 0, 45,  "#FFD700", "#FFD700") + CCircle(0, 0, 35, "orange", "orange") + CCircle(0, 0, 25, "red", "red") + CCircle(0, 0, 15, "black", "black") + CCircle(0, 0, 10, "#4B0082", "none")
show(center_circle)

#Middle Grill
grill = ellipse(x=0, y=0, w=120, h=30, stroke_weight=5, stroke="black") | repeat(20, rotate(18)) | rotate(10)
show(grill)

#Center Spokes * 5

centersw = CenterSpoke("black") | scale(1)
centersy = CenterSpoke("red") | scale(0.87)
centersg = CenterSpoke("orange") | scale(0.73)
centerso = CenterSpoke("#FFD700") | scale(0.60)
centersr = CenterSpoke("yellow") | scale(0.45)
centersb = CenterSpoke("white") | scale(0.30)
centerspoke = centersw + centersy + centersg + centerso + centersr + centersb
centerspokef = centerspoke | repeat(5, rotate(72)) | rotate(-10)
show(centerspokef)

# centersw = Triangle("white") | scale(1)
# centersy = Triangle("yellow") | scale(0.834)
# centersg = Triangle("#FFD700") | scale(0.668)
# centerso = Triangle("orange") | scale(0.502)
# centersr = Triangle("red") | scale(0.336)
# centersb = Triangle("black") | scale(0.17)
# centerspoke = centersw + centersy + centersg + centerso + centersr + centersb
# centerspokef = centerspoke | repeat(4, rotate(90))
# show(centerspokef)

#Middle Square Round
middle_square = Square(25, 25, "#4B0082", "white") | repeat(40, rotate(20) | scale(0.9))
show(middle_square)
