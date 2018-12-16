from django.db import models

# Create your models here.


class Sensor(models.Model):
    """传感器设备"""
    en_name = models.CharField(
        max_length=50, verbose_name="英文名称", default="")
    cn_name = models.CharField(
        max_length=50, verbose_name="中文名称", default="")
    code = models.CharField(
        max_length=50, verbose_name="16进制编号", default="")
    unit = models.CharField(
        max_length=50, verbose_name="单位", default="")
    description = models.CharField(
        max_length=100, verbose_name="描述信息", default="")

    def __str__(self):
        return "{}|{}".format(self.code, self.cn_name)

class FunctionCode(models.Model):
    """操作"""
    en_name = models.CharField(
        max_length=50, verbose_name="英文名称", default="")
    cn_name = models.CharField(
        max_length=50, verbose_name="中文名称", default="")
    code = models.CharField(
        max_length=50, verbose_name="16进制编号", default="")
    description = models.CharField(
        max_length=100, verbose_name="描述信息", default="")


class  Message(models.Model):
    """监控数据"""
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    data = models.CharField(max_length=50, default="", verbose_name="传感器返回数据") 
    display_data= models.CharField(max_length=50, default="", verbose_name="界面显示数据") 
    sensor = models.ForeignKey(
        Sensor, related_name="message", verbose_name="传感器",
        on_delete=models.CASCADE) 