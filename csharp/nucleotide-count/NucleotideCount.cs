using System;
using System.Collections.Generic;

public static class NucleotideCount
{
    public static IDictionary<char, int> Count(string sequence)
    {
      int cntA = 0;
      int cntC = 0;
      int cntG = 0;
      int cntT = 0;

      foreach(var nucleotide in sequence)
      {
        switch(nucleotide)
        {
          case 'A': cntA++; break;
          case 'C': cntC++; break;
          case 'G': cntG++; break;
          case 'T': cntT++; break;
          default: throw new ArgumentException();
        }
      }

      var dict = new Dictionary<char, int>();
      dict['A'] = cntA;
      dict['C'] = cntC;
      dict['G'] = cntG;
      dict['T'] = cntT;

      return dict;
    }
}
