// script.js file
document.getElementById("registerBtn").addEventListener("click", function() {
    var nameInput = document.getElementById("nameInput");
    if (nameInput.value.trim() === "") {
        alert("Please enter your name.");
        nameInput.focus();
        return false;
    }
    // Proceed with registration logic here
});

function submitForm() {
    var name = document.getElementById("nameInput").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/process_input", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        alert(response.message);
      }
    };
    xhr.send(JSON.stringify({ "name": name }));
  }