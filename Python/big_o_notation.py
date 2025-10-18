# TIME COMPLEXITY

# O(n)
def get_squared_numbers(numbers):
    squared_numbers = []
    
    for n in numbers:
        squared_numbers.append(n*n)
     
    print(squared_numbers)   
    # return squared_numbers        


numbers = [2,3,5,34,4,3,2,34]
get_squared_numbers(numbers)

# O(n*2)

def get_duplicate(numbers):
    duplicate = []
    
    for i in range(len(numbers)):
        for j in range((i+1), len(numbers)):
            if numbers[i] == numbers[j]:
                duplicate.append(numbers[i])
                
    print(duplicate)                        
    return duplicate
            
get_duplicate(numbers)            