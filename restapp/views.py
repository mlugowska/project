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

    #  API endpoint -> profil można zobaczyć oraz edytować
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    # decorator w celu dodania własnych ENDpointów, które są inne niż standardowe create/update/delete
    @detail_route()
    def highlight(self, *args, **kwargs):

        # def heapSort(data):
        #     dataSize = len(data)
        #
        #     def swap(parent_idx, child_idx):
        #         if data[parent_idx] < data[child_idx]:
        #             data[parent_idx], data[child_idx] = data[child_idx], data[parent_idx]
        #
        #     def indexing(parent_idx, unsortedData):
        #
        #         greaterElement_idx = lambda a, b: a if data[a] > data[b] else b
        #
        #         while parent_idx * 2 + 2 < unsortedData:
        #             childLeft_idx = parent_idx * 2 + 1
        #             childRight_idx = parent_idx * 2 + 2
        #             greaterChild_idx = greaterElement_idx(childLeft_idx, childRight_idx)
        #             swap(parent_idx, greaterChild_idx)
        #             parent_idx = greaterChild_idx
        #
        #     def convert_to_heap():
        #         for element in range((dataSize / 2) - 1, -1, -1):
        #             indexing(element, dataSize)
        #
        #     def sorting():
        #         iter = dataSize
        #         while iter > 0:
        #             iter -= 1
        #         swap(iter, 0)
        #         indexing(0, iter)
        #
        #     convert_to_heap()
        #     sorting()

        self.profile = self.get_object()#.values('carrots')
        # heapSort(self.profile)
        return Response(self.profile.highlighted)







