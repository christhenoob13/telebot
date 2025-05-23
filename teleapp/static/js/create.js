function Alert(className, message){
  const div = document.getElementById('respo-message');
  div.className = className;
  div.innerHTML = message
}

async const create_bot = () => {
  const token = document.getElementById('token');
  const botadmin = document.getElementById('botadmin');
  const commands = [...document.querySelectorAll('.commands')]
    .filter(cmd => cmd.checked)
    .map(cmd => cmd.value);
  const events = [...document.querySelectorAll('.events')]
    .filter(ev => ev.checked)
    .map((ev) => ev.value);
  
  try{
    const response = await fetch(`/api/create-bot`, {
      method: 'POST',
      headers: {
        "Content-Type": 'application/json'
      },
      body: JSON.stringify({
        token: token.value,
        botadmin: botadmin.value,
        prefix: prefix.value,
        commands: commands,
        events: events
      })
    })
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const res = await response.json();
    if (res) // ituloy
    Alert("alert alert-success", `<b>NAME: </b>${res.name}<br> <b>ID: </b>${res.id}`)
  }catch(err){
    console.log("ERROR: ", err)
  }
}