function myFun(flag) {
    // get the text from the textarea 
    var node1 = document.getElementById('text-plain-1');
    var node2 = document.getElementById('text-encrypted');
    if(flag) {
        // get the text from the textarea if decrypt
        node1 = document.getElementById('text-plain-2');
        node2 = document.getElementById('text-decrypted');
    }
    
    var text = node1.textContent;
    
    // variable to store the encrypted/decrypted text
    var encrypted = '';

    // loop through the text
    for (var i = 0; i < text.length; i++) {
        // get the character code of the current character
        var char = text[i];
        // check if the character is a letter
        if (char.match(/[a-z]/i)) {
            // get the character code of the current character
            var code = char.charCodeAt(0);
            // check if the character is lowercase
            if (code >= 97 && code <= 122) {
                // apply the shift
                code = 122 - code + 97;
            }
            // check if the character is upper case
            else if(code >= 65 && code <= 90) {
                // apply the shift
                code = 90 - code + 65;
            }
            // get the new character
            char = String.fromCharCode(code);
        }
        // add the character to the encrypted/decrypted text
        encrypted += char;
    }
    // set the encrypted/decrypted text
    node2.innerHTML = encrypted;
}

// get the encrypt button element
var encrypt_button = document.getElementById('click-encrypt');
// add the click event listener
encrypt_button.onclick = function(){myFun(0)};

// get the decrypt button element
var decrypt_button = document.getElementById('click-decrypt');
// add the click event listener
decrypt_button.onclick = function(){myFun(1)};