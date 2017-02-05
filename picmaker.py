image = open("carpet.ppm", "w")
string = "P3 729 729 256 \n"

def incarpet(i, j, n):
    third = n/3
    if third == 0:
        return False
    if i >= (third) and i < (2*third) and j >= (third) and j < (2*third):
        return True
    return incarpet(i%third, j%third, third)

for i in range(729):
    for j in range(729):
        if incarpet(i,j, 729) == True:
            string += "%d %d %d\n" % (255, 255, 255)
        else:
            string += "%d %d %d\n" % (i/3, 100, j/3)
            
image.write(string)            

 
