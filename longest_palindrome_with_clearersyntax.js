# rewritten for easier understanding

function longestPalindrome(str){
  var largest_left=0;
  var largest_right=0;
  
  for (var center=0; center<str.length; center++){
    var left = center;
    var right= center;
  
    // check odd length strings
    while (true){
      // make sure it's with right index of the 
      if ( (left<0) || (right> str.length-1)){
        break;
      }
      // if they're not equal break
      if (str[left]!=str[right]){
        break;
      } else {
        // update the values
        if (largest_right-largest_left < right-left ){
          largest_right=right;
          largest_left=left;
        }
      }
      left--;
      right++;
    }
    
    // check even length strings
    left = center;
    right= center+1;
    
    while (true){

      // if the two letters are not equal, no point for doing a palindrome check
      if (str[left]!== str[right]){
        break;
      }
      // make sure it's with right index of the 
      if ( (left<0) || (right> str.length-1)){
        break;
      }
      // if they're not equal break
      if (str[left]!=str[right]){
        break;
      } else {
        // update the values
        if (largest_right-largest_left < right-left ){
          largest_right=right;
          largest_left=left;
        }  
      }
      left--;
      right++;
    }
  }
  return str.slice(largest_left, largest_right+1);
}