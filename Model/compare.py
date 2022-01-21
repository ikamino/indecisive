
class Compare:

    def cmp (self, rest_list):
        end = 0
        curr = 1
        which_chose = 0
        orig_list = rest_list
        yes_list = []
        a = orig_list[0]
        b = orig_list[1]
        yes_list.append(a["name"])
        yes_list.append(b["name"])
        for i in range(len(rest_list) - 1):
            rest1 = yes_list[0]
            rest2 = yes_list[1]

            print("What would you rather eat? " + rest1 + " or " + rest2 + "? (Input 1 or 2 for options) Type 3 to let us choose based on what you've picked so far")
            answer = input()
       
            if((len(orig_list) -1) != curr):
                curr += 1
            
            if (answer == "1"):
                yes_list.remove(rest2)
                # curr += 1
                which_chose = 1
                a = orig_list[curr]
                yes_list.insert(1, a["name"])
                
            elif (answer == "2"):
                yes_list.remove(rest1)
                # curr += 1
                which_chose = 2
                a = orig_list[curr]
                yes_list.insert(0, a["name"])
            elif (answer == "3"):
                if (curr != 0): 
                    break
            else: 
                yes_list.remove(rest1)
                # curr += 1
                which_chose = 2
                a = orig_list[curr]
                yes_list.insert(0, a["name"])
               
        chosen = ""
        if(which_chose == 1):
            chosen = yes_list[0]
        elif (which_chose == 2):
            chosen = yes_list[1]
            
        print("You have chosen: " + chosen + "!")


    def __init__(self, rest_list):
        self.cmp(rest_list)



