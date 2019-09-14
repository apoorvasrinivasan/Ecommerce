

  144  source ../../venv/django/bin/activate
  146  python manage.py startapp common
  147  mkdir templates
  148  touch templates/index.html
  156  pip install pypugjs
  157  mv templates/index.html templates/index.pug
  158  pip install libsass django-compressor django-sass-processor
  159  mkdir static
  169  pip install django-coffeescript
  181  sudo npm -g install coffee-script
  184  pip install django-static-precompiler
  185  migrate static_precompiler
  186  python manage.py migrate static_precompiler
