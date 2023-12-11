import { predictor_form_asma, predictor_form_cardiopatia, predictor_form_idade, predictor_form_diabetes, predictor_form_doenca_hematologica,
  predictor_form_doenca_hepatica, predictor_form_doenca_neurologica, predictor_form_doenca_renal, predictor_form_imunodepressao, predictor_form_obesidade, 
  predictor_form_pneumopatia, predictor_form_puerpera, predictor_form_sindrome_de_down, predictor_form_racacor, predictor_form_covid_confirmado, 
  predictor_form_sexo} from "../names";


export const predictor_url = "http://localhost:5000/predictor/";
const frontend_app_url = 'http://localhost:3000/';

const prediction_meanings = {
  0: "sem previsão de óbito",
  1: "com previsão de óbito"
};

function check_form_values(values) {
  for (var key in values) {
    if (values[key] == null || values[key] === "select") {
      alert("Todos os campos devem ser informados!");
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
    "idade": parseInt(idade, 10),
    "asma": parseInt(asma, 10),
    "cardiopatia": parseInt(cardiopatia, 10),
    "diabetes": parseInt(diabetes, 10),
    "doenca_hematologica": parseInt(doenca_hematologica, 10),
    "doenca_hepatica": parseInt(doenca_hepatica, 10),
    "doenca_neurologica": parseInt(doenca_neurologica, 10),
    "doenca_renal": parseInt(doenca_renal, 10),
    "imunodepressao": parseInt(imunodepressao, 10),
    "obesidade": parseInt(obesidade, 10),
    "pneumopatia": parseInt(pneumopatia, 10),
    "puerpera": parseInt(puerpera, 10),
    "sindrome_de_down": parseInt(sindrome_de_down, 10),
    "racacor": racacor,
    "covid_confirmado": covid_confirmado,
    "sexo": sexo
  };

  return data;
}

const predict = async (form_values) => {
  const request_options = {
    method: 'POST',
    headers:  { 'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': frontend_app_url,
                'Access-Control-Allow-Headers': '*'
              },
    body: JSON.stringify(form_values)
  };
  fetch(predictor_url, request_options)
      .then(async response => {
          var data = await response.json();

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
    var data = {
      "idade": form_values.idade,
      "asma": form_values.asma,
      "cardiopatia": form_values.cardiopatia,
      "diabetes": form_values.diabetes,
      "doenca_hematologica": form_values.doenca_hematologica,
      "doenca_hepatica": form_values.doenca_hepatica,
      "doenca_neurologica": form_values.doenca_neurologica,
      "doenca_renal": form_values.doenca_renal,
      "imunodepressao": form_values.imunodepressao,
      "obesidade": form_values.obesidade,
      "pneumopatia": form_values.pneumopatia,
      "puerpera": form_values.puerpera,
      "sindrome_de_down": form_values.sindrome_de_down,
      "eh_racacor_amarela": form_values.racacor === "amarela",
      "eh_racacor_branca": form_values.racacor === "branca",
      "eh_racacor_desconhecida": form_values.racacor === "desconhecida",
      "eh_racacor_ignorada": form_values.racacor === "ignorada",
      "eh_racacor_indigena": form_values.racacor === "indigena",
      "eh_racacor_nenhuma": form_values.racacor === "nenhuma",
      "eh_racacor_parda": form_values.racacor === "parda",
      "eh_racacor_preta": form_values.racacor === "preta",
      "eh_covid_confirmado": form_values.covid_confirmado === "sim",
      "eh_sexo_feminino": form_values.sexo === "feminino",
      "eh_sexo_indefinido": form_values.sexo === "indefinido",
      "eh_sexo_masculino": form_values.sexo === "masculino"
    };
    predict(data);
  }
}
