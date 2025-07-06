import "bootstrap"
import htmx from "htmx.org"
import "htmx-ext-ws"
import "../scss/global.scss"


window.htmx = htmx

import "./autoresizeTextArea"

document.addEventListener("htmx:wsAfterMessage", () => {
  const messagesDiv = document.getElementById("message-list");

  messagesDiv.scrollTop = messagesDiv.scrollHeight;
})
