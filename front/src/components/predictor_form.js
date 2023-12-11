import React from "react";
import { predictor_form_asma, predictor_form_div, predictor_form_cardiopatia, predictor_form_diabetes, predictor_form_idade, predictor_button, 
  predictor_form_doenca_hematologica, predictor_form_doenca_hepatica, predictor_form_doenca_neurologica, predictor_form_doenca_renal, 
  predictor_form_imunodepressao, predictor_form_obesidade, predictor_form_pneumopatia, predictor_form_puerpera, predictor_form_sindrome_de_down, predictor_form_racacor, 
  predictor_form_covid_confirmado, predictor_form_sexo } from "../names";
import make_prediction from "../routes/predictor_routes";


export const PredictorForm = () => {
  return (
    <div id={predictor_form_div} 
        style={{
            position: 'absolute', left: '50%', top: '50%',
            transform: 'translate(-50%, -50%)'
        }}
    >
      <center><h1>Preditor</h1></center>
      <p>Idade: <input type="number" id={predictor_form_idade}/> </p> 
      <p>Asma: <input type="number" id={predictor_form_asma}/> </p> 
      <p>Cardiopatia: <input type="number" id={predictor_form_cardiopatia}/> </p> 
      <p>Diabetes: <input type="number" id={predictor_form_diabetes}/> </p> 
      <p>Doença Hematológica: <input type="number" id={predictor_form_doenca_hematologica}/> </p> 
      <p>Doença Hepática: <input type="number" id={predictor_form_doenca_hepatica}/> </p> 
      <p>Doença Neurológica: <input type="number" id={predictor_form_doenca_neurologica}/> </p> 
      <p>Doença Renal: <input type="number" id={predictor_form_doenca_renal}/> </p> 
      <p>Imunodepressão: <input type="number" id={predictor_form_imunodepressao}/> </p> 
      <p>Obesidade: <input type="number" id={predictor_form_obesidade}/> </p> 
      <p>Pneumopatia: <input type="number" id={predictor_form_pneumopatia}/> </p> 
      <p>Puérpera: <input type="number" id={predictor_form_puerpera}/> </p> 
      <p>Síndrome de Down: <input type="number" id={predictor_form_sindrome_de_down}/> </p> 
      <p>Raça/Cor: <select id={predictor_form_racacor}>
                      <option value="select">Selecione</option>
                      <option value="amarela">Amarela</option>
                      <option value="branca">Branca</option>
                      <option value="desconhecida">Desconhecida</option>
                      <option value="ignorada">Ignorada</option>
                      <option value="indigena">Indígena</option>
                      <option value="nenhuma">Nenhuma</option>
                      <option value="parda">Parda</option>
                      <option value="preta">Preta</option>                      
                  </select></p>
      <p>Covid Confirmado: <select id={predictor_form_covid_confirmado}>
          <option value="select">Selecione</option>
          <option value="sim">Sim</option>
          <option value="nao">Não</option>                  
      </select></p>
      <p>Sexo: <select id={predictor_form_sexo}>
          <option value="select">Selecione</option>
          <option value="feminino">Feminino</option>
          <option value="indefinido">Indefinido</option>   
          <option value="masculino">Masculino</option>               
      </select></p>

      <center><p><button id={predictor_button} onClick={make_prediction} style={{height: '60px', width : '150px'}}>Realizar predição</button></p></center>
    </div>
  );
};

