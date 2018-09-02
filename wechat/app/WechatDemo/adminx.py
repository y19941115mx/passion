# Register your models here.
import xadmin
from xadmin import views

from .models import Banner, BannerItem


class GlobalSetting(object):
    site_title = "微信小程序后台"
    site_footer = "想象力有限公司"


class BannerAdmin(object):
    pass


class BannerItemAdmin(object):
    style_fields = {"detail": "ueditor"}


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(BannerItem, BannerItemAdmin)
xadmin.site.register(views.CommAdminView, GlobalSetting)