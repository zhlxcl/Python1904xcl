import xadmin

from .models import *

xadmin.site.register(Member)
xadmin.site.register(Customer)
xadmin.site.register(Color)
xadmin.site.register(Category)
xadmin.site.register(Tag)
xadmin.site.register(Good)
xadmin.site.register(Ads)