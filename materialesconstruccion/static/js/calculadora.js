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

    function addfila(){
        inputdescr=document.createElement('input');
        descrip=document.createElement('td');
        inputdescr.setAttribute('name','descrip'+(i+1));
        descrip.appendChild(inputdescr);
    
        inputcantidad=document.createElement('input');
        inputcantidad.setAttribute('name','cant'+(i+1))
        inputcantidad.classList.add('cantidad');
        inputcantidad.addEventListener('change', calculototal)
        cantidad=document.createElement('td');
        cantidad.appendChild(inputcantidad);
    
        inputcosto=document.createElement('input');
        inputcosto.classList.add('costounit');
        inputcosto.setAttribute('name','costoUnit'+(i+1));
        inputcosto.addEventListener('change', calcularSubtotal);
        costo=document.createElement('td');
        costo.appendChild(inputcosto);
    
        inputsubtotal=document.createElement('input');
        inputsubtotal.classList.add('subtotal');
        inputsubtotal.addEventListener('change', calcularcostounit);
        subtotal=document.createElement('td');
        subtotal.appendChild(inputsubtotal);
    
        fila=document.createElement('tr');
        fila.appendChild(descrip);
        fila.appendChild(cantidad);
        fila.appendChild(costo);
        fila.appendChild(subtotal);
        document.getElementById('tablaCotizacion').appendChild(fila)
    }

    function deletfila(){
        numero=document.getElementById('tablaCotizacion');
        numero.removeChild(numero.lastChild);
        calculototal();
    }