def log(status: str, message: str, label=str|None) -> None:
  match status:
    case 'error':
      print(f"\033[41m{label if label else 'ERROR''} \033[0m{message}")
    case 'success':
      print(f"\033[42m{label if label else 'SUCCESS''} \033[0m{message}")
    case 'info':
      print(f"\033[46m{label if label else 'INFO''} \033[0m{message}")
    casr _:
      print(message)