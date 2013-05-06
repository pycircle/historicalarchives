# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Action'
        db.create_table('actions_action', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 5, 6, 0, 0))),
            ('expire_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('aim', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('actions', ['Action'])

        # Adding M2M table for field participants on 'Action'
        db.create_table('actions_action_participants', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('action', models.ForeignKey(orm['actions.action'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('actions_action_participants', ['action_id', 'user_id'])

        # Adding M2M table for field linked_collections on 'Action'
        db.create_table('actions_action_linked_collections', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('action', models.ForeignKey(orm['actions.action'], null=False)),
            ('collection', models.ForeignKey(orm['materials.collection'], null=False))
        ))
        db.create_unique('actions_action_linked_collections', ['action_id', 'collection_id'])

        # Adding M2M table for field materials_in_response on 'Action'
        db.create_table('actions_action_materials_in_response', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('action', models.ForeignKey(orm['actions.action'], null=False)),
            ('material', models.ForeignKey(orm['materials.material'], null=False))
        ))
        db.create_unique('actions_action_materials_in_response', ['action_id', 'material_id'])


    def backwards(self, orm):
        # Deleting model 'Action'
        db.delete_table('actions_action')

        # Removing M2M table for field participants on 'Action'
        db.delete_table('actions_action_participants')

        # Removing M2M table for field linked_collections on 'Action'
        db.delete_table('actions_action_linked_collections')

        # Removing M2M table for field materials_in_response on 'Action'
        db.delete_table('actions_action_materials_in_response')


    models = {
        'actions.action': {
            'Meta': {'ordering': "['-expire_date']", 'object_name': 'Action'},
            'aim': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'expire_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linked_collections': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['materials.Collection']", 'symmetrical': 'False'}),
            'materials_in_response': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['materials.Material']", 'symmetrical': 'False'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 6, 0, 0)'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
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
        }
    }

    complete_apps = ['actions']