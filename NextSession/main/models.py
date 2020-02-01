from django.db import models


# Create your models here.
class CharDescription(models.Model):
    char_name = models.CharField(max_length=100)
    char_level = models.IntegerField()
    char_exp = models.IntegerField()
    char_race = models.CharField(max_length=20)
    char_class = models.CharField(max_length=30)
    char_alignement = models.CharField(max_length=2)
    char_size = models.CharField(max_length=1)
    char_shortbio = models.TextField()

    def __str__(self):
        return self.char_name


class BaseStatus(models.Model):
    char_str = models.IntegerField()
    char_dex = models.IntegerField()
    char_con = models.IntegerField()
    char_int = models.IntegerField()
    char_wis = models.IntegerField()
    char_cha = models.IntegerField()


class CombatStatus(models.Model):
    Life_Points = models.IntegerField()
    weapon_one = models.CharField(max_length=15, blank=True, null=True)
    weapon_two = models.CharField(max_length=15, blank=True, null=True)
    weapon_three = models.CharField(max_lengt=15, blank=True, null=True)
    weapon_four = models.CharField(max_length=15, blank=True, null=True)

    shield = models.CharField(max_length=15, blank=True, null=True)
    armor = models.CharField(max_length=15, blank=True, null=True)
    protection_one = models.CharField(max_length=15, blank=True, null=True)
    protection_two = models.CharField(max_length=15, blank=True, null=True)


class CharSkills(models.Model):
    skill_name = models.CharField(max_length=15)
    skill_mod = models.CharField(max_length=3)
    skill_graduation = models.IntegerField()






