
north_int = int(input("Number of cars travelling north: "))
south_int = int(input("Number of cars travelling south: "))
east_int = int(input("Number of cars travelling east: "))
west_int = int(input("Number of cars travelling west: "))


while True:
    cars_total = 0
    
    cars_total = north_int + south_int + west_int + east_int
    n_and_s_total = north_int + south_int
    w_and_e_total = west_int + east_int
    
    if n_and_s_total > 0 or w_and_e_total > 0:
        if n_and_s_total >= w_and_e_total:
            print('Green light on N/S')
            north_int -= 5
            
            if north_int < 0:
                
                north_int = 0
            
            south_int -= 5
            
            if south_int < 0:
                south_int = 0
            
            

        else:
            print('Green light on E/W')
            west_int -= 5
            if west_int < 0:
                west_int = 0
            
            east_int -= 5
            if east_int < 0:
                east_int = 0
        
        
    else: 
        if cars_total == 0:
            print('No cars waiting, the traffic jam has been solved!')
            break
    



    










