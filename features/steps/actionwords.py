# encoding: UTF-8
from behave import *
from src.coffee_machine import CoffeeMachine

class Actionwords:
    def __init__(self):
        self.sut = CoffeeMachine()
        self.handled = []

    def i_start_the_coffee_machine_using_language_lang(self, lang = "en"):
        self.sut.start(lang)

    def a_notification_about_descaling_is_displayed(self):
        assert self.sut.is_descaling_needed() is True

    def i_shutdown_the_coffee_machine(self):
        self.sut.stop()

    def message_message_should_be_displayed(self, message):
        assert (self.sut.message == message) is True

    def coffee_should_be_served(self):
        assert self.sut.coffee_served is True

    def coffee_should_not_be_served(self):
        assert self.sut.coffee_served is False

    def i_take_a_coffee(self):
        self.sut.take_coffee()

    def i_empty_the_coffee_grounds(self):
        self.sut.empty_grounds()

    def i_fill_the_beans_tank(self):
        self.sut.fill_beans()

    def i_fill_the_water_tank(self):
        self.sut.fill_tank()

    def i_take_coffee_number_coffees(self, coffee_number = 10):
        coffee_number = int(coffee_number)

        while (coffee_number > 0):
            self.i_take_a_coffee()
            coffee_number = coffee_number - 1

            if 'water' in self.handled:
                self.i_fill_the_water_tank()

            if 'beans' in self.handled:
                self.i_fill_the_beans_tank()

            if 'grounds' in self.handled:
                self.i_empty_the_coffee_grounds()

    def the_coffee_machine_is_started(self):
        self.i_start_the_coffee_machine_using_language_lang()

    def i_handle_water_tank(self):
        self.handled.append('water')

    def i_handle_beans(self):
        self.handled.append('beans')

    def i_handle_coffee_grounds(self):
        self.handled.append('grounds')

    def i_handle_everything_except_the_water_tank(self):
        self.i_handle_coffee_grounds()
        self.i_handle_beans()

    def i_handle_everything_except_the_beans(self):
        self.i_handle_water_tank()
        self.i_handle_coffee_grounds()

    def i_handle_everything_except_the_grounds(self):
        self.i_handle_water_tank()
        self.i_handle_beans()

    def displayed_message_is(self, free_text = ""):
        self.message_message_should_be_displayed(message = free_text)

    def i_switch_to_settings_mode(self):
        self.sut.show_settings()

    def settings_should_be(self, datatable = "||"):
        # Apparently, no way to get the raw table and assert_equals does not work that much ...
        expected = [datatable.rows[0].headings]
        for row in datatable.rows:
            expected.append([c for c in row])

        assert (expected == [[str(k), str(v)] for k, v in self.sut.get_settings().items()]) is True
