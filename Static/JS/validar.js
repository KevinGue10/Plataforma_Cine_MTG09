function validar_registro(){
var username=document.formRegistro.nombres;
var username_len=username.value.length;
var password=document.formRegistro.contraseña;
var password_len=password.value.length;
var apellido=document.formRegistro.apellidos;
var username_len=username.value.length;
if(username_len==0){
    alert("Debes ingresar tu nombre");
    username.focus();

}
if(apellido_len==0){
    alert("Debes ingresar tu apellido");
    username.focus();

}
if(password_len==0 || password_len <8){
    alert("Debes ingresar tuna contraseña de minimo 8 caracteres");
    password.focus();

}


}