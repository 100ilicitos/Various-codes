# Get Windows Version
# by Busyman.Inc

# pip install wmi

import wmi
data = wmi.WMI()
for os_name in data.Win32_OperatingSystem():
  print(os_name.Caption)
