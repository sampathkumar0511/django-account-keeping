# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-06 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_keeping', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['name'], 'verbose_name': 'Account', 'verbose_name_plural': 'Accounts'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ['-invoice_date', '-pk'], 'verbose_name': 'Invoice', 'verbose_name_plural': 'Invoices'},
        ),
        migrations.AlterModelOptions(
            name='payee',
            options={'ordering': ['name'], 'verbose_name': 'Payee', 'verbose_name_plural': 'Payees'},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-transaction_date', '-pk'], 'verbose_name': 'Transaction', 'verbose_name_plural': 'Transactions'},
        ),
        migrations.AddField(
            model_name='account',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active?'),
        ),
        migrations.AlterField(
            model_name='account',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='currency_history.Currency', verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='account',
            name='initial_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Initial amount'),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='account',
            name='slug',
            field=models.SlugField(max_length=128, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='account',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Total amount'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='amount_gross',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Amount gross'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='amount_net',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Amount net'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='currency_history.Currency', verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_date',
            field=models.DateField(verbose_name='Invoice date'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=256, verbose_name='Invoice No.'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_type',
            field=models.CharField(choices=[('w', 'withdrawal'), ('d', 'deposit')], max_length=1, verbose_name='Invoice type'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_date',
            field=models.DateField(blank=True, null=True, verbose_name='Payment date'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='invoice_files', verbose_name='PDF'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='value_gross',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Value gross'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='value_net',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Value net'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='vat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='VAT'),
        ),
        migrations.AlterField(
            model_name='payee',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Payee'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='account_keeping.Account', verbose_name='Account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount_gross',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Amount gross'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount_net',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Amount net'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='account_keeping.Category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='currency_history.Currency', verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='account_keeping.Invoice', verbose_name='Invoice'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=256, verbose_name='Invoice No.'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='account_keeping.Transaction', verbose_name='Parent'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='payee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='account_keeping.Payee', verbose_name='Payee'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_date',
            field=models.DateField(verbose_name='Transaction date'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('w', 'withdrawal'), ('d', 'deposit')], max_length=1, verbose_name='Transaction type'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='value_gross',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Value gross'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='value_net',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Value net'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='vat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='VAT'),
        ),
    ]
