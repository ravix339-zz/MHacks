import ReactDOM from 'react-dom';
import {BrowserRouter, Route, Switch, Redirect, browserHistory} from 'react-router-dom';
import App from './app';
import Prediction from './prediction';
import Sentiment from './sentiment';
import Correlation from './correlation';
import './bundle.scss';


ReactDOM.render(
	<BrowserRouter>
		<App>
			<Route path="/main" component={Prediction} />
			<Route path="/sent" component={Sentiment} />
			<Route path="/corr" component={Correlation} />
  		</App>
  	</BrowserRouter>,

	document.getElementById('react-root')
)