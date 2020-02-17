import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      home: Home(),
    );
  }
}

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  final myController = TextEditingController();
  bool newStatus = true;
  String ip = '';
  void toggleSwitch(switchStatus) {
    var client = http.Client();
    try{
      var url = 'http://$ip:3000/switchLed';
      client.post(url,body: json.encode({'status': newStatus}), headers: {'Content-type':'application/json'}).then((response){
        print('status: ${newStatus.toString()}');
      });
    }
    finally{
      client.close();
    }
    setState(() {
      newStatus = !newStatus;
    });
    
  }
  

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.refresh),
        onPressed: (){
          setState(() {
            ip = myController.text;
          });
          print(ip);
        },
      ),
      appBar: AppBar(title: Text('Switch LED')),
      body: Container(
            child:Column(children: <Widget>[
              TextFormField(
              controller: myController,
              decoration: InputDecoration(contentPadding: EdgeInsets.all(10), labelText: 'Adres IP'),
            ),
            SizedBox(height: 20,),
            Text('Obecny adres IP: $ip'),
            SizedBox(height: 20,),
            Text('Turn the led ${newStatus==true ? 'ON':'OFF'}', style: TextStyle(fontSize: 20),),
            SizedBox(height: 20,),
            Transform.scale(
              scale: 2,
                          child: Switch(
                value: !newStatus,
                onChanged: toggleSwitch,
              ),
            )
        
            ],)
            
      ),
    );
  }
}
