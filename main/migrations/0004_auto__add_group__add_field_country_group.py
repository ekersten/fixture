# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Group'
        db.create_table(u'main_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'main', ['Group'])

        # Adding field 'Country.group'
        db.add_column(u'main_country', 'group',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['main.Group']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Group'
        db.delete_table(u'main_group')

        # Deleting field 'Country.group'
        db.delete_column(u'main_country', 'group_id')


    models = {
        u'main.country': {
            'Meta': {'object_name': 'Country'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'flag': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['main']