import cPickle

dict = cPickle.load(open("cifar_2class_py2.p","rb"))

for i in dict:
    print i, dict[i].shape
