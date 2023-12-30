import math

def find_angle(ab, bc):
    angle_rad = math.atan2(ab, bc)
    angle_deg = math.degrees(angle_rad)
    rounded_angle = round(angle_deg)
    return rounded_angle

if __name__ == '__main__':
    ab = float(input())
    bc = float(input())
    
    angle = find_angle(ab, bc)
    
    print(f"{angle}\u00b0")
