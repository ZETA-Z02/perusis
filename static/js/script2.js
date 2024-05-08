let mensaje = $("#mensaje");
mensaje.hide();
$("#hablar").click(function() {
  $("#respuesta").text("");
  $("#texto").text("");
  mensaje.show();
  // Al presionar el boton inicia la conversacion
  let inicioMessage = "Que desea saber hoy mi rey";
  speechSynthesis.speak(new SpeechSynthesisUtterance(inicioMessage));
  // Obtener los datos que se enviarán al servidor

  // Comenzar el reconocimiento de voz
  setTimeout(function() {
    talk();
  }, 1500);
  // Realizar una solicitud AJAX después de 10 segundos
  setTimeout(function() {
    // Detener el reconocimiento de voz
    rec.stop();
    let data = { texto: $("#texto").text() };
    // Realizar la solicitud AJAX
    $.ajax({
      type: "POST",
      url: "/procesar",
      data: data,
      success: function(response) {
        console.log("Hay una respuesta:", response);
        // Actualizar la página con la respuesta recibida
        speechSynthesis.speak(new SpeechSynthesisUtterance(response.resultado));
        $("#respuesta").text(response.resultado);
      },
      error: function(error) {
        console.log("Error:", error);
      },
    });
  }, 10000); // 10 segundos en milisegundos
});

function talk() {
  if ("webkitSpeechRecognition" in window) {
    rec = new webkitSpeechRecognition();
    rec.lang = "es-AR";
    rec.continuous = true;
    rec.interim = true;
    rec.addEventListener("result", iniciar);
    rec.start(); // Iniciar el reconocimiento de voz cuando la página se carga
  } else {
    alert("Disculpas, no puedes usar la API de reconocimiento de voz");
  }
}
function iniciar(event) {
  let texto = "";
  for (let i = event.resultIndex; i < event.results.length; i++) {
    texto += event.results[i][0].transcript + " ";
  }
  // Mostrar el texto reconocido en un elemento HTML
  $("#texto").text(texto);
}
$("#detener").click(function() {
  mensaje.hide();
  rec.stop();
});