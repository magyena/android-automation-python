import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.loginPages import PagesLogin
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.pages.settingsPages import SettingsPages
from MiradaVersion.test.id_Mirada_Login.login_by_phone import login_free_by_phone
from MiradaVersion.test.open_app import free_phone_data


@pytest.fixture(scope="module")
def driver():
    setup_appium = SetupAppium()
    driver = setup_appium.driver
    if not driver:
        pytest.fail("Driver initialization failed.")

    yield driver


@pytest.fixture(scope="module")
def sign_up_action(driver):
    return SignUp(driver)


@pytest.fixture(scope="module")
def homepage_action(driver):
    return HomePage(driver)


@pytest.fixture(scope="module")
def settings_action(driver):
    return SettingsPages(driver)


def test_TC_User_Can_Direct_to_Term_and_Condition(
    driver: WebDriver,
    free_phone_data,
    homepage_action: HomePage,
    settings_action: SettingsPages,
):
    login_free_by_phone(driver, free_phone_data)
    time.sleep(2)

    homepage_action.clickMenuButton()
    homepage_action.assertMenu()
    homepage_action.clickSettingsButton()
    homepage_action.assertSettingsPage()
    time.sleep(2)
    settings_action.clickLegalInformation()
    time.sleep(2)
    settings_action.assertLegalInformation()
    time.sleep(2)
    settings_action.clickTerms0fUse()
    time.sleep(5)
    driver.press_keycode(4)


def test_TC_User_Can_Direct_to_Privacy_and_Policy(
    driver: WebDriver,
    settings_action: SettingsPages,
):
    time.sleep(2)
    settings_action.assertLegalInformation()
    time.sleep(2)
    settings_action.clickPrivacyPolicy()
    time.sleep(5)
    driver.press_keycode(4)


def test_TC_User_Can_Direct_to_Software_Licenses(
    settings_action: SettingsPages,
):
    settings_action.assertLegalInformation()
    time.sleep(2)
    settings_action.clickSoftwareLicenses()
    time.sleep(2)
    settings_action.clickBacktoSettingsPage()
    time.sleep(2)
    settings_action.clickBacktoSettingsPage()


def test_TC_User_Can_Open_Help_Center(
    settings_action: SettingsPages,
):  
    time.sleep(2)
    settings_action.clickHelp()
    settings_action.assertHelpCenterPage()
    time.sleep(2)


def test_TC_User_Can_Open_Help_Center_Email(
    driver: WebDriver,
    homepage_action : HomePage,
    settings_action: SettingsPages,
): 
    print("in Email")
    # settings_action.clickEmailHelpCenter()
    # time.sleep(5)
    # driver.press_keycode(4)
    # driver.press_keycode(4)
    
    # time.sleep(2)


def test_TC_User_Can_Open_Help_Center_Whatsapp(
    driver: WebDriver,
    settings_action: SettingsPages,
):
    # settings_action.clickWhatsappHelpCenter()
    # time.sleep(5)
    # driver.press_keycode(4)
    time.sleep(2)
   


def test_TC_User_Can_Open_Help_Center_AboutUs(
    driver: WebDriver,
    settings_action: SettingsPages,
    homepage_action=HomePage,
):
    print("sebelum klik help about us")
    # driver.press_keycode[4]
    # time.sleep(2)
    # homepage_action.clickMenuButton()
    # homepage_action.clickSettingsButton()
    time.sleep(2)
    settings_action.clickAboutUSHelpCenter()
    time.sleep(2)
    driver.press_keycode(4)


def test_TC_User_Can_Open_Help_Center_Subscription(
    settings_action: SettingsPages,
):
    settings_action.clickSubscriptionHelpCenter()
    settings_action.assertSubscriptionPage()


def test_TC_User_Can_Open_Call_Center(
    settings_action: SettingsPages,
):
    time.sleep(2)
    settings_action.clickCallCenter()
    settings_action.clickCloseToSettings()
    time.sleep(2)


def test_TC_User_Can_see_Manage_Profiles(settings_action: SettingsPages):
    settings_action.clickManageProfiles()
    time.sleep(2)
    settings_action.assertManageProfiles()
    settings_action.clickBacktoSettingsPage()


def test_TC_User_Can_see_Notification(
    driver: WebDriver, settings_action: SettingsPages
):
    settings_action.clickNotification()
    time.sleep(2)
    settings_action.assertNotificationCentre()
    time.sleep(2)
    settings_action.clickBackSettings()
    time.sleep(2)
    
def test_TC_User_Can_Logiut(
    driver: WebDriver, settings_action: SettingsPages
):
    
    settings_action.clickSettingsProfile()
    settings_action.assertSettingsAccountPage()
    time.sleep(2)
    settings_action.clickLogoutButton()
