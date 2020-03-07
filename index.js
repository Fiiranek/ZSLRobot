const express = require('express');
const bodyParser = require('body-parser');
const gpio = require('rpi-gpio').promise;
const app = express();

app.use(bodyParser.json());
app.post('/switchLed', function(req, res){
	const statusExists = req && req.body && req.body.status != null;
	const status = statusExists ? req.body.status.toString() == "true":"false";
	gpio.setup(40,gpio.DIR_OUT).then(()=>{
		console.log(status);
		return gpio.write(40, status);
	}).catch((err)=>{
	console.log('error:${err.toString()}');
	});
	res.send('led was switched');
});
app.listen(3000);
console.log('server started on port 3000');
