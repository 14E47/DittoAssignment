from django.db import models


# Create your models here.
class Campaign(models.Model):
    # Each Campaign has    'Subject', 'preview_text', 'article_url', 'html_content', 'plain_text_content', 'published_date'
    slug = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    preview_text = models.TextField(blank=False)
    article_url = models.URLField(max_length=200)
    html_content = models.TextField(blank=True, Null=True)
    plain_text_content = models.TextField(blank=False)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Published Date:{self.published_date}, Subject: {self.subject}"

    class Meta:
        verbose_name = "Campaign"
        verbose_name_plural = "Campaigns"
        ordering = ('published_date',)
