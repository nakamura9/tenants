from tenant_app.models import Tenant

def get_tenant_from_request(request):
    return Tenant.objects.get(tenant_id=request.session['tenant_id'])

def tenant_filter(manager, request):
    tenant = get_tenant_from_request(request)    
    return manager.filter(tenant=tenant)