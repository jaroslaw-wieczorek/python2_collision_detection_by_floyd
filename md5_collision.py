import hashlib

# Floyd's algorithm (https://en.wikipedia.org/wiki/Cycle_detection)
# We want to find collisions between two strings that begin with this prefix.

my_prefix = "4284825"

# Get the first x bytes of the double md5 hash value
def hash_function(message, x=14, prefix="4284825", debug=False):
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
  save_results(m0, m1, hash_function(m0, x, my_prefix))


def save_results(m0, m1, hash):
  """Save results to file."""

  with open("moja_kolizja.txt", "w") as file:
    # Save first message:
    file.write(my_prefix + m0)
    file.write("\n")

    # Save second message:
    file.write(my_prefix + m1)
    file.write("\n")

    # Save hash
    file.write(hash)
    file.write("\n")


# Execute floyd funtion with initial value
floyd(x=14, initial="123hsdshd9fh933")


"""
0x416199 -> 4284825

Message A: 42848253cf02b27a4a781
Message B: 42848259dd4879a8d98bb
They both hash to: 0a05085732df91


"""
