items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
def countMatches(items, ruleKey, ruleValue):
    # print(items)
    dict = {}
    for item in items:
        if(dict.get('type') == None):
            dict['type'] = {item[0]: 1}
        else:
            print(dict['type'].get(item[0]))
        
        
        # if(dict.get('type').get(item[0])) == None:
        # else:
            # dict['type'] = dict.get(item[0]) + 1
        # dict['color'] = (item[1],0)
        # dict['name'] = (item[2], 0)
    
    print(dict)
    # print(dict.get('type').get(item[0]) + 1)
    # print(dict.get('type').get('phone'))
    
countMatches(items, ruleKey, ruleValue)