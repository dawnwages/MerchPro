from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

#from modelcluster.fields import ParentalKey 
#from modelcluster.contrib.taggit import ClusterTaggableManager

from taggit.models import TaggedItemBase
from taggit.managers import TaggableManager

class BlogPageTag(TaggedItemBase):
	content_object = models.CharField(max_length=50, db_index=True)
	class Meta:
		verbose_name = "Tag"
		verbose_name_plural = "Tags"

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

	#def serve(self, request):
	#	#Get blogs
	#	blogs = BlogPage.objects.childof(self).live()
	#	#Filter by tag
	#	tag = request.GET.get('tag')
	#	if tag:
	#		blogs = blogs.filter(tags_name=tag)
#
#		return render(request, self.template, {
#			'page': self,
#			'blogs': blogs,
#			})

class BlogPage(Page):
    date = models.DateField("Post date")
    feature_image = models.ForeignKey('wagtailimages.Image',
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
    tags = TaggableManager(through=BlogPageTag, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('tags'),
        FieldPanel('body', classname="full"),
        ImageChooserPanel('feature_image'),
        ImageChooserPanel('thumbnail_image'),
    ]
