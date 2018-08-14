def is_inside(point, shape):
    if shape[0] <= point[0] <= (shape[0]+shape[2]):
        return True
    elif shape[1] <= point[1] <= (shape[1]+shape[3]):
        return True
    else:
        return False

if is_inside([200, 120], [140, 60, 100, 200]):
    print("Your code is correct")
else:
    print("Why bug why")