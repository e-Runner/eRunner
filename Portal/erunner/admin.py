from django.contrib import admin
from models import Statistics, Id, Result
from models_dimension import Prod, Modl, SubModl, SubFW, ResultDesc,TestLevel, ModVersion, TestSuite,Importance

admin.site.register(Statistics)
admin.site.register(Id)
admin.site.register(Result)
admin.site.register(Prod)
admin.site.register(SubFW)
admin.site.register(Modl)
admin.site.register(SubModl)
admin.site.register(ResultDesc)
admin.site.register(Importance)

admin.site.register(TestLevel)
class TestVersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'module')

admin.site.register(ModVersion, TestVersionAdmin)

class TestSuiteAdmin(admin.ModelAdmin):
    raw_id_fields = ('mod_version',)

admin.site.register(TestSuite, TestSuiteAdmin)