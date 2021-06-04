from django.db import models

# Create your models here.
class TenantManager(models.Manager):
    def get_queryset(self):
        return super.get_queryset().filter(tenant=self)


class Tenant(models.Model):
    tenant_id = models.IntegerField(max_length=4)
    
    def __str__(self):
        return f'{self.tenant_id}'


class CommonFieldsModel(models.Model):
    class Meta:
        abstract = True
        
    creator = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tenant = models.ForeignKey('tenant_app.Tenant', on_delete=models.CASCADE)