def addNumbers( number ):
    if number == 1:
        return 1
    else:
        return addNumbers( (number - 1) ) + (number)
            
            
    
def main():
    
    x = addNumbers( 100 )
    print x
    
main()