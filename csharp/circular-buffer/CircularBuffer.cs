using System;
using System.Diagnostics;

public class CircularBuffer<T>
{
    private T[] _items;
    private int _readIndex = 0;
    private int _writeIndex = 0;
    private bool _isFull = false;

    public CircularBuffer(int capacity)
    {
      if(capacity < 1)
        throw new ArgumentException();

      _items = new T[capacity];
    }

    public T Read()
    {
      if(IsEmpty)
        throw new InvalidOperationException();

      var item = ExchangeWithDefault(_readIndex);
      FinalizeRead();

      return item;
    }

    public void Write(T value)
    {
      if(_isFull)
        throw new InvalidOperationException();

      _items[_writeIndex] = value;
      FinalizeWrite();
    }

    public void Overwrite(T value)
    {
      if(_isFull)
        Read(); // "dummy" read
      
      Debug.Assert(!_isFull);
      Write(value);
    }
    
    public void Clear()
    {
      _readIndex = 0;
      _writeIndex = 0;
      _isFull = false;
      
      // todo: could be optimized by defaulting only thouse items that are set
      for(var i = 0; i < Capacity; ++i) 
        _items[i] = default(T);
    }

    public bool IsEmpty => (_readIndex == _writeIndex) && !_isFull;

    public int Capacity => _items.Length;

    private void FinalizeRead()
    {
      AdvanceIndex(ref _readIndex);
      _isFull = false;
    }

    private void FinalizeWrite()
    {
      AdvanceIndex(ref _writeIndex);
      if(_writeIndex == _readIndex)
        _isFull = true;
    }

    private void AdvanceIndex(ref int index)
    {
      index = ++index % Capacity;
    }

    private T ExchangeWithDefault(int index)
    {
      var item = _items[index];
      _items[index] = default(T);
      return item;
    }
}
