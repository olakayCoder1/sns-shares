# Generated by Django 4.0.10 on 2024-04-01 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_mailbox', '0008_auto_20190219_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('phone_2', models.CharField(blank=True, max_length=50, null=True)),
                ('email_2', models.EmailField(blank=True, max_length=50, null=True)),
                ('ads', models.CharField(blank=True, max_length=255, null=True)),
                ('deposit_date', models.DateField(blank=True, null=True)),
                ('contract_start_date', models.DateField(blank=True, null=True)),
                ('contract_days', models.IntegerField(blank=True, null=True)),
                ('system_provided', models.BooleanField(default=True)),
                ('last_contacted', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '顧客',
                'verbose_name_plural': '顧客管理',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('property_type', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '属性',
                'verbose_name_plural': '属性管理',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('status_type', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ステータス',
                'verbose_name_plural': 'ステータス管理',
            },
        ),
        migrations.CreateModel(
            name='MailTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'メールテンプレート',
                'verbose_name_plural': 'メールテンプレート管理',
            },
        ),
        migrations.CreateModel(
            name='MailDomain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(blank=True, max_length=255, null=True)),
                ('port', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('imap_host', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mailbox', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_mailbox.mailbox')),
            ],
            options={
                'verbose_name': 'メールドメイン',
                'verbose_name_plural': 'メールドメイン管理',
            },
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.EmailField(blank=True, max_length=50, null=True)),
                ('outgoing', models.BooleanField(default=False)),
                ('read', models.DateTimeField(blank=True, null=True)),
                ('processed', models.DateTimeField(blank=True, null=True)),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attachments', models.ManyToManyField(blank=True, to='django_mailbox.messageattachment')),
                ('customers', models.ManyToManyField(blank=True, to='db_schema.customer')),
                ('managers', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'メール',
                'verbose_name_plural': 'メール管理',
            },
        ),
        migrations.CreateModel(
            name='CustomerMemo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db_schema.customer')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '顧客メモ',
                'verbose_name_plural': '顧客メモ管理',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db_schema.property'),
        ),
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db_schema.status'),
        ),
    ]
