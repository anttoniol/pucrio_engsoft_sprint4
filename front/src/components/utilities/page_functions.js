import { root } from "..";
import {PredictorForm} from "../components/predictor_form";


export default function render_page(data) {
    root.render(
      <div>
        <PredictorForm />
      </div>
    );
}