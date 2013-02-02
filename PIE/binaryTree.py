class TreeNode:
    def __init__(self,data):
        self.rightNode = None
        self.leftNode = None
        self.data = data
    
    def addNode(self,newData):
        if newData < self.data:
            if self.leftNode == None:
                self.leftNode = TreeNode(newData) 
            else:
                self.leftNode.addNode(newData)
        else:
            if self.rightNode == None:
                self.rightNode = TreeNode(newData)
            else:
                self.rightNode.addNode(newData)
                
    ''' def searchNodes(self,toSearch):
        if self == toSearch:
            print "found"
            return self
        else:'''
    
    '''def printTree(self):
        if self.leftNode:
            self.leftNode.printTree()
        '''
                
def main():
    treeRoot = TreeNode(10)
    treeRoot.addNode(8)
    treeRoot.addNode(12)
    #treeRoot.printTree()
    print treeRoot.leftNode
main()
    