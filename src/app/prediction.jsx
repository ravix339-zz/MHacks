import createPlotlyComponent from 'react-plotlyjs';
//See the list of possible plotly bundles at https://github.com/plotly/plotly.js/blob/master/dist/README.md#partial-bundles or roll your own
import Plotly from '../../node_modules/plotly.js/dist/plotly-cartesian';
const PlotlyComponent = createPlotlyComponent(Plotly);

class Prediction extends React.Component {
	constructor(props) {
		super(props);
		this.state = {}
	}

	render() {
        console.log(this.props);
        let predicted = [
          {
            type: "scatter",
            mode: "lines",
            name: 'Predicted',
            x: this.props.data.weeks,
            y: this.props.data.Prices,
            line: {color: '#17BECF'}
          }
        ];
        let actual = {
          type: "scatter",
          mode: "lines",
          name: 'Actual',
          x: this.props.data.weeks,
          y: this.props.data.Prices,
          line: {color: '#7F7F7F'}
        }
	    let layout = {                     // all "layout" attributes: #layout
	      	title: 'simple example',  // more about "layout.title": #layout-title
	      	xaxis: {                  // all "layout.xaxis" attributes: #layout-xaxis
	        	title: 'time'         // more about "layout.xaxis.title": #layout-xaxis-title
	      	},
	      	annotations: [            // all "annotation" attributes: #layout-annotations
	        	{
	          		text: 'simple annotation',    // #layout-annotations-text
	          		x: 0,                         // #layout-annotations-x
	          		xref: 'paper',                // #layout-annotations-xref
	          		y: 0,                         // #layout-annotations-y
	          		yref: 'paper'                 // #layout-annotations-yref
	        	}
	      	]
	    };
	    let config = {
	      	showLink: false,
	      	displayModeBar: true
	    };
		return (
			<div className="plot">
				<PlotlyComponent className="whatever" data={[predicted, actual]} layout={layout} config={config}/>
			</div>
		);
	}
}

export default Prediction
