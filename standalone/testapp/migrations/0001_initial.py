# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TestModel'
        db.create_table('testapp_testmodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('myfield', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('testapp', ['TestModel'])


    def backwards(self, orm):
        
        # Deleting model 'TestModel'
        db.delete_table('testapp_testmodel')


    models = {
        'testapp.testmodel': {
            'Meta': {'object_name': 'TestModel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'myfield': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['testapp']
