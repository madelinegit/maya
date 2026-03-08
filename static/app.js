async function send() {

const input = document.getElementById("msg")
const chat = document.getElementById("chat")

const text = input.value

chat.innerHTML += `<div><b>You:</b> ${text}</div>`

const res = await fetch("/chat", {

method: "POST",

headers: {
"Content-Type": "application/json"
},

body: JSON.stringify({
message: text
})

})

const data = await res.json()

chat.innerHTML += `<div><b>Maya:</b> ${data.reply}</div>`

input.value = ""

}