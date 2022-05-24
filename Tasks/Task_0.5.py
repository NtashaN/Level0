def area(side1, side2, side3):
     #Heron's Formula
     sp = 0.5 * (side1 + side2 + side3) 
     return (sp * ((sp - side1) * (sp-side2) * (sp-side3))) **0.5