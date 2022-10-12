var titulo1
var genero1
var duracion1
var sinopsis1
var titulo_org1
var reparto1
var directo1
function showp(){
    np=document.getElementById("nmov").value;
    console.log('Funciona')
    switch (np){
        case '1':
            console.log('Entro')
            document.getElementById("titulo").innerHTML=this.titulo1;
            document.getElementById("generos").innerHTML=this.genero1;
            document.getElementById("duracion").innerHTML=this.duracion1;
            document.getElementById("sinopsis").innerHTML=this.sinopsis1;
            document.getElementById("titulo_org").innerHTML=this.titulo_org1;
            document.getElementById("reparto").innerHTML=this.reparto1;
            document.getElementById("director").innerHTML=this.directo1;
           
            break;
        case '2':
            titulo2=document.getElementById("titulo").value;
            genero2=document.getElementById("generos").value;
            duracion2=document.getElementById("duracion").value;
            sinopsis2=document.getElementById("sinopsis").value;
            titulo_org2=document.getElementById("titulo_org").value;
            reparto2=document.getElementById("reparto").value;
            directo2=document.getElementById("director").value;
            break;
        case '3':
            titulo3=document.getElementById("titulo").value;
            genero3=document.getElementById("generos").value;
            duracion3=document.getElementById("duracion").value;
            sinopsis3=document.getElementById("sinopsis").value;
            titulo_org3=document.getElementById("titulo_org").value;
            reparto3=document.getElementById("reparto").value;
            directo3=document.getElementById("director").value;
            break;

        case '4':
            titulo4=document.getElementById("titulo").value;
            genero4=document.getElementById("generos").value;
            duracion4=document.getElementById("duracion").value;
            sinopsis4=document.getElementById("sinopsis").value;
            titulo_org4=document.getElementById("titulo_org").value;
            reparto4=document.getElementById("reparto").value;
            directo4=document.getElementById("director").value;
            break;
            
        case '5':
            titulo5=document.getElementById("titulo").value;
            genero5=document.getElementById("generos").value;
            duracion5=document.getElementById("duracion").value;
            sinopsis5=document.getElementById("sinopsis").value;
            titulo_org5=document.getElementById("titulo_org").value;               
            reparto5=document.getElementById("reparto").value;
            directo5=document.getElementById("director").value;
            break;
        case '6':
            titulo6=document.getElementById("titulo").value;
            genero6=document.getElementById("generos").value;
            duracion6=document.getElementById("duracion").value;
            sinopsis6=document.getElementById("sinopsis").value;
            titulo_org6=document.getElementById("titulo_org").value;
            reparto6=document.getElementById("reparto").value;
            directo6=document.getElementById("director").value;
            break;
        case '7':
            titulo7=document.getElementById("titulo").value;
            genero7=document.getElementById("generos").value;
            duracion7=document.getElementById("duracion").value;
            sinopsis7=document.getElementById("sinopsis").value;
            titulo_org7=document.getElementById("titulo_org").value;
            reparto7=document.getElementById("reparto").value;
            directo7=document.getElementById("director").value;
            break;

        case '8':
            titulo8=document.getElementById("titulo").value;
            genero8=document.getElementById("generos").value;
            duracion8=document.getElementById("duracion").value;
            sinopsis8=document.getElementById("sinopsis").value;
            titulo_org8=document.getElementById("titulo_org").value;
            reparto8=document.getElementById("reparto").value;
            directo8=document.getElementById("director").value;
            break;
        case '9':
            titulo9=document.getElementById("titulo").value;
            genero9=document.getElementById("generos").value;
            duracion9=document.getElementById("duracion").value;
            sinopsis9=document.getElementById("sinopsis").value;
            titulo_or9=document.getElementById("titulo_org").value;
            reparto9=document.getElementById("reparto").value;
            directo9=document.getElementById("director").value;
            break;
        case '10':
            titulo10=document.getElementById("titulo").value;
            genero10=document.getElementById("generos").value;
            duracion10=document.getElementById("duracion").value;
            sinopsis10=document.getElementById("sinopsis").value;
            titulo_org10=document.getElementById("titulo_org").value;
            reparto10=document.getElementById("reparto").value;
            directo10=document.getElementById("director").value;
            break;
    }
}

function agp(){
    np=document.getElementById("nmov").value;
    console.log("entro: "+np)
    switch (np){
        case '1':
            this.titulo1=document.getElementById("titulo").value;
            this.genero1=document.getElementById("generos").value;
            this.duracion1=document.getElementById("duracion").value;
            this.sinopsis1=document.getElementById("sinopsis").value;
            this.titulo_org1=document.getElementById("titulo_org").value;
            this.reparto1=document.getElementById("reparto").value;
            this.directo1=document.getElementById("director").value;
            break;
        case '2':
            titulo2=document.getElementById("titulo").value;
            genero2=document.getElementById("generos").value;
            duracion2=document.getElementById("duracion").value;
            sinopsis2=document.getElementById("sinopsis").value;
            titulo_org2=document.getElementById("titulo_org").value;
            reparto2=document.getElementById("reparto").value;
            directo2=document.getElementById("director").value;
            break;
        case '3':
            titulo3=document.getElementById("titulo").value;
            genero3=document.getElementById("generos").value;
            duracion3=document.getElementById("duracion").value;
            sinopsis3=document.getElementById("sinopsis").value;
            titulo_org3=document.getElementById("titulo_org").value;
            reparto3=document.getElementById("reparto").value;
            directo3=document.getElementById("director").value;
            break;

        case '4':
            titulo4=document.getElementById("titulo").value;
            genero4=document.getElementById("generos").value;
            duracion4=document.getElementById("duracion").value;
            sinopsis4=document.getElementById("sinopsis").value;
            titulo_org4=document.getElementById("titulo_org").value;
            reparto4=document.getElementById("reparto").value;
            directo4=document.getElementById("director").value;
            break;
            
        case '5':
            titulo5=document.getElementById("titulo").value;
            genero5=document.getElementById("generos").value;
            duracion5=document.getElementById("duracion").value;
            sinopsis5=document.getElementById("sinopsis").value;
            titulo_org5=document.getElementById("titulo_org").value;               
            reparto5=document.getElementById("reparto").value;
            directo5=document.getElementById("director").value;
            break;
        case '6':
            titulo6=document.getElementById("titulo").value;
            genero6=document.getElementById("generos").value;
            duracion6=document.getElementById("duracion").value;
            sinopsis6=document.getElementById("sinopsis").value;
            titulo_org6=document.getElementById("titulo_org").value;
            reparto6=document.getElementById("reparto").value;
            directo6=document.getElementById("director").value;
            break;
        case '7':
            titulo7=document.getElementById("titulo").value;
            genero7=document.getElementById("generos").value;
            duracion7=document.getElementById("duracion").value;
            sinopsis7=document.getElementById("sinopsis").value;
            titulo_org7=document.getElementById("titulo_org").value;
            reparto7=document.getElementById("reparto").value;
            directo7=document.getElementById("director").value;
            break;

        case '8':
            titulo8=document.getElementById("titulo").value;
            genero8=document.getElementById("generos").value;
            duracion8=document.getElementById("duracion").value;
            sinopsis8=document.getElementById("sinopsis").value;
            titulo_org8=document.getElementById("titulo_org").value;
            reparto8=document.getElementById("reparto").value;
            directo8=document.getElementById("director").value;
            break;
        case '9':
            titulo9=document.getElementById("titulo").value;
            genero9=document.getElementById("generos").value;
            duracion9=document.getElementById("duracion").value;
            sinopsis9=document.getElementById("sinopsis").value;
            titulo_or9=document.getElementById("titulo_org").value;
            reparto9=document.getElementById("reparto").value;
            directo9=document.getElementById("director").value;
            break;
        case '10':
            titulo10=document.getElementById("titulo").value;
            genero10=document.getElementById("generos").value;
            duracion10=document.getElementById("duracion").value;
            sinopsis10=document.getElementById("sinopsis").value;
            titulo_org10=document.getElementById("titulo_org").value;
            reparto10=document.getElementById("reparto").value;
            directo10=document.getElementById("director").value;
            break;
    }
}

function precom(){
    document.getElementById("RPelicula1").innerText =titulo1 ;
    document.getElementById("RPelicula2").innerText =titulo2 ;
    document.getElementById("RPelicula3").innerText =titulo3 ;
    document.getElementById("RPelicula4").innerText =titulo4 ;
    document.getElementById("RPelicula5").innerText =titulo5 ;
}

function cartel(){




}
