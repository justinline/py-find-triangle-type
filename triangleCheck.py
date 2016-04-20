# Script to check the angle of a triangle given the 3 lengths as integers. 

def triangle_type(a,b,c):
    # Sort given lengths
    ordered = sorted([a,b,c])
    x,y,z = ordered[0], ordered[1], ordered[2]


    compare = (x ** 2) + (y ** 2)
    # Check whether Triangle Exists
    while ((x + y) > z):
        # Use Cosine rule to check angle type
        if (z ** 2) < compare:
            return "Acute"
        elif (z ** 2) > compare:
            return "Obtuse"
        elif (z ** 2) == compare:
            return "Right Angle"
    # If triangle isn't possible
    return "Triangle cannot be made with given sides"