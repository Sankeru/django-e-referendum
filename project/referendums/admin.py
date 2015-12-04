from django.contrib import admin
from referendums.models import Vote, Referendum
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.forms import TextInput, Textarea

# Register your models here.


class VoteAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('id', )}),
        (_('Информация о голосе'), {'fields': (
                                            'referendum',
                                            'user',
                                            'result',
                                            'datetime_created',
                                            )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('referendum',
                       'user',
                       'result',)},
        ),
    )

    readonly_fields = ('id', )
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},
    }

    list_display = ('id', 'referendum', 'result', 'user', 'datetime_created',)
    search_fields = ('id', 'referendum', 'result', 'user', 'datetime_created',)
    ordering = ('datetime_created',)


class ReferendumAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Информация о референдуме'), {'fields': (
                                            'id',
                                            'title',
                                            'question',
                                            'result',
                                            'initiator',
                                            'top_address',
                                            'datetime_created',
                                            )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title',
                       'question',
                       'result',
                       'initiator',
                       'top_address',
                       'datetime_created',)},
        ),
    )

    readonly_fields = ('id', )
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '30'})},
    }

    list_display = ('id', 'title',
                    'result', 'initiator', 'datetime_created',)
    search_fields = ('id', 'title', 'result', 'initiator', 'datetime_created',)
    ordering = ('datetime_created',)


admin.site.register(Vote, VoteAdmin)
admin.site.register(Referendum, ReferendumAdmin)
