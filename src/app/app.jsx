import {NavLink} from 'react-router-dom';
import InputRange from 'react-input-range';
import PropTypes from 'prop-types'; // ES6 
import moment from 'moment';
// import moment from 'moment';

class App extends React.Component {
	constructor(props) {
		super(props)
		this.state = {
			sVal: 0,
			data: null,
			weeks: moment().week() - (moment([2012, 7, 1]).week()) + 6 + (moment().year() - (moment([2012, 7, 1]).year()))*52
		}
		this.onChange = this.onChange.bind(this);
	}

	componentWillMount() {
		fetch("/data", {
			method: 'GET'
		}).then((res) => {
			try {
       			const data = res.json();
                return data;
        	// Do your JSON handling here
    		} catch(err) {
        	// It is text, do you text handling here
        		return null
    		}
		}).then( (data2) =>{
				this.setState({data: data2})
		})
	}
	onChange(val) {
		this.setState({sVal: val})
	}
  	getChildContext() {
    	return {
      		data: this.state.data, 
      		sVal: this.state.sVal
      	}
  	}



	render() {
		return (
				<div id='content'>
					<ul>
					<li><NavLink to={'/main'} activeClassName="active">Prediction</NavLink></li>
					<li><NavLink to={'/sent'} activeClassName="active">Sentiment</NavLink></li>
					<li><NavLink to={'/corr'} activeClassName="active">Correlation</NavLink></li>
					</ul>
					<div id="slider-container">
					<InputRange
						formatLabel={value => `week of ${(moment([2012,6,1]).add(parseInt(value), 'w')).format('YYYY-MM-DD').toString()}`}
				        maxValue={this.state.weeks}
				        minValue={0}
				        value={this.state.sVal}
				        onChange={this.onChange} />
				    </div>
				        {this.props.children}
				</div>
		)
	}
}
App.childContextTypes = {
    	data: React.PropTypes.object,
    	sVal: React.PropTypes.number,
  	}
export default App
// `week of ${(moment([2012,7,1]).add(parseInt(value), 'w')).format('YYYY-MM-DD').toString()}`}