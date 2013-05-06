# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Material'
        db.create_table('materials_material', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('uploader', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('date_of_creation', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 5, 6, 0, 0))),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('path', self.gf('django.db.models.fields.FilePathField')(max_length=100)),
        ))
        db.send_create_signal('materials', ['Material'])

        # Adding model 'Collection'
        db.create_table('materials_collection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('founder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('date_of_creation', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 5, 6, 0, 0))),
        ))
        db.send_create_signal('materials', ['Collection'])

        # Adding M2M table for field materials_belonging on 'Collection'
        db.create_table('materials_collection_materials_belonging', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('collection', models.ForeignKey(orm['materials.collection'], null=False)),
            ('material', models.ForeignKey(orm['materials.material'], null=False))
        ))
        db.create_unique('materials_collection_materials_belonging', ['collection_id', 'material_id'])

        # Adding model 'Request_for_materials'
        db.create_table('materials_request_for_materials', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issuer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('date_of_creation', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 5, 6, 0, 0))),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('materials', ['Request_for_materials'])

        # Adding M2M table for field materials_in_response on 'Request_for_materials'
        db.create_table('materials_request_for_materials_materials_in_response', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('request_for_materials', models.ForeignKey(orm['materials.request_for_materials'], null=False)),
            ('material', models.ForeignKey(orm['materials.material'], null=False))
        ))
        db.create_unique('materials_request_for_materials_materials_in_response', ['request_for_materials_id', 'material_id'])


    def backwards(self, orm):
        # Deleting model 'Material'
        db.delete_table('materials_material')

        # Deleting model 'Collection'
        db.delete_table('materials_collection')

        # Removing M2M table for field materials_belonging on 'Collection'
        db.delete_table('materials_collection_materials_belonging')

        # Deleting model 'Request_for_materials'
        db.delete_table('materials_request_for_materials')

        # Removing M2M table for field materials_in_response on 'Request_for_materials'
        db.delete_table('materials_request_for_materials_materials_in_response')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'materials.collection': {
            'Meta': {'object_name': 'Collection'},
            'date_of_creation': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 6, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'founder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materials_belonging': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['materials.Material']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        'materials.material': {
            'Meta': {'object_name': 'Material'},
            'date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'date_of_creation': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 6, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'path': ('django.db.models.fields.FilePathField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'uploader': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True'})
        },
        'materials.request_for_materials': {
            'Meta': {'object_name': 'Request_for_materials'},
            'date_of_creation': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 6, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'materials_in_response': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['materials.Material']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        }
    }

    complete_apps = ['materials']