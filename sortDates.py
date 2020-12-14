class dateSorter: 
    mode = input("Enter a mode (ASC/DEC): ")  
    one = input("Type in a date (DD-MM-YYYY_HH:MM): ")
    two = input("Type in a date (DD-MM-YYYY_HH:MM): ")
    three = input("Type in a date (DD-MM-YYYY_HH:MM): ")
    if mode == "ASC":
            if int(one[6:10]) < int(two[6:10]) and int(one[6:10]) < int(three[6:10]):
                print(one, ", ")
                if int(two[6:10]) < int(three[6:10]):
                    print(two, ", ", three)
                else:
                    print(three, ", ", two)
            elif int(two[6:10]) < int(one[6:10]) and int(two[6:10]) < int(three[6:10]):
                    print(two, ", ")
                    if int(one[6:10]) < int(three[6:10]):
                        print(one, ", ", three)
                    else:
                        print(three, ", ",one)
            elif int(three[6:10]) < int(one[6:10]) and int(three[6:10]) < int(two[6:10]):
                    print(three, ", ")
                    if int(one[6:10]) < int(two[6:10]):
                        print(one, ", ", two)
                    else:
                        print(two, ", ", one)
            elif int(one[6:10]) == int(two[6:10]) or int(one[6:10]) == int(three[6:10]):
                    if int(one[3:5]) < int(two[3:5]) and int(one[3:5]) < int(two[3:5]):
                        print(one, ", ")
                        if int(two[3:5]) < int(three[3:5]):
                            print(two, ", ", three)
                        else:
                            print(three, ", ", two)
                    if int(two[3:5]) < int(one[3:5]) and int(two[3:5]) < int(three[3:5]):
                        print(two, ", ")
                        if int(one[3:5]) < int(three[3:5]):
                            print(one, ", ", three)
                        else:
                            print(three, ", ",one)
                    if int(three[3:5]) < int(one[3:5]) and int(three[3:5]) < int(two[3:5]):
                        print(three, ", ")
                        if int(one[3:5]) < int(two[3:5]):
                            print(one, ", ", two)
                        else:
                            print(two, ", ", one)
            elif int(one[3:5]) == int(two[3:5]) or int(one[3:5]) == int(three[3:5]):
                    if int(one[0:2]) < int(two[0:2]) and int(one[0:2]) < int(two[0:2]):
                            print(one, ", ")
                            if int(two[0:2]) < int(three[0:2]):
                                print(two, ", ", three)
                            else:
                                print(three, ", ", two)
                    if int(two[0:2]) < int(one[0:2]) and int(two[0:2]) < int(three[0:2]):
                            print(two, ", ")
                            if int(one[0:2]) < int(three[0:2]):
                                print(one, ", ", three)
                            else:
                                print(three, ", ",one)
                    if int(three[0:2]) < int(one[0:2]) and int(three[0:2]) < int(two[0:2]):
                            print(three, ", ")
                            if int(one[0:2]) < int(two[0:2]):
                                print(one, ", ", two)
                            else:
                                print(two, ", ", one)                   
    if mode == "DEC":
            if int(one[6:10]) > int(two[6:10]) and int(one[6:10]) > int(three[6:10]):
                print(one, ", ")
                if int(two[6:10]) > int(three[6:10]):
                    print(two, ", ", three)
                else:
                    print(three, ", ", two)
            elif int(two[6:10]) > int(one[6:10]) and int(two[6:10]) > int(three[6:10]):
                    print(two, ", ")
                    if int(one[6:10]) > int(three[6:10]):
                        print(one, ", ", three)
                    else:
                        print(three, ", ",one)
            elif int(three[6:10]) > int(one[6:10]) and int(three[6:10]) > int(two[6:10]):
                    print(three, ", ")
                    if int(one[6:10]) > int(two[6:10]):
                        print(one, ", ", two)
                    else:
                        print(two, ", ", one)
            elif int(one[6:10]) == int(two[6:10]) or int(one[6:10]) == int(three[6:10]):
                    if int(one[3:5]) > int(two[3:5]) and int(one[3:5]) > int(two[3:5]):
                        print(one, ", ")
                        if int(two[3:5]) > int(three[3:5]):
                            print(two, ", ", three)
                        else:
                            print(three, ", ", two)
                    if int(two[3:5]) > int(one[3:5]) and int(two[3:5]) > int(three[3:5]):
                        print(two, ", ")
                        if int(one[3:5]) > int(three[3:5]):
                            print(one, ", ", three)
                        else:
                            print(three, ", ",one)
                    if int(three[3:5]) > int(one[3:5]) and int(three[3:5]) > int(two[3:5]):
                        print(three, ", ")
                        if int(one[3:5]) > int(two[3:5]):
                            print(one, ", ", two)
                        else:
                            print(two, ", ", one) 
            elif int(one[3:5]) == int(two[3:5]) or int(one[3:5]) == int(three[3:5]):
                    if int(one[0:2]) > int(two[0:2]) and int(one[0:2]) > int(two[0:2]):
                            print(one, ", ")
                            if int(two[0:2]) > int(three[0:2]):
                                print(two, ", ", three)
                            else:
                                print(three, ", ", two)
                    if int(two[0:2]) > int(one[0:2]) and int(two[0:2]) > int(three[0:2]):
                            print(two, ", ")
                            if int(one[0:2]) > int(three[0:2]):
                                print(one, ", ", three)
                            else:
                                print(three, ", ",one)
                    if int(three[0:2]) > int(one[0:2]) and int(three[0:2]) > int(two[0:2]):
                            print(three, ", ")
                            if int(one[0:2]) > int(two[0:2]):
                                print(one, ", ", two)
                            else:
                                print(two, ", ", one)    
