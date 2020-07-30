def encrypt(plain_text, key):
  """   
    plain text will be the un-encrypted text
    key will be the shift number
    encrypt('abcd', 2)
    plain_text: abcd
    shift: 2
    --> cdef
  Args:
      plain_text (string): [the plain text that needs to be shifted]
      key (int): [number of shifts to make]
  """
  encrypted_text = ''
  print(f'the text is {plain_text}')
  for str_char in range(len(plain_text)):
    char = plain_text[str_char]
  
    # shifted_char_str =  str_char + key
    # encrypted_text += str(shifted_char_str)
  print(f'the encrpyted data with a shift of {key} is {encrypted_text}.')
  # print('#'*50)
  return encrypted_text

if __name__ == "__main__":
  assert encrypt('ABCD',2) == 'cdef'

