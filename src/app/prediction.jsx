import createPlotlyComponent from 'react-plotlyjs';
//See the list of possible plotly bundles at https://github.com/plotly/plotly.js/blob/master/dist/README.md#partial-bundles or roll your own
import Plotly from '../../node_modules/plotly.js/dist/plotly-cartesian';
const PlotlyComponent = createPlotlyComponent(Plotly);
import PropTypes from 'prop-types'; // ES6

class Prediction extends React.Component {
    constructor(props) {
        super(props);
        this.state = {}
    }

    render() {
        let predicted = {
            type: "scatter",
            mode: "lines",
            name: 'Predicted',
            x: this.context.data ?
            JSON.parse(this.context.data.weeks).slice(0, sVal) : "2010-7-18",
            y: this.context.data ? JSON.parse(this.context.data.Prices).slice(0, sVal) : 0,
            line: { color: '#17BECF' }
        };
        let actual = {
            type: "scatter",
            mode: "lines",
            name: 'Actual',
            x: this.context.data ?
            JSON.parse(this.context.data.weeks).slice(0, sVal) : "2010-7-18",
            y: this.context.data ? JSON.parse(this.context.data.Prices).slice(0, sVal) : 0,
            line: { color: '#7F7F7F' }
        };
        let layout = { // all "layout" attributes: #layout
            title: 'simple example', // more about "layout.title": #layout-title
            xaxis: { // all "layout.xaxis" attributes: #layout-xaxis
                title: 'time' // more about "layout.xaxis.title": #layout-xaxis-title
            }
        };
        let config = {
            showLink: false,
            displayModeBar: false
        };
        let plot = this.context.data ? <PlotlyComponent className="whatever" data={[predicted, actual]} layout={ layout } config={ config } /> : null
        return (
        	<div className = "plot" > { plot } </div>
        );
    }
}
Prediction.contextTypes = {
    data: React.PropTypes.object,
    sVal: React.PropTypes.number
}
export default Prediction
