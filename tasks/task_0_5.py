def area(side1, side2, side3):
     semi_perimeter = 0.5 * (side1 + side2 + side3) 
     return (semi_perimeter * ((semi_perimeter - side1) * (semi_perimeter-side2) * (semi_perimeter-side3))) **0.5