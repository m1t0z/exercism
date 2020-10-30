using System;
using System.Diagnostics;

public static class ReverseString
{
    public static string Reverse(string input)
    {
      // Use string.Create to avoid unnecessary temporal allocations.
      return string.Create(input.Length, input, (Span<char> strContent, string input) => {
          Debug.Assert(strContent.Length == input.Length);
          var len = input.Length;
          for(var i = 0; i < len; ++i)
            strContent[i] = input[len - i - 1];
        }
      );
    }
}
