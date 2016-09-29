# Forest Service Prototype
This is a Django application to test out an online permit of the non-commercial group use Forest Service permit.

## Guiding documents

This non-commercial group use permit prototype is being developed as part of initial, discovery research for a broader Forest Service ePermitting project. Read more in the [discovery plan](https://github.com/18F/forest-service-prototype/raw/master/docs/discovery-plan.pdf).

In general, this prototype is driven by the goals, users and features set forward at a special uses permitting kick-off workshop. Read more in the [special uses workshop summary](https://github.com/18F/forest-service-prototype/raw/master/docs/special-uses-read-out.pdf). In a few weeks, we will kick off a similar discovery effort for Christmas tree permits. Read more in the [Christmas tree workshop summary](https://github.com/18F/forest-service-prototype/raw/master/docs/christmas-tree-read-out.pdf).

For the clearest view of issue priorities and status, check [this Waffle board](https://waffle.io/18F/forest-service-prototype).

## Local Installation

This app is designed to run on Python 3.5.2. `pyenv` is recommended for managing
your Python version, along with `pyenv-virtualenvwrapper` for managing the
dependencies installed with `pip`. With that, you can prepare your development
environment by running:

```
git clone https://github.com/18f/forest-service-prototype.git
cd forest-service-prototype
mkvirtualenv forest-service-prototype
pip install -r requirements.txt
createdb forest-service-prototype
cd forestserviceprototype
./manage.py migrate
./manage.py runserver
```

The app should now be running at http://localhost:8000.

## Contributing

Please read through our [contributing guidelines](CONTRIBUTING.md). These guidelines are directions for opening issues and submitting pull requests, and they also detail the coding and design standards we follow.

## Public domain

This project is in the worldwide [public domain](LICENSE.md). As stated in [CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.
