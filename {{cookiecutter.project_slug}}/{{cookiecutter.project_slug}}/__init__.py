{% if cookiecutter.add_celery == "yes"  %}

from .celery import app as celery_app

__all__ = ("celery_app",)
    
{% endif %}

    