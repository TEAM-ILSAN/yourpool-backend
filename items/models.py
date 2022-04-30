from django.db import models

class Item(models.Model):
    ITEM_CHOICES = [
        ('HAT', 'HAT'),
        ('ACC', 'ACC'),
        ('TAB', 'TABLE'),
        ('CLO', 'CLOTHES'),
        ('SKIN', 'SKIN'),
        ('HAIR', 'HAIR'),
    ]
    
    item_name = models.CharField(max_length=30)
    category = models.CharField(max_length=4, choices=ITEM_CHOICES)
    price = models.IntegerField()

    class Meta:
        db_table = 'items'