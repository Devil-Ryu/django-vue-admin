from django.shortcuts import render

# Create your views here.
from itsm_app.models import holemend
from itsm_app.serializers import holemendSerializer, holemendCreateUpdateSerializer
from dvadmin.utils.viewset import CustomModelViewSet

class holemendModelViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = holemend.objects.all()
    serializer_class = holemendSerializer
    create_serializer_class = holemendCreateUpdateSerializer
    update_serializer_class = holemendCreateUpdateSerializer
    filter_fields = ['Sn', 'Status']
    search_fields = ['Sn']