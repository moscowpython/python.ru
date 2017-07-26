Contributing
============

::

    $ virtualenv python.ru --python=python3.5
    $ source python.ru/bin/activate
    $ git clone git@github.com:moscowpython/python.ru.git python_ru
    $ cd python_ru
    $ git checkout feature/launch  # remove after merging in master
    $ pip install -r requirements.txt
    $ python manage.py migrate

    # Loading development fixtures
    $ python manage.py loaddata fixtures/development.json
    # Some images to work with
    $ cp -R fixtures/media/ media/

    $ python manage.py runserver

    # Creating admin account, regular password strength validation applies!
    $ python manage.py createsuperuser --username admin --email=team@python.ru


