from django.contrib import admin
from .models import Post, Vacancies, Applications, HrDocs, CorpDocs, CompanyApps, FAQs, HomeImg

admin.site.site_header = 'NCWSC INTRANET ADMINISTRATION'
admin.site.register(Post)
admin.site.register(Vacancies)
admin.site.register(Applications)
admin.site.register(HrDocs)
admin.site.register(CorpDocs)
admin.site.register(CompanyApps)
admin.site.register(FAQs)
admin.site.register(HomeImg)