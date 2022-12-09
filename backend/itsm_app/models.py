from django.db import models
from django.utils import timezone
# Create your models here.
from dvadmin.utils.models import CoreModel


class holemend(CoreModel):
    Sn = models.CharField(max_length=64, verbose_name="工单号")
    Summary = models.CharField(max_length=255, verbose_name="主题")
    Creator = models.CharField(max_length=64, verbose_name="建单人")
    CreateDate = models.DateTimeField(
        default=timezone.now, blank=True, null=True, verbose_name="建单日期")
    Handler = models.CharField(max_length=64, blank=True, null=True, verbose_name="处理人")
    Mobile = models.CharField(max_length=64, blank=True, null=True, verbose_name="手机号")
    Status = models.CharField(max_length=64, blank=True, null=True, verbose_name="工单状态")
    BaseId = models.CharField(max_length=64, blank=True, null=True, verbose_name="文件ID")

    class Meta:
        db_table = "holemend"
        verbose_name = "工单表"
        verbose_name_plural = "工单表"
