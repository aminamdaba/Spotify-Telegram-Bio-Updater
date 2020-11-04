CLIENT_ID = "5052840a1252469281ffe0ec969d180b"
CLIENT_SECRET = "d93b42098ce04a88822dfbe306b6e6be"
API_ID = 1899108
API_HASH = "8de7de684ccd03109e6d30eaa98a4489"
INITIAL_TOKEN = "AQA8hOFPG8g9UhgiI0sRE40wIO9vCjBHJi5K808SIxUBh3hQYwaDwov7K31R8FsWrvN6GQ5tiite39k6kPGUTxz2JhKAs6wdAhwP28qjmNIjnSoveIvlbZMB4wy7wZ7xN7_WzbQ6ajrCxSqNU44BF715PPPb7ndQsrYTa_wt2H_VWkBCDKEvZMR0eKBcA82RTVoAi1fQgmXLa0H0bPbtX6iiKM5zWC0x5rhsBGFrf_vkfbb9y5h"
INITIAL_BIO = ""
LOG = "me"
# the escaping is necessary since we are testing against a regex pattern with it.
SHUTDOWN_COMMAND = "\/\/stop"
# The key which is used to determine if the current bio was generated from the bot ot from the user. This means:
# NEVER use whatever you put here in your original bio. NEVER. Don't do it!
KEY = '🎶'
# The bios MUST include the key. The bot will go though those and check if they are beneath telegrams character limit.
BIOS = [KEY + ' Now Playing: {interpret} - {title} {progress}/{duration}',
        KEY + ' Now Playing: {interpret} - {title}',
        KEY + ' : {interpret} - {title}',
        KEY + ' Now Playing: {title}',
        KEY + ' : {title}']
# Mind that some characters (e.g. emojis) count more in telegram more characters then in python. If you receive an
# AboutTooLongError and get redirected here, you need to increase the offset. Check the special characters you either
# have put in the KEY or in one of the BIOS with an official Telegram App and see how many characters they actually
# count, then change the OFFSET below accordingly. Since the standard KEY is one emoji and I don't have more emojis
# anywhere, it is set to one (One emoji counts as two characters, so I reduce 1 from the character limit).
OFFSET = 1
# reduce the OFFSET from our actual 70 character limit
LIMIT = 70 - OFFSET
