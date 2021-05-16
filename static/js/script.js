function password_check(){

    name_ = document.getElementById("nameInput");
    if (String(name_.value).length < 1){
      alert('Введите нормальное имя');
    }
  
    pass = document.getElementById("inputPassword");
    if (String(pass.value).length < 7){
      alert('Пароль слишком короткий');
    }
  
  }
    
      