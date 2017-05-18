#coding:utf-8
#建堆
def build_max_heap(x):
    j = int(len(x)/2)-1
    while j>=0:
        max_heap(x,j)
        j=j-1
#维护堆性质
def max_heap(x,i):
    l = 2*i+1
    r = 2*i+2
    if i == 0:
        l = 1
        r = 2
    if l <= len(x)-1 and x[l] > x[i]:
        largest = l
    else: largest = i
    if r <= len(x)-1 and x[r] > x[largest]:
        largest = r
    if largest != i:
        x[largest],x[i] = x[i],x[largest]
        return max_heap(x,largest)
    else:return x
#堆排序算法
def heapsort(x):
    build_max_heap(x)
    i = len(x)
    while i >= 1:
        del x[0]
        print("1:",x)
        max_heap(x,0)





a=[4,1,3,2,16,9,10,14,8,7]
build_max_heap(a)
print(a)
heapsort(a)
print(a)