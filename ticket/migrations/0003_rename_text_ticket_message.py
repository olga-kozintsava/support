# Generated by Django 3.2.7 on 2021-09-21 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_alter_ticket_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='text',
            new_name='message',
        ),
    ]
