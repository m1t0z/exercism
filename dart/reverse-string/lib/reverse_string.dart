// NOTE: supports only Basic Multilingual Plane (BMP) subset of the Unicode,
// thus will not work correctly with 4 byte surrogate pairs.
String reverse(String str) {
  var sb = StringBuffer();
  for (var i = str.length - 1; i >= 0; i--) {
    sb.write(str[i]);
  }
  return sb.toString();
}
