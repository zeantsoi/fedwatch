# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Keyword', fields ['keyword']
        db.create_unique(u'api_keyword', ['keyword'])


    def backwards(self, orm):
        # Removing unique constraint on 'Keyword', fields ['keyword']
        db.delete_unique(u'api_keyword', ['keyword'])


    models = {
        u'api.keyword': {
            'Meta': {'object_name': 'Keyword'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'unique': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['api']