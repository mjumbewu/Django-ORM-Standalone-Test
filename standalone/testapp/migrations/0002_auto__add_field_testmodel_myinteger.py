# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'TestModel.myinteger'
        db.add_column('testapp_testmodel', 'myinteger', self.gf('django.db.models.fields.IntegerField')(null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'TestModel.myinteger'
        db.delete_column('testapp_testmodel', 'myinteger')


    models = {
        'testapp.testmodel': {
            'Meta': {'object_name': 'TestModel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'myfield': ('django.db.models.fields.TextField', [], {}),
            'myinteger': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['testapp']
