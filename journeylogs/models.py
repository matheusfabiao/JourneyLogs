from django.db import models

# Create your models here.
class Topic(models.Model):
    """Um assunto sobre qual o usuário está aprendendo."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em String do modelo."""
        if len(str(self.text)) > 50:
            return self.text[:50] + '...'
        else:
            return self.text
