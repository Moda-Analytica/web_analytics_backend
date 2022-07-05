import pytest

from app.schemas.contact import ContactSchema
from app.schemas.infographics import InfographicSchema
from app.schemas.push_notification import PushNotificationSchema
from app.schemas.runinstance import RunInstanceSchema
from app.schemas.sectors import SectorSchema
from app.schemas.subsectors import SubSectorSchema


def test_contact_schema():
    contact = ContactSchema(first_name="test", last_name="test",
                            email="test@gmail.com", subject="test sub", message="test message")

    assert contact.first_name == "test"
    assert contact.last_name == "test"
    assert contact.email == "test@gmail.com"
    assert contact.subject == "test sub"
    assert contact.message == "test message"


def test_infographic_schema():
    infographic = InfographicSchema(
        sector="test sec", title="test title", description="test desc", report="test url")

    assert infographic.sector == "test sec"
    assert infographic.title == "test title"
    assert infographic.description == "test desc"
    assert infographic.report == "test url"


def test_push_notification_schema():
    notification = PushNotificationSchema(
        title="notification title", body="notification body")

    assert notification.title == "notification title"
    assert notification.body == "notification body"


def test_run_instance_schema():

    runinstance = RunInstanceSchema(
        _id="123", metrics_added=10, sectors_added=9, start_run_time="startruntimestr")

    assert runinstance.id == "123"
    assert runinstance.metrics_added == 10
    assert runinstance.sectors_added == 9
    assert runinstance.start_run_time == "startruntimestr"


def test_sector_schema():
    sector = SectorSchema(_id=1, name="sector test", description="sector desc")

    assert sector.id == 1
    assert sector.name == "sector test"
    assert sector.description == "sector desc"


def test_subsector_schema():
    subsector = SubSectorSchema(_id="123", metric="test metric", description="test desc",
                                sector="education", value_type="test value", reference="test ref.", report="test report")

    assert subsector.id == "123"
    assert subsector.metric == "test metric"
    assert subsector.description == "test desc"
    assert subsector.sector == "education"
    assert subsector.value_type == "test value"
    assert subsector.reference == "test ref."
    assert subsector.report == "test report"
