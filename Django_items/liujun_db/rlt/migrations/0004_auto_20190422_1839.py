# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rlt', '0003_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='stutent_name',
            new_name='student_name',
        ),
    ]
