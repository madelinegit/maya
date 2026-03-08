async function send() {
    const input = document.getElementById("msg")
    const chat = document.getElementById("chat")
    const text = input.value
    if (!text.trim()) return

    chat.innerHTML += `<div class="mb-2"><b>You:</b> ${text}</div>`
    input.value = ""

    const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text })
    })

    const data = await res.json()
    const reply = data.reply

    if (reply.startsWith("[IMAGE]") && reply.includes("[/IMAGE]")) {
        const url = reply.replace("[IMAGE]", "").replace("[/IMAGE]", "").trim()
        chat.innerHTML += `<div class="mb-2"><b>Maya:</b><br><img src="${url}" style="max-width:100%;border-radius:8px;margin-top:6px;"></div>`
    } else {
        chat.innerHTML += `<div class="mb-2"><b>Maya:</b> ${reply}</div>`
    }

    chat.scrollTop = chat.scrollHeight
}