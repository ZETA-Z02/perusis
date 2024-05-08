mensaje.hide();
$(document).ready(function () {
	let mensaje = $("#mensaje");

	let rec;
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
	talk();
	$("#hablar").click(function () {
	  // Obtener los datos que se enviarán al servidor
	  let data = { texto: $("#texto").text() };

	  // Realizar una solicitud AJAX
	  $.ajax({
		type: "POST",
		url: "/procesar",
		data: data,
		success: function (response) {
		  console.log("Hay una respuesta:", response);
		  // Actualizar la página con la respuesta recibida
		  $("#respuesta").text(response.resultado);	// Obtener los datos que se enviarán al servidor
		  speechSynthesis.speak(new SpeechSynthesisUtterance(response.resultado));
		},
		error: function (error) {
		  console.log("Error:", error);
		},
	  });
	});

	function iniciar(event) {
	  let texto = "";
	  for (let i = event.resultIndex; i < event.results.length; i++) {
		texto += event.results[i][0].transcript + " ";
	  }
	  // Mostrar el texto reconocido en un elemento HTML
	  $("#texto").text(texto);
	}


  });