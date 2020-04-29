import hashlib

# Floyd's algorithm (https://en.wikipedia.org/wiki/Cycle_detection)
# We want to find collisions between two strings that begin with this prefix.

my_prefix = '\x41\x61\x99'

# Get the first x bytes of the double md5 hash value
def hash_function(message, x=14, prefix='\x41\x61\x99', debug=False):
  temp_hash = hashlib.md5(hashlib.md5(prefix + message).digest()).digest()

  if debug is True:
    print(message, x, prefix, temp_hash)

  return temp_hash[:x]


def hash_function2(message, x=14, prefix='\x41\x61\x99', debug=False):
  temp_hash = hashlib.md5(hashlib.md5(prefix + message).digest()).hexdigest()

  if debug is True:
    print(message, x, prefix, temp_hash)

  return temp_hash[:x]


def floyd(x, initial):
  # Set a few temp values to zero or none
  x0 = initial
  m0 = None
  m1 = None

  # Start
  tortoise = hash_function(x0, x, my_prefix)
  hare = hash_function(tortoise, x, my_prefix)


  # First loop until our hashes are equal
  while tortoise != hare:
    tortoise = hash_function(tortoise, x, my_prefix)
    hare   = hash_function(hash_function(hare, x, my_prefix), x, my_prefix)

  # Set pointer to initial value
  tortoise = x0
  
  # Secound loop 
  while tortoise != hare:
    m0 = tortoise

    tortoise = hash_function(tortoise, x, my_prefix)
    hare = hash_function(hare, x, my_prefix)

  # Loop many times until get second value
  hare = hash_function(tortoise, x, my_prefix)

  while tortoise != hare:
    m1 = hare
    hare = hash_function(hare, x, my_prefix)

  # Save results to the file
  save_results(m0, m1, hash_function(m0, x, my_prefix), hash_function2(m0, x*2, my_prefix))


def save_results(m0, m1, hash1, hash2):
  """Save results to file."""

  with open("message0.bin", "wb") as file:
    # Save first message:
    file.write(my_prefix + m0)

  with open("message1.bin", "wb") as file:
    # Save second message:
    file.write(my_prefix + m1)

  with open("hash_1.bin", "wb") as file:
    # Save bianry hash of messages:
    file.write(hash1)

  with open("hash_2.txt", "w") as file:
    # Save of messages:
    file.write("Message 1:\n")
    file.write(my_prefix + m0)

    file.write("\n\nMessage 2:\n")
    file.write(my_prefix + m1)

    file.write("\n\nHash:\n")
    file.write(hash2)


# Execute floyd funtion with initial value
floyd(x=7, initial="123hsdshd9fh933")


"""
0x416199 -> 4284825

Message A: 42848253cf02b27a4a781
Message B: 42848259dd4879a8d98bb
They both hash to: 0a05085732df91


"""
