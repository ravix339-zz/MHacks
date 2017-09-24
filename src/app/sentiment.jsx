import createPlotlyComponent from 'react-plotlyjs';
//See the list of possible plotly bundles at https://github.com/plotly/plotly.js/blob/master/dist/README.md#partial-bundles or roll your own
import Plotly from '../../node_modules/plotly.js/dist/plotly-cartesian';
const PlotlyComponent = createPlotlyComponent(Plotly);

class Sentiment extends React.Component {
	constructor(props) {
		super(props);
		this.state = {}
	}

	render() {
		let data = [
	      	{
		        type: 'scatter',  // all "scatter" attributes: https://plot.ly/javascript/reference/#scatter
		        x: [1, 2, 3],     // more about "x": #scatter-x
		        y: [6, 2, 3],     // #scatter-y
		        marker: {         // marker is an object, valid marker keys: #scatter-marker
		          	color: 'rgb(16, 32, 77)' // more about "marker.color": #scatter-marker-color
	        	}
	      	},
	      	{
		        type: 'bar',      // all "bar" chart attributes: #bar
		        x: [1, 2, 3],     // more about "x": #bar-x
		        y: [6, 2, 3],     // #bar-y
		        name: 'bar chart example' // #bar-name
		    }
    	];
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
				<PlotlyComponent className="whatever" data={data} layout={layout} config={config}/>
			</div>
		);
	}
}

export default Sentiment
