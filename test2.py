# import pywinauto
# desktop = pywinauto.Desktop(backend="uia")
# window = desktop.windows(title_re=".* Google Chrome$", control_type="Pane")[0]
# wrapper_list = window.descendants(control_type="TabItem")
# for wrapper in wrapper_list:
#     wrapper.click_input()
#     wrapper_url = window.descendants(title="Address and search bar", control_type="Edit")[0]
#     print(wrapper_url.get_value())
import datetime
from browser_history import get_history

outputs = get_history()

# his is a list of (datetime.datetime, url) tuples
his = outputs.histories
for h in his[::-1]:
    print(h[0])
    substring = h[1][h[1].find('https://') + len('https://'):h[1].find("/", h[1].find('https://') + len('https://'))]
    print(substring)
    print("")
    print(h[0].replace(tzinfo=None))
    print(datetime.datetime(2023, 8, 9, 4, 0, 0))
    if h[0].replace(tzinfo=None) < datetime.datetime(2023, 8, 9, 4, 20, 0):
        break

