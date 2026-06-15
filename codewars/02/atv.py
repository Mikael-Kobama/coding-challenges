# solucao.py

def partition(arr, classifier_method):
    verdadeiros = []
    falsos = []
    
    for item in arr:
        if classifier_method(item):
            verdadeiros.append(item)
        else:
            falsos.append(item)
            
    return (verdadeiros, falsos)