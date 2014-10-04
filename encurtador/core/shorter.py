import hashlib

def to_short(url):
  return hashlib.md5(url).hexdigest()[:7]
