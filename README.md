# Duolingo Leaderboard XP farm

#### How to use:

1. Make sure python is installed on your machine
1. Make sure python's selenium package is installed (pip install selenium)
1. Make sure to use the latest chrome driver (.exe) (or your browser's latest driver. Get chrome drivers [here](https://googlechromelabs.github.io/chrome-for-testing/#stable))
1. Make sure an english course is selected. The UI's language doesnt matter, but the course has to be english.
1. Provide your login data in constants\.py
1. Set the ITERS value in constants\.py (earned XP ≈ ITERS * 10, later ITERS * 5)
1. Run main\.py
1. Enjoy :)

#### Troubleshooting:

1. "Invalid password error message" - just run the code again. It happens rarely, no idea why...
1. "Nothing happens after login" - set COOKIES_ENABLED value to True in constants\.py