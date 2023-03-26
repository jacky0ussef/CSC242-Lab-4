'''
Jack Youssef
2/16/2023

This driver program tests the ArrayBag and LinkedBag classes, which now each include a clone method.

This program creates an ArrayBag, called array_bag. Then, array_bag_clone is created, using the clone method of array_bag.
These two bags are then compared for equality and identity. Their contents are identical, but they are not the same bag.

This program creates a LinkedBag, called linked_bag. Then, linked_bag_clone is created, using the clone method of linked_bag.
These two bags are then compared for equality and identity. Their contents are identical, but they are not the same bag.
'''

from arraybag import ArrayBag
from linkedbag import LinkedBag
        
        
def main():
    ''' Tests the ArrayBag and LinkedBag classes. '''
    
    # testing ArrayBag's clone method
    print('Testing the ArrayBag clone method:\n')
    array_bag = ArrayBag([1, 2, 3])
    array_bag_clone = array_bag.clone()
    print('array_bag == array_bag_clone, expecting true:', array_bag == array_bag_clone)
    print('array_bag is array_bag_clone, expecting false:', array_bag is array_bag_clone, '\n')
    
    print('Testing the LinkedBag clone method:\n')
    linked_bag = LinkedBag([4, 5, 6])
    linked_bag_clone = linked_bag.clone()
    print('linked_bag == linked_bag_clone, expecting true:', linked_bag == linked_bag_clone)
    print('linked_bag is linked_bag_clone, expecting false:', linked_bag is linked_bag_clone)


if __name__ == '__main__':
    main()
        

        