let messageContainer = document.querySelector("#message");
let submitButton = document.querySelector("#submit");
messageContainer.textContent = "";

submitButton.addEventListener("click", (e) => {
  // e.preventDefault();
  messageContainer.textContent = "";
  // send data
  //client feedback success
  messageContainer.textContent = "Successful ✔️";
});
