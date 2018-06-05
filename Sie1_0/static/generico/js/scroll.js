function getOffset( el ) {
    var _x = 0;
    var _y = 0;
    while(el && !isNaN( el.offsetLeft ) && !isNaN( el.offsetTop ) ) {
        _x += el.offsetLeft - el.scrollLeft;
        _y += el.offsetTop - el.scrollTop;
        el = el.offsetParent;
    }
    return { top: _y, left: _x };
}

var elemento = document.getElementById('descripcion');
var x = getOffset(elemento).left;
var y = getOffset(elemento).top;



document.body.onload = res();
    function res(){

        let desc = document.getElementById('descripcion');

        if( $(desc).is(":visible") ){

            desc.onchange = scrollTo(x,y);

        }
    }



    var elemento = document.getElementById('contacto');

    let urlA = window.location.href;

    document.body.onload = obtenerUrl();

    function obtenerUrl(){

        if (urlA != 'http://127.0.0.1:8000/'){

            elemento.style.display = 'none';

        }

    }


