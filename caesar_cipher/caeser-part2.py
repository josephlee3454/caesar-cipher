def encrypt(plain_text, key):
  out_text = []
  crypt_text = []

  upp = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]
  low = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
# print(upp)
# print(low)
  for char in plain_text:
    if char in upp:
      index = upp.index(char)
      crypting = (index + key)% 26
      crypt_text.append(crypting)
      new_letter = upp[crypting]
      out_text.append(new_letter)
    elif char in low:
      index = low.index(char)
      crypting = (index + key)% 26
      crypt_text.append(crypting)
      new_letter = low[crypting]
      out_text.append(new_letter)
  return out_text

if __name__ == "__main__":
  encrypt('abc',2)
# print(encrypt('abc', 2))


