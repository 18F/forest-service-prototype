import factory
from datetime import datetime, timedelta, tzinfo
from dateutil.tz import tzlocal
from specialuseform.models import Permit


class PermitFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Permit

    event_name = factory.Faker('catch_phrase')
    organizer_address_1 = factory.Faker('street_address')
    city = factory.Faker('city')
    state = factory.Faker('state_abbr')
    zipcode = factory.Faker('zipcode')
    phone_daytime = factory.Faker('phone_number')
    description = factory.Faker('paragraph')
    location = factory.Faker('word')
    participant_number = factory.Faker('random_digit')
    spectator_number = factory.Faker('random_digit')
    start_date = factory.Faker(
        'date_time_between_dates',
        datetime_start=datetime.now(),
        datetime_end=datetime.now() + timedelta(days=2),
        tzinfo=tzlocal(),
    )
    end_date = factory.Faker(
        'date_time_between_dates',
        datetime_start=datetime.now() + timedelta(days=3),
        datetime_end=datetime.now() + timedelta(days=6),
        tzinfo=tzlocal(),
    )
    permit_holder_name = factory.Faker('name')
    permit_holder_address_1 = factory.Faker('street_address')
    permit_holder_city = factory.Faker('city')
    permit_holder_state = factory.Faker('state_abbr')
    permit_holder_zipcode = factory.Faker('zipcode')
