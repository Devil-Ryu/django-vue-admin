from itsm_app.models import holemend
from dvadmin.utils.serializers import CustomModelSerializer


class holemendSerializer(CustomModelSerializer):
    """
    序列化器
    """
    class Meta:
        model = holemend
        fields = "__all__"


class holemendCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的序列化器
    """
    class Meta:
        model = holemend
        fields = "__all__"
