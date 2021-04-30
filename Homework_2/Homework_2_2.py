import sys
string = sys.stdin.read()
string = string.split('\n')
label_1 = string[0]
label_1 = label_1.split(' ')
label_2 = string[1]
label_2 = label_2.split(' ')

def clusterError(labelMethod_1,labelMethod_2):
    cluster_1 = {}
    cluster_2 = {}

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

    import itertools
    permutatedCluster_2 = list(itertools.permutations(list(cluster_2.values())))

    clusterErrorList = []
    for l in permutatedCluster_2:
        clusterErrors = 0
        for m in range(len(l)):
            clusterErrors += len(set(l[m]) - set(list(cluster_1.values())[m]))
            clusterErrors += len(set(list(cluster_1.values())[m]) - set(l[m]))
        clusterErrorList.append(clusterErrors)

    return min(clusterErrorList)

print(clusterError(label_1,label_2))
