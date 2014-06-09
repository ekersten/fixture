# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Match'
        db.create_table(u'main_match', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('home', self.gf('django.db.models.fields.related.ForeignKey')(related_name='team_home', to=orm['main.Country'])),
            ('away', self.gf('django.db.models.fields.related.ForeignKey')(related_name='team_away', to=orm['main.Country'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'main', ['Match'])


    def backwards(self, orm):
        # Deleting model 'Match'
        db.delete_table(u'main_match')


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
        },
        u'main.match': {
            'Meta': {'object_name': 'Match'},
            'away': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team_away'", 'to': u"orm['main.Country']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'home': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team_home'", 'to': u"orm['main.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['main']