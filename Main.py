import Process as p
def VSM():

    freeTextQuery=input("Enter the Query : ")
    query = freeTextQuery
    result = p.main(query)
    for x in result:
        print(x[0],"   ",x[1])

VSM()

