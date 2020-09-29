function generateHashtag (str) {
  // This function takes a string and returns the hashtag equivalent
  // (e.g. Codewars => #CodeWars)
  
  // trimming and replacing all double spaces with just one space
  let trimmedStr = str.trim().replace(/  +/g, ' ').toLowerCase();
  
  // Returning false if string is blank or over 140 characters
  if (trimmedStr == '' || trimmedStr.length + 1 > 140) { return false }
  
  // Title Casing each word in the string
  let titleCaseStr = trimmedStr.split(' ').map( word => { 
    return word[0].toUpperCase() + word.slice(1)
  });
  
  // Returning final hashtag
  return '#' + titleCaseStr.join('')
}
