def sort_package(width, height, length, mass):
     
    if any(dim < 0 for dim in (width, height, length)) or mass < 0: # validating the input / Edge cases
        return "INVALID"  
    volume = width * height * length
    
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20
    
    if is_bulky and is_heavy:
        return "REJECTED"  # heavy and bulky
    elif is_bulky or is_heavy:
        return "SPECIAL"  # heavy or bulky
    else:
        return "STANDARD"  # heavy nor bulky
    
test_cases = [
    (50, 40, 500, 10),   
    (150, 40, 30, 25),   
    (100, 100, 100, 22),  
    (150, 150, 150, 25),  
    (80, 60, 30, 15),   
    (100, 100, 100, 20),  
    (150, 20, 20, 5),     
    (1, 1, 1, 0),       
    (0, 0, 0, 0),         
 
]

# this to run the test cases above and dispaly
for i, (w, h, l, m) in enumerate(test_cases):
    result = sort_package(w, h, l, m)
    print(f"Test case {i + 1}: package dimension: ({w}, {h}, {l}, {m}) = '{result}'")