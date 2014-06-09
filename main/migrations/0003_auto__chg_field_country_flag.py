# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Country.flag'
        db.alter_column(u'main_country', 'flag', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    def backwards(self, orm):

        # Changing field 'Country.flag'
        db.alter_column(u'main_country', 'flag', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100))

    models = {
        u'main.country': {
            'Meta': {'object_name': 'Country'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'flag': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['main']