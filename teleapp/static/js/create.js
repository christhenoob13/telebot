function Alert(status, message){
  Swal.fire({
    position: 'center',
    icon: status,
    html: message,
    showConfirmButton: false,
    timer: 1500
  });
}

const create_bot = async () => {
  const token = document.getElementById('token');
  const admin = document.getElementById('admin');
  const prefix = document.getElementById('prefix');
  const commands = [...document.querySelectorAll('.commands')]
    .filter(cmd => cmd.checked)
    .map(cmd => cmd.value);
  const events = [...document.querySelectorAll('.events')]
    .filter(ev => ev.checked)
    .map((ev) => ev.value);
  
  if (!token.value) return Alert("error", "Missing bot token value");
  if (!admin.value) return Alert("error", "Missing AdminID value");
  if (commands.length < 1) return Alert("error", "Please select a commands at least one")
  
  try{
    const response = await fetch(`/api/create-bot`, {
      method: 'POST',
      headers: {
        "Content-Type": 'application/json'
      },
      body: JSON.stringify({
        token: token.value,
        admin: admin.value,
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