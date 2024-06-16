nums = [0,1,2,3,4]
index = [0,1,2,2,1]
def createTargetArray(nums, index):
    target = []
    print(len(target))
    for idx in index:
        if(len(target) == 0):
            print(idx)
            target[idx] = nums[idx]
        # target.append(nums[idx])
    
    # print(target)
createTargetArray(nums, index)