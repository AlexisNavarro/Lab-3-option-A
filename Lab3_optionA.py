# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:17:35 2019

@author: Alexis Navarro
CS 2302 MW 1:30 PM -2:50 PM
Purpose: To learn how to create Binary search trees with a text file, but then to apply AVL trees and to use RED-BLACK TREES
"""

import numpy as np
import math
import time




#--------------------------BST TREE--------------------------------------------------------------------------------------------------------

class BST:
    def __init__(self, item, root=None,left=None, right=None):  
        self.root = root
        self.item = item
        self.left = left 
        self.right = right 


def insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = insert(T.left,newItem)
    else:
        T.right = insert(T.right,newItem)
    return T

def build_BST(f1,f2):
    tree=None
    
    f3 = open("tree_holder.txt","w")
    
    for line in f1:
        info = line.split(' ')
        tree=insert(tree,[info[0],np.array(info[1:]).astype(np.float)]) #inserts the words and embeddings of the text file
    
    for line2 in f2:
        data = line2.split(',')
        e0 = findWord(tree,data[0])#returns the list when found
        e1 = findWord(tree,data[1])
        print("Similarity", data[0:2], " = ", round(np.sum(e0 * e1) / (math.sqrt(np.sum(e0 * e0)) * math.sqrt(np.sum(e1 * e1))), 4))  # compute the similarity
   
    print('Number of Nodes is: ',num_Nodes(tree))
    print('Height: ', height(tree))
    
   #tried to write on to the file and insert my tree but it would not write anything or read the text file.
    #for line3 in f3:
        #f3.write("word in tree:",tree)
        #f3.close()
    
    #f3 = open("tree_holder.txt","r")
    #print(f3.read())
    #f3.close()

    

    return tree

def num_Nodes(T):
    if T is None:
        return 0
    else:
        return 1 + num_Nodes(T.left)+num_Nodes(T.right)
    return 0

def findWord(T,k):
    t = T  
    while t is not None:  
        if t.item[0] == k:
            #temp.item[1]
            return t.item[1]
        elif t.item[0] > k:  
            t= t.left
        elif t.item[0]<k:  
            t = t.right
    return None 

def height(T):
    if T is None:
        return 0
    leftH = height(T.left)
    rightH = height(T.right)
    
    if rightH<leftH:
        return leftH+1
    else:
        return rightH+1

#--------------------------AVL-TREE--------------------------------------------------------------------------------------------------------
#The AVL code comes from zybooks and with some modifications added on to it.

class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1

#method to check if the current tree I have is an AVL, if not then it would construct it.
def build_AVL(tree):
    AVL_tree = None
    #print('goes in before if ')
    if is_Balanced(tree) == True:
        AVL_tree = tree
        #print('goes in')
        return AVL_tree

    AVL_tree=AVL_rebalance(tree)


    return AVL_tree

def AVL_insert(tree,node):
    if tree.root == None:
        tree.root = node
        node.parent = None
        return

    curr = tree.root
    while curr == None:
        if node.item < curr.item:
            if curr.left == None:
                cur.left = node
                node.parent = curr
                curr = None
            else:
                cur = curr.left
        
        else:
            if curr.right == None:
                curr.right = node
                node.parent = curr
                curr = None
            else:
                curr = curr.right

        node = node.parent
        while node != None:
            AVL_rebalance(tree,node)
            node = node.parent


def AVL_rebalance(tree):
    AVL_updateH(tree)
    if is_Balanced(tree) == -2:
        if is_Balanced(tree.right) ==1:
            AVL_rotate_right(tree.right)==1

        return AVL__rotate_left(tree)
    elif is_Balanced:
        if is_Balanced(tree.left):
            AVL__rotate_left(tree, tree.left)
        
        return AVL_rotate_right(tree)
    return tree

def AVL_rotate_right(self, z): 

        y = z.left 
        T3 = y.right 

        # Perform rotation 
        y.right = z 
        z.left = T3 

        # Update heights 
        z.height = 1 + max(self.height(z.left), 
                        self.height(z.right)) 
        y.height = 1 + max(self.height(y.left), 
                        self.height(y.right)) 

        # Return the new root 
        return y 
        
def AVL__rotate_left(self, z): 
    
            y = z.right 
            T2 = y.left 
    
            # Perform rotation 
            y.left = z 
            z.right = T2 
    
            # Update heights 
            z.height = 1 + max(self.height(z.left), 
                            self.height(z.right)) 
            y.height = 1 + max(self.height(y.left), 
                            self.height(y.right)) 
    
            # Return the new root 
            return y 
    




def AVL_updateH(tree):
    left_height = -1

    if tree.left!=None:
        left_height = tree.left.height

    right_height = -1

    if tree.right != None:
        right_height = tree.right.height
    tree.height = max(left_height, right_height)+1



def AVL_set_child(parent, whichChild, child):
    if whichChild != 'left' and whichChild != 'right':
        return False
    if whichChild == 'left':
        parent.left = child
    else:
        parent.right = parent
    
    AVL_updateH(parent)
    return True



def AVL_replace_Child(parent, curr_child, new_child):
    if parent.left == curr_child:
        return AVL_set_child(parent,'left',new_child)

    elif parent.right == curr_child:
        return AVL_set_child(parent,'right', new_child)

    return False



def is_Balanced(tree):
    if tree is None:
        return True
    lh = height(tree.left)
    rh= height(tree.right)

    if (abs(lh - rh)<1) and is_Balanced(tree.left) is True and is_Balanced(tree.right) is True:
        return True
    return False


#--------------------------RED BLACK TREE--------------------------------------------------------------------------------------------------------
#RED-BLACK TREE methods come from zybooks with some modfications/additions of my own
class Node():
    def __init__(self, data):
        self.data = data  
        self.parent = None 
        self.left = None 
        self.right = None 

        self.color = 1 # 1 . Red, 0 . Black



class red_black_tree():
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color=0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL


    


    def tree_balance(self,node):
        if node.parent == None:
            node.color = 0
            return
        if node.parent.color == 0:
            return

        parent = node.parent
        grandparent = GetGrandparent(node)
        uncle = RBTreeGetUncle(node)
        if uncle != None and uncle.color == 1: 
                parent.color = uncle.color = 0
                grandparent.color = 1
                tree_balance(node, grandparent)
                return
        
        if node == parent.right  and parent == grandparent.left: 
            rotate_left(node, parent)
            node = parent
            parent = node.parent
        
        elif node == parent.left and parent == grandparent.right:
            rotate_left(node, parent)
            self = parent
            parent = node.parent
        
        parent.color = 0
        grandparent.color = 1
        if node == parent.left:
            rotate_right(node, grandparent)
        else:
            rotate_left(node, grandparent)
            

    def GetGrandparent(self):
        if self.parent == None:
            return None
        return self.parent.parent


    def RBTreeGetUncle(self):
        grandparent = None
        if self.parent != None:
            grandparent = self.parent.parent
        if grandparent == None:
            return None
        if grandparent.left == self.parent:
            return grandparent.right
        else:
            return grandparent.left


    def set_child(self, which_child,child):
        if which_child != "left" and which_child != "right":
            return False

        if which_child == "left":
            self.left = child
        else:
            self.right = child
        if child != None:
            child.parent = self
        return True


    def replace_child(self,current_child,new_child):
        if self.left == current_child:
            return set_child(self, "left", new_child)
        elif self.right == current_child:
            return set_child(self, "right", new_child)
        return False


    def rotate_left(self, node):
        right_left_child = node.right.left
        if node.parent != None:
            replace_child(node.parent, node, node.right)
        else: 
            tree.root = node.right
            tree.root.parent = None
        
        set_child(self.right, "left", node)
        set_child(self, "right", right_left_child)

    def rotate_right(self, node):
        left_right_child = node.left.right
        if node.parent != None:
            replace_child(node.parent, node, node.left)
        else:
            tree.root = node.left
            tree.root.parent = None
        
        set_child(node.left, "right", node)
        set_child(node, "left", left_right_child)

    #--------------------------MAIN--------------------------------------------------------------------------------------------------------

def main():
    file_info=[]
    my_file_info=[]
    tree = BST(None)
    node = Node(None)
    AVL = TreeNode(None)
    RBT = TreeNode(None)


    f1=open('glove.6B.50d.txt',encoding='utf-8') #open the file with the similarities  
    f2 = open('List.txt',encoding='utf-8') #uses my own text file to be read later on

    
    
    
    print('Choose table implementation')  
    x=int(input('Do you want a AVL Tree (AVL) or Red black trees (RBT)? select 1 for AVL or 2 for RBT: '))
    
    
    if x == 1:
        start_Time=int(time.time())#starting time

        print('Building Binary Search Tree with AVL ')
        tree=build_BST(f1,f2) # make the BST 
        AVL = build_AVL(tree.root) # checks if the BST is an AVL
        end_Time = int(time.time())#ending time
        print('\nRunning time for binary search tree query processing: ',(end_Time-start_Time))
    elif x == 2:
        start_Time2=int(time.time())#starting time

        print('Building Binary Search Tree with a Red Black Tree')
        tree = build_BST(f1,f2)
        RBT= red_black_tree.tree_balance(tree.root,node) #TAKES THE BST TREE TO BE MADE INTO A RED-BLACK TREE

        end_Time2 = int(time.time())#ending time
        print('\nRunning time for binary search tree query processing: ',(end_Time2-start_Time2))

if __name__=="__main__":
    main()