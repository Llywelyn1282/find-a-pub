.phone_number was not appearing in database and throwing errors

after many attempts the fix was deleting the migrations, caches and database data and starting again.


persisting overflow issue on certain pages

after many attempts at locating and fixing the cause, the issue was found to be simply that certain rows were not contained within containers, thus breaking the bootstrap structure and causing overflow.