from django.db import models

class KindQuerySet(models.QuerySet):
    def emails(self):
        return self.filter(kind=self.model.EMAIL)

class KindContactManager(models.Manager):
    def emails(self):
        return self.filter(kind=self.model.EMAIL)
    
    def phones(self):
        return self.filter(kind=self.model.PHONE)