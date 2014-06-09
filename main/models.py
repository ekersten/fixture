from django.db import models

class Group(models.Model):
	name = models.CharField(max_length=1)

	def __unicode__(self):
		return self.name


class Country(models.Model):
	class Meta:
		verbose_name_plural = 'countries'

	name = models.CharField(max_length=100)
	flag = models.ImageField(upload_to='flags', null=True, blank=True)
	abbr = models.CharField(max_length=3)
	group = models.ForeignKey(Group)

	def __unicode__(self):
		return self.name

class Match(models.Model):
	class Meta:
		verbose_name_plural = 'matches'

	home = models.ForeignKey(Country, related_name='team_home')
	away = models.ForeignKey(Country, related_name='team_away')
	datetime = models.DateTimeField(verbose_name='Date')

	def __unicode__(self):
		return self.home.name + ' vs. ' + self.away.name + ' [' + self.datetime.strftime('%d/%m %H:%M') + ']'