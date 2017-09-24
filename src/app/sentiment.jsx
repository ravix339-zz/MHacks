import createPlotlyComponent from 'react-plotlyjs';
//See the list of possible plotly bundles at https://github.com/plotly/plotly.js/blob/master/dist/README.md#partial-bundles or roll your own
import Plotly from '../../node_modules/plotly.js/dist/plotly-cartesian';
const PlotlyComponent = createPlotlyComponent(Plotly);
import PropTypes from 'prop-types'; // ES6

class Sentiment extends React.Component {
	constructor(props) {
		super(props);
		this.state = {}
	}

	render() {
		let sentbytime = {
		        type: 'scatter',  // all "scatter" attributes: https://plot.ly/javascript/reference/#scatter
		        mode: "lines",
		        name: "Sentiment By Time",
		        x: this.context.data ?
                JSON.parse(this.context.data.weeks).slice(0, this.context.sVal) : "2010-7-18",    // more about "x": #scatter-x
		        y: this.context.data ?
                JSON.parse(this.context.data.Sentiments).slice(0, this.context.sVal) : 0,     // #scatter-y
		        line: { color: '#17BECF' }
	    };
	    let layout = {                     // all "layout" attributes: #layout
	      	title: 'simple example',  // more about "layout.title": #layout-title
	      	xaxis: {                  // all "layout.xaxis" attributes: #layout-xaxis
	        	title: 'time'         // more about "layout.xaxis.title": #layout-xaxis-title
	      	},
	      	annotations: [            // all "annotation" attributes: #layout-annotations
	      	]
	    };
	    let config = {
	      	showLink: false,
	      	displayModeBar: false
	    };
	    var plot = this.context.data ? <PlotlyComponent className="whatever" data={[sentbytime]} layout={ layout } config={ config } /> : null
		return (
			<div className="plot">
				{plot}
			</div>
		);
	}
}
Sentiment.contextTypes = {
    	data: React.PropTypes.object,
    	sVal: React.PropTypes.number
  	}

export default Sentiment
