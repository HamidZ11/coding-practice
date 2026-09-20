function maskEmail(email) {
  let atIndex = email.indexOf("@");
  let username = email.slice(0, atIndex); // "@" is the separator
  let domain = email.slice(atIndex);

  let maskedUsername = username[0] + "*".repeat(username.length - 2) + username[username.length - 1];
  // first char of username + "*" for the length - 2 + last char of username

  return maskedUsername + domain;
}

let email = "apple.pie@example.com";

console.log(maskEmail(email));