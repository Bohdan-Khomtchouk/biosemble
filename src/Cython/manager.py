# Copyright (C) 2017 Bohdan Khomtchouk
# This file is part of biosemble.

# -------------------------------------------------------------------------------------------

from similarity import main
from datetime import datetime

pre = datetime.now()
main()
print(datetime.now() - pre)
