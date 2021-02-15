from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from milestone.serializers import *


@api_view(['GET'])
def api_milestone_by_project(request, pk):
    milestones = Milestone.objects.filter(project_id=pk)
    serializer = MilestoneSerializer(milestones, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def api_milestone_add(request):
    print("cao")
    serializer = CreateMilestoneSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Milestone successfully added.", status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'GET', 'PUT'])
def api_milestone_detail(request, pk):
    try:
        milestone = Milestone.objects.get(id=pk)
    except (KeyError, Milestone.DoesNotExist) as ex:
        return Response({'error': 'Invalid or missing object id'}, status=status.HTTP_404_NOT_FOUND,
                        content_type="application/json")
    if request.method == 'GET':
        serializer = MilestoneSerializer(milestone)
        if not milestone.deleted:
            return JsonResponse(serializer.data)
        return Response({'error': 'Invalid or missing object id'}, status=status.HTTP_404_NOT_FOUND,
                        content_type="application/json")
    elif request.method == 'DELETE':
        milestone.deleted = True
        milestone.save()
        return Response({'success': 'Milestone successfully deleted'}, status=status.HTTP_200_OK)

    serializer = CreateMilestoneSerializer(milestone, data=request.data)
    if serializer.is_valid():
        milestone = serializer.save()
        milestone.save()
        return Response({'success': 'Milestone successfully edited'}, status=status.HTTP_200_OK,
                        content_type="application/json")
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")