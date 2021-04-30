def clusterError(labelMethod_1,labelMethod_2):
    '''
    calculate the cluster error
    labelMethod_1 & labelMethod_2 are list of the dots derived from different label method, for the label method every time is randomised
    '''
    cluster_1 = {}#cluster_1 &cluster_2 are the dictionary in which the keys are the lables of the dots and the values are their correspondent index in labelMethod_1 & labelMethod_2
    cluster_2 = {}

    #produce the wanted cluster_1 & cluster_2
    for i in range(len(labelMethod_1)):
        if labelMethod_1[i] in cluster_1.keys():
            cluster_1[labelMethod_1[i]].append(i)
        else:
            cluster_1[labelMethod_1[i]] = [i]

    for k in range(len(labelMethod_1)):
        if labelMethod_2[k] in cluster_2.keys():
            cluster_2[labelMethod_2[k]].append(k)
        else:
            cluster_2[labelMethod_2[k]] = [k]

    #permutated the cluster_2
    import itertools
    permutatedCluster_2 = list(itertools.permutations(list(cluster_2.values())))#the list of all posibilities of the permutated cluster_2 in the form of tuple

    #produce the list of the cluster errors of different permutations of cluster_2
    clusterErrorList = []
    for l in permutatedCluster_2:
        clusterErrors = 0
        for m in range(len(l)):
            clusterErrors += len(set(l[m]) - set(list(cluster_1.values())[m]))
            clusterErrors += len(set(list(cluster_1.values())[m]) - set(l[m]))
        clusterErrorList.append(clusterErrors)

    #return the minimum cluster error
    return min(clusterErrorList)

print(clusterError(['1','1','2','3'],['1','2','2','3']))
