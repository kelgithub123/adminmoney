let i=1
function calcularSubtotal(){
    let costounit=document.querySelectorAll(".costounit");
    let cantidad=document.querySelectorAll(".cantidad");
    let subtotal=document.querySelectorAll(".subtotal");
    let total=0;
        for(var i=0;i<=costounit.length-1;i++){
            subtotal[i].value=costounit[i].value*cantidad[i].value;  
                }
    calculototal();
                
    }
    function calcularcostounit(){
    let costounit=document.querySelectorAll(".costounit");
    let cantidad=document.querySelectorAll(".cantidad");
    let subtotal=document.querySelectorAll(".subtotal");
    let total=0;
        for(var i=0;i<=costounit.length-1;i++){  
                costounit[i].value=subtotal[i].value / cantidad[i].value;    
        }
        calculototal();          
    }
    
    function calculototal(){
    let costounit=document.querySelectorAll(".costounit");
    let cantidad=document.querySelectorAll(".cantidad");
    let subtotal=document.querySelectorAll(".subtotal");
    let total=0;
        for(var i=0;i<=costounit.length-1;i++){
                subtot=costounit[i].value*cantidad[i].value;
                total=total+subtot;
        }
                document.querySelector(".total").innerHTML=total;
    }    

    function valorinput(){
        inputprev=document.getElementById("idbanco").parentNode.previousSibling.childNodes[0];
        inputprev= inputprev.previousSibling.childNodes[0];
        console.log(inputprev)
        document.getElementById("banco").value=inputprev
    }

    function obtener(id){
        alert('presionaste id'+id)
        if(id){
        document.getElementById("banco").value=id}
        else{
            document.getElementById("banco").value="no cap"
        }
    }

    function retiroform(){
        formulario=document.getElementsByClassName('formulario');
        Array.from(formulario).forEach(function(refer){
            console.log(refer.action);
            lnk=refer.action;
            id=lnk.substr(-1);
            refer.action='retiro/'+id;
            console.log(refer.action);
        });
    }

    function abonoform(){
        formulario=document.getElementsByClassName('formulario');
        Array.from(formulario).forEach(function(refer){
            console.log(refer.action);
            lnk=refer.action;
            id=lnk.substr(-1);
            refer.action='abono/'+id;
            console.log(refer.action);
        });
    }


    function addfila(){
        i=i+1
        inputdescr=document.createElement('input');
        descrip=document.createElement('td');
        inputdescr.setAttribute('name','descrip'+(i));
        descrip.appendChild(inputdescr);
    
        inputcantidad=document.createElement('input');
        inputcantidad.setAttribute('name','cant'+(i))
        inputcantidad.classList.add('cantidad');
        inputcantidad.addEventListener('change', calculototal)
        cantidad=document.createElement('td');
        cantidad.appendChild(inputcantidad);
    
        inputcosto=document.createElement('input');
        inputcosto.classList.add('costounit');
        inputcosto.setAttribute('name','costoUnit'+(i));
        inputcosto.addEventListener('change', calcularSubtotal);
        costo=document.createElement('td');
        costo.appendChild(inputcosto);

        tipo=document.createElement('td');
        tipo.innerHTML=`<select name="tipo`+(i)+`" id="">
        <option value="construccion">construccion</option>
        <option value="alimentacion">alimentacion</option>
        <option value="vivienda">vivienda</option>
        </select>`;
        
        inputsubtotal=document.createElement('input');
        inputsubtotal.classList.add('subtotal');
        inputsubtotal.addEventListener('change', calcularcostounit);
        subtotal=document.createElement('td');
        subtotal.appendChild(inputsubtotal);
    
        fila=document.createElement('tr');
        fila.appendChild(descrip);
        fila.appendChild(cantidad);
        fila.appendChild(costo);
        fila.appendChild(tipo);
        fila.appendChild(subtotal);
        document.getElementById('tablaCotizacion').appendChild(fila);

        num=document.getElementById('num');
        num.value=i
    }

    function deletfila(){
        numero=document.getElementById('tablaCotizacion');
        numero.removeChild(numero.lastChild);
        calculototal();
    }