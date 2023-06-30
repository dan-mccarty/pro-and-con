
from django.shortcuts import render
from .models import Decision

def decision_save(request, decision_index):

    print('...decision_save...')
    print(decision_index, request)
    print('request.items: ', request.__dict__)

    return render(request, 'decision.html')



def decision_page(request, decision_index=0):
    
    print('user_id:', request.user.id)

    context = {
        'id': None,
        'description': 'some random text',
        'pros': ['1', '2', '3'],
        'cons': ['1', '2']
    }

    objects = Decision.objects.filter(user_id=request.user.id)

    if len(objects) != 0:

        if decision_index < 0:
            print('decision_index exceeds minimum')
            decision_index = 0

        if decision_index >= len(objects):
            print('decision_index exceeds maximum')
            decision_index = len(objects) - 1

        if 0 >= decision_index < len(objects):
            print('decision_index:', decision_index)
            print('object:', objects[decision_index])
            obj = objects[decision_index]
            context['id'] = decision_index
            context['description'] = obj.description
            context['pros'] = obj.pros
            context['cons'] = obj.cons
    
    return render(request, 'decision.html', context)