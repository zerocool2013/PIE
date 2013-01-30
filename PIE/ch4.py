class Person:
    def __init__(self, name):
        self.name = name
        self.skateboards = []
        self.girlfriends = [] 
        self.jobs = []

    def addBoard(self, board):
        self.skateboards.append(board)
        
    def addGirlfriend(self,gfName):
        self.girlfriends.append( gfName )
    
    def addJob(self, job ):
        self.jobs.append(job)
   
    '''def displayInfo(self):
        print self.name + "'s Info:"
        print "Boards: " + self.skateboards
        print "Girlfriends: " + self.girlfriends
        print "Jobs: " + self.jobs'''
        
def main():
    anthony = Person( 'anthony' )
    anthony.addBoard('black')
    anthony.addGirlfriend('audrie')
    anthony.addJob('chase')
    print anthony.name
    print anthony.skateboards
    print anthony.girlfriends
    print anthony.jobs
    anthony.addGirlfriend('mary')
    print anthony.girlfriends
    x = []
    x.append(anthony.girlfriends)
    x.append(anthony.jobs)
    print x
    
main()

    