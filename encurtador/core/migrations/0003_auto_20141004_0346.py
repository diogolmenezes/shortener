# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_url_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='url',
            new_name='original',
        ),
        migrations.RenameField(
            model_name='url',
            old_name='url_encurtada',
            new_name='short',
        ),
    ]
