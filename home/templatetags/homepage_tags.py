from django import template
from CMS.models import BlogPage

register = template.Library()

@register.inclusion_tag('home/tags/top_stories.html')
def top_stories():
	blog_pages = BlogPage.objects.live().order_by('-latest_revision_at')
	return {
		'latest_histories': blog_pages
	}