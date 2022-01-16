from APIdict import rest_info_list


class compare:

    def cmp (self, rest_list):
        end = 0
        curr = 1
        which_chose = 0
        orig_list = rest_list
        yes_list = []
        yes_list.append(orig_list[0])
        yes_list.append(orig_list[1])
        for i in range(len(rest_list) - 1):
            rest1 = yes_list[0]
            rest2 = yes_list[1]

            print("What would you rather eat? " + rest1 + " or " + rest2 + "?")
            answer = input()
            if((len(orig_list) -1) != curr):
                curr += 1
            
            if (answer == rest1):
                yes_list.remove(rest2)
                # curr += 1
                which_chose = 1
                yes_list.insert(1, orig_list[curr])
            else:
                yes_list.remove(rest1)
                # curr += 1
                which_chose = 2
                yes_list.insert(0, orig_list[curr])
        chosen = ""
        if(which_chose == 1):
            chosen = yes_list[0]
        else:
            chosen = yes_list[1]
        print("You have chosen: " + chosen + "!")

    def __init__(self, rest_list):
        self.cmp(rest_list)




print(rest_info_list())