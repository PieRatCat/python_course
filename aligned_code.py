import re

def align_comments(code, column=80):
    lines = code.split('\n')
    aligned_lines = []
    
    for line in lines:
        if '#' in line:
            code_part, comment_part = line.split('#', 1)
            code_part = code_part.rstrip()
            spaces_needed = column - len(code_part) - 1
            if spaces_needed > 0:
                aligned_line = f"{code_part} {' ' * spaces_needed}# {comment_part.strip()}"
            else:
                aligned_line = f"{code_part} # {comment_part.strip()}"
        else:
            aligned_line = line
        aligned_lines.append(aligned_line)
    
    return '\n'.join(aligned_lines)

# Example usage
code = """
class FruitProduct:
    \"\"\"A class representing fruit products in a grocery store.\"\"\"
    
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

swedish_apples = FruitProduct(52, 1) # Create an instance of Fruit Product

print(FruitProduct.__doc__) # Print the docstring of the class
print("Price: ", swedish_apples.price, ", Quantity: ", swedish_apples.quantity) # Print the attributes of the instance
print(type(swedish_apples)) # Print the type of the instance
print(isinstance(swedish_apples, FruitProduct)) # Check if the instance is of the class FruitProduct
"""

aligned_code = align_comments(code, column=80)
print(aligned_code)