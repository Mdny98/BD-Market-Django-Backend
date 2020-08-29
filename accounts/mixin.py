from django.shortcuts import get_object_or_404, redirect
from blog.models import Article
class FieldsMixin():
	def dispatch(self, request, *args, **kwargs):
		self.fields = [
			"title", "slug", "category",
			"description", "image", "publish"
		]
		if request.user.is_superuser:
			self.fields.append("author")
			self.fields.append("status")
   
		return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
	def form_valid(self, form):
		if self.request.user.is_superuser:
			form.save()
		elif self.request.user.is_staff:
			self.obj = form.save()
			self.obj.author = self.request.user
			self.obj.status = 'np'
		return super().form_valid(form)

class SuperUserAccessMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404("You can't see this page.")

class AuthorsAccessMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			if request.user.is_superuser:
				return super().dispatch(request, *args, **kwargs)
			else:
				return redirect("accounts:profile")
		else:
			return redirect("login")


class AuthorAccessMixin():
	def dispatch(self, request, pk, *args, **kwargs):
		article = get_object_or_404(Article, pk=pk)
		if article.author == request.user and article.status in 'NP' or\
		request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404("You can't see this page.")


