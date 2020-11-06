using System.Diagnostics;
using System.Text;

public static class RotationalCipher
{
    public static string Rotate(string text, int shiftKey)
    {
      shiftKey = shiftKey % 26;

      var rotated = new StringBuilder(text.Length);
      foreach(var character in text)
      {
        rotated.Append(Rotate(character, shiftKey));
      }

      return rotated.ToString();
    }

    private static char Rotate(char c, int shiftKey)
    {
      // pre-conditions
      Debug.Assert(0 <= shiftKey && shiftKey < 26);

      if(c >= 'a' && c <= 'z')
        return (char)(((int)(c - 'a') + shiftKey) % 26 + 'a');
      else if(c >= 'A' && c <= 'Z')
        return (char)(((int)(c - 'A') + shiftKey) % 26 + 'A');
      else
        return c;
    }
}
