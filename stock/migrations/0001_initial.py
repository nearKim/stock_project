# Generated by Django 3.1 on 2020-08-26 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(blank=True, max_length=30, null=True)),
                ('is_deprecated', models.BooleanField(default=False)),
                ('locale', models.CharField(max_length=20)),
                ('market_name', models.CharField(max_length=30)),
                ('ticker_type', models.CharField(choices=[('stk', '주식'), ('etf', 'ETF'), ('ftr', '선물')], default='stk', max_length=3)),
            ],
        ),
    ]
