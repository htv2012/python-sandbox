import multiprocessing

def main():
    data = []
    total = []
    for j in range(0,10):
        total.append(data)
        for i in range(0,100):
            data.append({str(i):i})

    CalcManager(total,start=0,end=50)

def CalcManager(myData,start,end):
    print('in calc manager')
    #Multi processing
    #Set the number of processes to use.  
    nprocs = 3
    #Initialize the multiprocessing queue so we can get the values returned to us
    tasks = multiprocessing.JoinableQueue()
    result_q = multiprocessing.Queue()
    #Setup an empty array to store our processes
    procs = []
    #Divide up the data for the set number of processes 
    interval = (end-start)/nprocs 
    new_start = start
    #Create all the processes while dividing the work appropriately
    for i in range(nprocs):
        print('starting processes')
        new_end = new_start + interval
        #Make sure we dont go past the size of the data 
        if new_end > end:
            new_end = end 
        #Generate a new process and pass it the arguments 
        data = myData[new_start:new_end]
        #Create the processes and pass the data and the result queue
        p = multiprocessing.Process(target=multiProcess,args=(data,new_start,new_end,result_q,i))
        procs.append(p)
        p.start()
        #Increment our next start to the current end 
        new_start = new_end+1
    print('finished starting')    

    #Print out the results
    for i in range(nprocs):
        result = result_q.get()
        print(result)

    #Joint the process to wait for all data/process to be finished
    for p in procs:
        p.join()

#MultiProcess Handling
def multiProcess(data,start,end,result_q,proc_num):
    print('started process')
    results = []
    temp = []
    for i in range(0,22):
        results.append(temp)
        for j in range(0,3):
            temp.append(j)
    result_q.put(results)
    return

if __name__== '__main__':   
    main()
