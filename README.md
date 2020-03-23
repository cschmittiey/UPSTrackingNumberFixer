# UPSTrackingNumberFixer
I had a lost package, and the shipper only gave me a truncated UPS tracking number (and didn't return my emails), so I wrote a script to bruteforce all the possible combinations and figure out where the package went.

You'll need an [EasyPost](https://www.easypost.com/) account and API key to search tracking numbers.

This script could probably be adapted to bruteforce all kinds of tracking numbers but there are some hardcoded settings for UPS currently.

This script assumes that you're missing 10 or less characters off of the end of the tracking number. 

The idea was to write this in a way that wasn't hard coded based on how many alphanumeric digits were missing, which was an exercise in thought for me.

This is just a one-day project, used to find one tracking number. I'm happy to take PRs and such but I don't plan to maintain this or anything in the future.

"A UPS tracking number, for domestic packages within the United States, will usually start with "1Z" followed by a 6 character shipper number (numbers and letters), a 2 digit service level indicator, and finally 8 digits identifying the package (the last digit being a check digit), for a total of 18 characters."
 - https://en.wikipedia.org/wiki/Tracking_number
 
 ## Usage 
 
 Install prereqs:
 ```
 pip3 install easypost
 ```
 
 Edit the API key and the partialTrackingNumber variable and you should be good to go once running the script.
