#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not'''
    length = len(boxes)
    keys = set()
    opened_boxes = []
    k = 0

    while k < length:
        oldi = k
        opened_boxes.append(k)
        keys.update(boxes[k])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                k = key
                break
        if oldi != k:
            continue
        else:
            break

    for k in range(length):
        if k not in opened_boxes and k != 0:
            return False
    return True
