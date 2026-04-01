/*1. Módulo de Tesorería: Pago de Permisos (Cálculos y Retorno)
El vecino ingresa el monto de su permiso de circulación para saber cuánto pagará tras el descuento municipal.
Lógica: Si el monto es mayor a $70.000, el descuento es del 15%. Si es menor, es del 5%.
Regla: La Función Principal debe mostrar el total a pagar con un signo de peso ($).
*/


function precioFinal() {
    const result = document.getAnimations("result2");
    let input = document.getElementById("input2");
    const container = document.getElementById("container2");

}

function pagoPermisos() {
    let dinero = parseFloat(input.value);
    if (monto > 70.000) {
        alert(`${dinero} tiene un descuento del 15%`)
    } else {
        alert(`${dinero} tiene un descuento del 5%`)
    }
}




/*2. Módulo de Salud: Fila de Vacunación (Arreglos y Prioridad)
Gestión de nombres en la fila de espera del consultorio local.
Lógica: * Botón Normal: Agrega el nombre al final de la lista (push).
Botón Urgencia: Agrega el nombre al inicio de la lista (unshift).
Regla: El resultado debe mostrarse como una lista ordenada en el HTML. <ol>
*/
let asistencia = [];
function agregarLista(nombre) {
    asistencia.push(nombre)

    return asistencia.join(", ")
}

function filaVacunacion() {
    const container = document.getElementById("container2");
    const result = document.getElementById("result2");
    const input = document.getElementById("input2");
    let nombre = input.value;
    let resultado = agregarLista(nombre); // llamado a la funcion con envio de parametros
    result.textContent = resultado;
    input.value = "";
    container.classList.remove("d-none");
};

/*3. Módulo de Subsidios: Buscador de Beneficiarios (Ciclos e If)
Verificar si un RUT o nombre está en el listado de entrega de beneficios.
Lógica: Tener un arreglo con al menos 6 nombres. Usar un ciclo for para buscar si el dato ingresado existe en la lista.
Regla: La función debe devolver "Beneficiario Verificado" o "No registrado".
*/
function buscarBeneficiario() {
    let nombres = []
}