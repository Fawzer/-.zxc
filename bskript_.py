import bcrypt
import time
import my_def

start_time = time.time()

hashed = b"$2a$09$3DM3M4SLHBcFfoOJ6HGDTugM9YOOf6lIJWJ32C/4Q808K4rcLud7m"

for password in range(1000):
    print("{:03d}".format(password))

    if bcrypt.checkpw(bytes("{:03d}".format(password), "utf-8"), hashed):
        print(password)
        print("It Matches!")
        break

print("--- %s seconds ---" % (time.time() - start_time))

print()
print("UNIX time (down)")
print(print(start_time))