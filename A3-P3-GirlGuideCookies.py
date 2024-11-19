#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:     
#Student Name:  

def guide(no_of_guides):
    guide_name_list=[]
    cookie_box=[]
    prize=["trip to the Girl Guide Jamboree in Aruba","Super Seller Badge","Left Over Cookies",""]
    for i in range(no_of_guides):
        index=i+1
        guide_name=input("\nEnter the name of guide #{0}: ".format(index))
        guide_name_list.append(guide_name)
        boxes_sold=int(input("Enter the number of boxes sold by {0}: ".format(guide_name)))
        cookie_box.append(boxes_sold)
    avg=(sum(cookie_box))/(len(cookie_box))
    print("\nThe average number of boxes sold by each guide was {0}".format(avg))

    print("\nGuide\tPrizes Won:")
    print("\n------------------------------------------------------------")

    for j in range(len(guide_name_list)):
        if cookie_box[j]>avg and cookie_box[j]!=max(cookie_box):
            print("{0}\t-{1}".format(guide_name_list[j],prize[1]))
        elif cookie_box[j]<=avg and cookie_box[j]!=0:
            print("{0}\t-{1}".format(guide_name_list[j],prize[2]))
        elif cookie_box[j]==max(cookie_box):
            print("{0}\t-{1}".format(guide_name_list[j],prize[0]))
        else:
            print("{0}\t-{1}".format(guide_name_list[j],prize[3]))




def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    guides=int(input("Enter the number of guides selling cookies: "))
    
    guide(guides)

    # YOUR CODE ENDS HERE

main()