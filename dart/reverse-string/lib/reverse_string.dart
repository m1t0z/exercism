String reverse(String str) {
  var sb = StringBuffer();
  for (var i = str.length - 1; i >= 0; i--) {
    sb.write(str[i]);
  }
  return sb.toString();
}
