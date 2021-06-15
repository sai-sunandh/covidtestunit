from django.db import models

# Create your models here.

class test(models.Model):
	Name=models.CharField(max_length=30)
	Age=models.IntegerField()
	Email=models.EmailField()
	Phone=models.BigIntegerField()

class result(models.Model):
	
	Name=models.CharField(max_length=30)
	Email=models.EmailField()
	Phone=models.BigIntegerField()
	difficult_breathing=models.CharField(max_length=30)
	chestpain=models.CharField(max_length=30)
	loss_of_speech=models.CharField(max_length=30)
	fever=models.CharField(max_length=30)
	dry_cough=models.CharField(max_length=30)
	tiredness=models.CharField(max_length=30)
	aches_and_pains=models.CharField(max_length=30)
	sore_throat=models.CharField(max_length=30)
	diarrhoea=models.CharField(max_length=30)
	conjunctivitis=models.CharField(max_length=30)
	headaches=models.CharField(max_length=30)
	loss_of_taste=models.CharField(max_length=30)
	rash_on_skin=models.CharField(max_length=30)
	
