import pywinauto
desktop = pywinauto.Desktop(backend="uia")
window = desktop.windows(title_re=".* Google Chrome$", control_type="Pane")[0]
wrapper_list = window.descendants(control_type="TabItem")
for wrapper in wrapper_list:
    wrapper.click_input()
    wrapper_url = window.descendants(title="Address and search bar", control_type="Edit")[0]
    print(wrapper_url.get_value())