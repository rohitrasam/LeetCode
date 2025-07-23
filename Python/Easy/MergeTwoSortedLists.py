def mergeTwoLists(list1: list[int], list2: list[int]) -> list[int]:
    result = []
    



    """My Solution with lists"""
    # result = []
    # i = 0
    # j = 0
    # while i < len(list1) and j < len(list2):
    #     if list1[i] < list2[j]:
    #         result.append(list1[i])
    #         i += 1
    #     elif list1[i] > list2[j]:
    #         result.append(list2[j])
    #         j += 1
    #     else:
    #         result.append(list1[i])
    #         result.append(list2[j])
    #         i += 1
    #         j += 1
    

    # while i < len(list1):
    #     result.append(list1[i])
    #     i += 1

    # while j < len(list2):
    #     result.append(list2[j])
    #     j += 1

    # return result



if __name__ == '__main__':
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))

    print(mergeTwoLists(l1, l2))