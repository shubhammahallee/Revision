from Pages.Page01 import Page01

def test_Case01(setup):

    lp = Page01(setup)#

    lp.test_verify_title()
    lp.test_radio_button()
    lp.test_text_box()
    lp.test_dropdown_button()
    lp.test_select_items()
    lp.test_toggle_switch()
    lp.test_switch_window()
    lp.test_switch_tab()
    lp.test_switch_to_alert()
    lp.test_random_wait()
    lp.test_mouse_hover()
    lp.test_drag_and_drop()
    lp.test_double_click()
    lp.test_click_hold()

