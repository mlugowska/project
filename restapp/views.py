# -*- coding: utf-8 -*-
from restapp.models import Profile
from restapp.serializers import ProfileSerializer
from rest_framework.decorators import detail_route
from rest_framework import viewsets
from rest_framework.response import Response


class ProfileViewSet(viewsets.ModelViewSet):

    """
    ADD, UPDATE OR DELETE RABBIT PROFILE
    """

    #  API endpoint that allows users to be viewed or edited
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    # decorator can be used to add any custom endpoints that don't fit into the standard create/update/delete style.
    @detail_route()
    def highlight(self, *args, **kwargs):
        self.profile = self.get_object()
        return Response(self.profile.highlighted)
    #
    # @api_view(['GET'])
    # def profile_get(request):
    #     def heapSort(data):
    #         dataSize = len(data)
    #
    #         def swap(parent_idx, child_idx):
    #             if data[parent_idx] < data[child_idx]:
    #                 data[parent_idx], data[child_idx] = data[child_idx], data[parent_idx]
    #
    #         def indexing(parent_idx, unsortedData):
    #
    #             greaterElement_idx = lambda a, b: a if data[a] > data[b] else b
    #
    #             while parent_idx * 2 + 2 < unsortedData:
    #                 childLeft_idx = parent_idx * 2 + 1
    #                 childRight_idx = parent_idx * 2 + 2
    #                 greaterChild_idx = greaterElement_idx(childLeft_idx, childRight_idx)
    #                 swap(parent_idx, greaterChild_idx)
    #                 parent_idx = greaterChild_idx
    #
    #         def convert_to_heap():
    #             for element in range((dataSize / 2) - 1, -1, -1):
    #                 indexing(element, dataSize)
    #
    #         def sorting():
    #             iter = dataSize
    #             while iter > 0:
    #                 iter -= 1
    #             swap(iter, 0)
    #             indexing(0, iter)
    #
    #         convert_to_heap()
    #         sorting()
    #
    #     profile = Profile.objects.all()
    #     carrot_field = Profile.objects.values_list('carrots', flat=True).order_by('carrots')
    #     heapSort(carrot_field)
    #     serializer = ProfileSerializer(carrot_field, many=True)
    #     return Response(serializer.data)




