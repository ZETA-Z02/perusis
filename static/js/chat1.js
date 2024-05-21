// oculta y abre el chatbot
const chatbotToggler = document.querySelector(".chatbot-toggler");
const closeBtn = document.querySelector(".close-btn");

chatbotToggler.addEventListener("click", () =>
  document.body.classList.toggle("show-chatbot")
);
closeBtn.addEventListener("click", () =>
  document.body.classList.remove("show-chatbot")
);
$(document).on('click', '#send-email', function () {
  console.log("send email");
  let email = $("#email").val();
  let id = $(this).parent().attr('id');
  console.log(email+id);
  // enviar por ajax a email, 
  $.ajax({
    type: "POST",
    url: "/email",
    contentType: "application/json",
    data: JSON.stringify({content: email, id:id}),
    success: function (response) {
      console.log("exito"+response.resultado)
    },error: function(error){
      console.log("fallo"+error.resultado)
    }
  });
});
//
$(document).ready(function () {
  // LOS 2 ENVIAN EL MENSAJE
  $("#send-btn").click(function () {
    let entrada = $("#entrada").val();
    peticionAjax(entrada);
  });
  $("#entrada").on("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
      e.preventDefault();
      let entrada = $("#entrada").val();
      peticionAjax(entrada);
    }
  });
  // LOS 2 ENVIAN EL MENSAJE->END
  //sendChatBtn.addEventListe->er("click", handleChat);
  // CREAR FUNCTION PARA ENVIAR EL MENSAJE POR AJAX Y QUE APAREZCA POR PANTALLA
});
function peticionAjax(pregunta) {
  let preguntaUsuario = $("#chat-question");
  let respuesta = $("#chat-answer");
  $.ajax({
    type: "POST",
    url: "/chatbot1",
    contentType: "application/json",
    data: JSON.stringify({content: pregunta}),
    success: function (response) {
      console.log("Hay una respuesta:", response);
      preguntaUsuario.html(`<p>${pregunta}</p>`)
      respuesta.html(response.resultado);
      $("#entrada").val('');
    },
    error: function (error) {
      console.log("Error:", error);
    },
  });
}
// let html = `<li class="chat incoming">
      //               <span class="material-symbols-outlined">smart_toy</span>
      //               <p>Esto es una Respuesta,<br />asistente virtual de PERUSIS</p>
      //             </li>`;
