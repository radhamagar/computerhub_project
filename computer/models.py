from django.db import models

# Create your models here.
class ComputerBrands(models.Model):
    brand_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='Media')
    def __str__(self):
        return self.brand_name

class ComputerSpecification(models.Model):
    generation = models.CharField(max_length=50)
    price_min = models.DecimalField(max_digits=10, decimal_places=2)
    price_max = models.DecimalField(max_digits=10, decimal_places=2)
    ram = models.PositiveIntegerField()
    brand = models.ForeignKey(ComputerBrands, on_delete=models.CASCADE, related_name='brand')

    def __str__(self):
        return f"{self.brand} {self.generation}"
    
class ComputerGeneration(models.Model):
    generation = models.CharField(max_length=50)

    def __str__(self):
        return self.generation

class Computer(models.Model):
    computer_code = models.CharField(max_length=50, unique=True)
    computer = models.ForeignKey(ComputerGeneration, on_delete=models.CASCADE,related_name='computer')
    quantity = models.PositiveIntegerField()
    unit_rate = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.unit_rate
        super(Computer, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.computer_code} ({self.computer.brand} {self.computer.generation})"


