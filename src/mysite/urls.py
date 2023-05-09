"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from personal.views import (
    home_screen_view,
    l2_tools_view,
    openHistoryExtendedPage_view,
    liveSearch_view,
    boAccountCreatePage_view,
    archiveRound_view,
    archiveRedshiftRound_view,
    RTP_view,
    gameEnb_view,
    infoPage_view,
    rtpCloning_view,
)

from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
    theme_view,
)

urlpatterns = [
    path('theme/', theme_view, name="theme"),
    path('admin/', admin.site.urls),
    path('', home_screen_view, name="home"),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),
    path('l2_tools/', l2_tools_view, name="L2"),
    path('openHistoryExtendedPage/', openHistoryExtendedPage_view, name="openHistoryExtended"),
    path('liveSearchPage/', liveSearch_view, name="liveSearch"),
    path('boAccountCreatePage/', boAccountCreatePage_view, name="boAccGenerator"),
    path('archiveRoundPage/', archiveRound_view, name="checkArchiveRound"),
    path('archiveRedshiftRoundPage/', archiveRedshiftRound_view, name="checkArchiveRedshiftRound"),
    path('rtpPages/', RTP_view, name="rtpPages"),
    path('gameEnbPage/', gameEnb_view, name="gameEnbPage"),
    path('infoPage/', infoPage_view, name="infoPage"),
    path('rtpCloning/', rtpCloning_view, name="rtpCloning"),
]
