
from demoqa_test.page.registration_page import RegistrationPage
from demoqa_test.model.conftest import open_browser

def test_registration(open_browser):
    registration_page = RegistrationPage()

    registration_page.first_name('Test')
    registration_page.last_name('Testovich')
    registration_page.email('testemeil@test.com')
    registration_page.gender('Male')
    registration_page.user_number('7999888445')
    registration_page.fill_date_of_birth('1993', 'July', '13' )
    registration_page.subjects('English')
    registration_page.hobbies('Sports')
    registration_page.current_address('Earth, Eurasia 4.8.15.22.43')
    registration_page.state('Haryana')
    registration_page.city('Karnal')
    registration_page.submit()
    registration_page.should_have_registered_user_with(
        'Test Testovich',
        'testemeil@test.com',
        'Male',
        '7999888445',
        '13 July,1993',
        'English',
        'Sports',
        'Earth, Eurasia 4.8.15.22.43',
        'Haryana Karnal')