import { predictor_form_asma, predictor_form_cardiopatia, predictor_form_idade, predictor_form_diabetes, predictor_form_doenca_hematologica,
  predictor_form_doenca_hepatica, predictor_form_doenca_neurologica, predictor_form_doenca_renal, predictor_form_imunodepressao, predictor_form_obesidade, 
  predictor_form_pneumopatia, predictor_form_puerpera, predictor_form_sindrome_de_down, predictor_form_racacor, predictor_form_covid_confirmado, 
  predictor_form_sexo} from "../names";


export const predictor_url = "http://localhost:5000/predictor/";
const frontend_app_url = 'http://localhost:3000/';

const prediction_meanings = {
  0: "Sem previsão de óbito",
  1: "Com previsão de óbito"
};

function check_form_values(values) {
  for (var key in values) {
    if (values[key].trim().length === 0) {
      alert("Nenhum campo deve estar em branco!");
      return false;
    }
  }
  return true;
}


function get_form_values() {
  var idade = document.getElementById(predictor_form_idade).value;
  var asma = document.getElementById(predictor_form_asma).value;
  var cardiopatia = document.getElementById(predictor_form_cardiopatia).value;
  var diabetes = document.getElementById(predictor_form_diabetes).value;
  var doenca_hematologica = document.getElementById(predictor_form_doenca_hematologica).value;
  var doenca_hepatica = document.getElementById(predictor_form_doenca_hepatica).value;
  var doenca_neurologica = document.getElementById(predictor_form_doenca_neurologica).value;
  var doenca_renal = document.getElementById(predictor_form_doenca_renal).value;
  var imunodepressao = document.getElementById(predictor_form_imunodepressao).value;
  var obesidade = document.getElementById(predictor_form_obesidade).value;
  var pneumopatia = document.getElementById(predictor_form_pneumopatia).value;
  var puerpera = document.getElementById(predictor_form_puerpera).value;
  var sindrome_de_down = document.getElementById(predictor_form_sindrome_de_down).value;
  var racacor = document.getElementById(predictor_form_racacor).value;
  var covid_confirmado = document.getElementById(predictor_form_covid_confirmado).value;
  var sexo = document.getElementById(predictor_form_sexo).value;

  var data = {
    "idade": idade,
    "asma": asma,
    "cardiopatia": cardiopatia,
    "diabetes": diabetes,
    "doenca_hematologica": doenca_hematologica,
    "doenca_hepatica": doenca_hepatica,
    "doenca_neurologica": doenca_neurologica,
    "doenca_renal": doenca_renal,
    "imunodepressao": imunodepressao,
    "obesidade": obesidade,
    "pneumopatia": pneumopatia,
    "puerpera": puerpera,
    "sindrome_de_down": sindrome_de_down,
    "eh_racacor_amarela": racacor === "amarela",
    "eh_racacor_branca": racacor === "branca",
    "eh_racacor_desconhecida": racacor === "desconhecida",
    "eh_racacor_ignorada": racacor === "ignorada",
    "eh_racacor_indigena": racacor === "indigena",
    "eh_racacor_nenhuma": racacor === "nenhuma",
    "eh_racacor_parda": racacor === "parda",
    "eh_racacor_preta": racacor === "preta",
    "eh_covid_confirmado": covid_confirmado === "sim",
    "eh_sexo_feminino": sexo === "feminino",
    "eh_sexo_indefinido": sexo === "indefinido",
    "eh_sexo_masculino": sexo === "masculino"
  };

  return data;
}

const predict = async (form_values) => {
  const request_options = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json',
               'Access-Control-Allow-Origin': frontend_app_url,
               'Access-Control-Allow-Headers': '*'
             },
    body: JSON.stringify(form_values)
  };
  fetch(predictor_url, request_options)
      .then(async response => {
          var data = await response.json();
          console.log(data);

          if (!response.ok) 
              alert("Houve um erro ao realizar a predição!");
          else {
              alert("Predição realizada com sucesso: " + prediction_meanings[data["predicao"]]);
          }
      })
      .catch(() => {
        alert("Houve um erro ao realizar a predição!");
      });
};

export default function make_prediction() {
  var form_values = get_form_values();
  if (check_form_values(form_values)) {
    predict(form_values);
  }
}
