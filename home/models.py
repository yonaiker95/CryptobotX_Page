from django.db import models

# Create your models here.


class PaymentHistory(models.Model):
    username = models.CharField(max_length=15)
    monto = models.CharField(max_length=15)
    medio_de_pago = models.CharField(max_length=15)
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.username+' - $'+self.monto+' - '+self.medio_de_pago+' - '+self.status

    class Meta:
        db_table = "PaymentHistory"
