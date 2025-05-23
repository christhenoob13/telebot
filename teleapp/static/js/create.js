function Alert(status, message){
  const div = document.getElementById('respo-message');
  div.className = className === 'error' ?
    `alert alert-danger alert-dismissible` :
    `alert alert-success alert-dismissible`;
  div.innerHTML = `<button type="button" class="btn-close" data-bs-dismiss="alert"></button>${message}`
}

async const create_bot = () => {
  const token = document.getElementById('token');
  const botadmin = document.getElementById('botadmin');
  const prefix = document.getElementById('prefix');
  const commands = [...document.querySelectorAll('.commands')]
    .filter(cmd => cmd.checked)
    .map(cmd => cmd.value);
  const events = [...document.querySelectorAll('.events')]
    .filter(ev => ev.checked)
    .map((ev) => ev.value);
  
  if (!token.value) return Alert("error", "Invalid bot token value");
  
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
    const res = await response.json();
    if (res?.error){
      Alert("error", `<b>ERROR: </b>${res.error}`)
    }else{
      Alert("success", `<b>NAME: </b>${res.name}<br> <b>ID: </b>${res.id}`)
    }
  }catch(err){
    console.log("ERROR: ", err)
  }
}