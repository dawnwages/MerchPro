from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

class BlogIndexPage(Page):
	intro = RichTextField(blank=True)

	content_panels = Page.content_panels + [
		FieldPanel('intro', classname="full")
	]
	def get_context(self, request):
    # Update context to include only published posts, 
    # in reverse chronological order
	    context = super(BlogIndexPage, self).get_context(request)
	    live_blogpages = self.get_children().live()
	    context['blogpages'] = live_blogpages.order_by('-first_published_at')
	    return context

class BlogPage(Page):
    date = models.DateField("Post date")
    feature_image = models.ForeignKey('wagtailImages.Image',
    	null=True,
    	blank=True,
    	on_delete=models.SET_NULL,
    	related_name='+')
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    thumbnail_image = models.ForeignKey(
    	'wagtailimages.Image',
    	null=True,
    	blank=True,
    	on_delete=models.SET_NULL,
    	related_name='+')
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]
