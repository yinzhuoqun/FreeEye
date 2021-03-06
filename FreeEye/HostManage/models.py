from django.db import models

# Create your models here.
class Host(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=128)
    port = models.IntegerField(default=22)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    remark = models.TextField(max_length=128,blank=True,default='')
    active = models.BooleanField(default=False)
    isDel = models.BooleanField(default=False)
    hostgroup = models.ForeignKey('SystemManage.HostGroup',on_delete=models.SET_NULL,blank=True,null=True,default=None)
    alert = models.ManyToManyField('AlertManage.Alert',blank=True,default=None)
    createAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s -- %s'%(self.name,self.addr)


class HostInfo(models.Model):
    host = models.OneToOneField(Host)
    OS = models.CharField(max_length=64)
    cpu_version = models.CharField(max_length=128)
    cpu_thd_cnt = models.IntegerField()
    MAC = models.CharField(max_length=32)
    mem_total = models.IntegerField()
    kernal_version = models.CharField(max_length=128)

class HostStat(models.Model):
    host = models.ForeignKey(Host)
    cpu_sys = models.FloatField()
    cpu_usr = models.FloatField()
    cpu_idle = models.FloatField()
    mem_total = models.IntegerField()
    mem_used = models.IntegerField()
    mem_free = models.IntegerField()
    mem_avai = models.IntegerField()
    net_sent = models.IntegerField()
    net_recv = models.IntegerField()
    disk_write = models.IntegerField()
    disk_read = models.IntegerField()
    createAt = models.DateTimeField(auto_now_add=True)

class Application(models.Model):
    appName = models.CharField(max_length=32)
    cmdline = models.CharField(max_length=32)
    cmdArgs = models.CharField(max_length=128)
    startCommand = models.CharField(max_length=256)
    stopCommand = models.CharField(max_length=256)

class HostAppliction(models.Model):
    NOT_INSTALL = 'NI'
    OFF = 'OF'
    ON = 'ON'
    STATUS_CHOICES=(
        (NOT_INSTALL,'未安装'),
        (OFF,'未启动'),
        (ON,'运行中'),
    )
    host = models.ForeignKey(Host)
    application_id = models.IntegerField()
    status = models.CharField(max_length=2,choices=STATUS_CHOICES,default=OFF)
    updateAt  = models.DateTimeField(auto_now=True)
