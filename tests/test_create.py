
from core.models import AddedInfo, Agent, Camera, Domain, Entry, MetaData, Category
import pytest


# fixtures
@pytest.fixture
def domain1(db):
    domain =  Domain.objects.create(
                            domain='subdomai', 
                            description='DESCRIPTION',
                            active = False
                            )

    domain.full_clean()
    domain.save()
    return domain

@pytest.fixture
def agent1(domain1):
    agent = Agent.objects.create(

    name = 'AGENT1',
    uid = 'WXCWJUBGWI4525QLPBG2ILWKZC348TFKQRGQM76Y',
    description = 'DESCRIPTION1',
    linked_email_account = 'agent@gmail.com',
    address = 'address 1',
    geolocation = '-33.45430930000001,-70.5964762',
    domain = domain1,
    ssh_reverse_ip = '192.168.1.1',
    ssh_reverse_port = 8080,
    ssh_key_file_name = 'file.txt',
    config_added_info = '{"key":1}',
    config_ui = '{"key":1}'
    
    )
    agent.full_clean()
    agent.save()
    return agent

@pytest.fixture
def category1(agent1):

    category = Category.objects.create(
            name = 'CATEGORY1',
            agent = agent1
            )
    category.full_clean()
    
    category.save()
    return category

@pytest.fixture
def cam1(agent1):
    cam = Camera.objects.create(

        name = 'CAM1',
        camera_id = 123456,
        agent = agent1,
        local_link = 'http://google.com',

    )
    cam.full_clean()
    cam.save()
    return cam

@pytest.fixture
def meta1():
    meta = MetaData.objects.create(

        meta_data = '{"key":1}'
    )
    meta.full_clean()
    meta.save()
    return meta


#test crate objects
# Domain

@pytest.mark.django_db()
def test_create_domain():
    domain =  Domain.objects.create(
                            domain='subdomain', 
                            description='DESCRIPTION',
                            active = False
                            )

    domain.full_clean()
    domain.save()


# MetaData

@pytest.mark.django_db()
def test_create_metadata():
    metadatas = MetaData.objects.create(
            meta_data = '{"key":1}'
            )
    metadatas.full_clean()
    
    metadatas.save()

# Agent

@pytest.mark.django_db()
def test_create_agent(domain1):

    agent = Agent.objects.create(

    name = 'AGENT1',
    uid = 'WXCWJUBGWI4525QLPBG2ILWKZC348TFKQRGQM76Y',
    description = 'DESCRIPTION1',
    linked_email_account = 'agent@gmail.com',
    address = 'address 1',
    geolocation = '-33.45430930000001,-70.5964762',
    domain = domain1,
    ssh_reverse_ip = '192.168.1.1',
    ssh_reverse_port = 23,
    ssh_key_file_name = 'file.txt',
    config_added_info = '{"key":1}',
    config_ui = '{"key":1}'
    

    )
    agent.full_clean()
    agent.save()

#Category

@pytest.mark.django_db()
def test_create_category(agent1):

    category = Category.objects.create(
            name = 'CATEGORY1',
            agent = agent1
            )
    category.full_clean()
    
    category.save()

# Camera

@pytest.mark.django_db()
def test_create_camera(agent1):
    camera = Camera.objects.create(
        name = 'CAMERA1',
        camera_id = 12345678,
        agent = agent1,
        local_link = 'https://mail.google.com/',
        
    )
    camera.full_clean()
    camera.save()

# AddedInfo
@pytest.mark.django_db()
def test_create_addedinfo(category1):
    addedinfo = AddedInfo.objects.create(
    plate = 'ABCD1234',
    driver_name = 'NAME LASTNAME',
    driver_id = '12345678-1',
    category = category1,
    custom_fields = '{"key":1}'

    )
    addedinfo.full_clean()
    addedinfo.save()

#Entry
@pytest.mark.django_db()
def test_create_entry(cam1, category1, agent1, meta1):
    entry = Entry.objects.create(
    plate = '1234ABCD',

    camara = cam1,
    agent = agent1,
    
    confidence = 1.1,
    travel_direction = 300.0,

    vehicle = '{"key":1}',
    
    is_parked = True,
    is_preview = True,
    vehicle_detected = True,
    
    best_uuid = '123456789123456789',
    link_image = 'https://mail.google.com/',
    image = 'gfhffghfghttet2gdfkjfgjasff',
    crop_image = 'iusjhdilfj9wekjdfoiuvcdoilvd9slijfdopifdf',

    driver_name = 'NAME LASTNAME',
    driver_id = '123456-8',
    category = category1,
    custom_fields = '{"key":1}',

    meta_data = meta1

    )

    