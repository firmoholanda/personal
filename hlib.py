
#open and write file
def onpenFile():
        file = open('dump.xml', 'w')
                file.write('some text')
        file.close()

#merge lists
def merge(list1, list2): 
        merged_list = [[list1[i], list2[i]] for i in range(0, len(list1))] 
        return merged_list


