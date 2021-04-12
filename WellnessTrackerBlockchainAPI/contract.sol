// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.8.0;

contract  wellnesstracker {
    string BodyTemperature;
    int BloodPressure;
    int Respiration;
    int Glucose;
    int HeartRate;
    int Cholesterol;
    int OxygenSaturation;
    
    constructor() {
         BodyTemperature= "35.7"; 
         BloodPressure= 114; 
         Respiration= 15; 
         Glucose= 130; 
         HeartRate= 92; 
         Cholesterol= 185;
         OxygenSaturation=99;
    }
    
    function get() public view returns(string memory,int ,int ,int ,int ,int ,int ) {
        return (BodyTemperature,BloodPressure,Respiration,Glucose,HeartRate,Cholesterol,OxygenSaturation);
    }
    
    function set(string memory _bodytemperature,int  _bloodpressure,int  _respiraton,int  _glucose,int  _heartrate,int  _cholesterol,int  _oxygensaturation) public {
        BodyTemperature= _bodytemperature; 
        BloodPressure= _bloodpressure; 
        Respiration= _respiraton; 
        Glucose= _glucose; 
        HeartRate= _heartrate; 
        Cholesterol= _cholesterol;
        OxygenSaturation=_oxygensaturation;
    }
}