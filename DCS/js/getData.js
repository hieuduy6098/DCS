function updateGuiRealTimeValue(data, idmay, line) {
  var doc_element = document.getElementById("hieusuat"+idmay+line);
  if(typeof(doc_element) != 'undefined' && doc_element != null){
    document.getElementById("hieusuat"+idmay+line).innerHTML = data.hieuSuat;
    document.getElementById("sanLuong"+idmay+line).innerHTML = data.sanLuong;
    document.getElementById("soGoiBiCan"+idmay+line).innerHTML = data.soGoiBiCan;
    document.getElementById("ptgoiBiCan"+idmay+line).innerHTML = data.ptgoiBiCan;
    document.getElementById("soGoiRong"+idmay+line).innerHTML = data.soGoiRong;
    document.getElementById("ptgoiRong"+idmay+line).innerHTML = data.ptgoiRong;
  }
};
function tonggiatri(data1, data2, data3, line) {
  var doc_element = document.getElementById("tonghieusuat"+line);
  if(typeof(doc_element) != 'undefined' && doc_element != null){
    document.getElementById("tonghieusuat"+line).innerHTML = data1.hieuSuat+data2.hieuSuat+data3.hieuSuat;
    document.getElementById("tongsanLuong"+line).innerHTML = data1.sanLuong+data2.sanLuong+data3.sanLuong;
    document.getElementById("tongsoGoiBiCan"+line).innerHTML = data1.soGoiBiCan+data2.soGoiBiCan+data3.soGoiBiCan;
    document.getElementById("tongptgoiBiCan"+line).innerHTML = data1.ptgoiBiCan+data2.ptgoiBiCan+data3.ptgoiBiCan;
    document.getElementById("tongsoGoiRong"+line).innerHTML = data1.soGoiRong+data2.soGoiRong+data3.soGoiRong;
    document.getElementById("tongptgoiRong"+line).innerHTML = data1.ptgoiRong+data2.ptgoiRong+data3.ptgoiRong;
  }
}
function onMessageArrived(message) {
  if(message) {
      try {
          var data = JSON.parse(message.payloadString);
          //console.log(data);
          var topic = message.destinationName; 
          if (topic == "dcsData") {
              // revise this piece of code later
              if (data.id == "L1") {
                updateGuiRealTimeValue(data.data[0], data.data[0].idmay, data.id)
                updateGuiRealTimeValue(data.data[1], data.data[1].idmay, data.id)
                updateGuiRealTimeValue(data.data[2], data.data[2].idmay, data.id)
                tonggiatri(data.data[0], data.data[1], data.data[2], data.id)

              } else if (data.id == "L2") {
                updateGuiRealTimeValue(data.data[0], data.data[0].idmay, data.id)
                updateGuiRealTimeValue(data.data[1], data.data[1].idmay, data.id)
                updateGuiRealTimeValue(data.data[2], data.data[2].idmay, data.id)
                tonggiatri(data.data[0], data.data[1], data.data[2], data.id)
              }
          }/*
          else if (topic == "client_response/history") {
              var x = new Array();
              var y = new Array();
              if (!Array.isArray(data.data) || !data.data.length) {
                // array does not exist, is not an array, or is empty
                // ⇒ do not attempt to process array
                console.log("No data");
              }
              else {
                  data.data.forEach(element => {
                      //var time = new Date(element.t).getDay()+":"+new Date(element.t).getMonth()+":"+new Date(element.t).getFullYear()+":"+new Date(element.t).getHours()+":"+new Date(element.t).getMinutes()+":"+new Date(element.t).getSeconds();
                      var datetime = new Date(element.t);
                      //var time = datetime.toLocaleDateString() + " " + datetime.toLocaleTimeString();
                      var time = datetime.toLocaleString();
                      // console.log(time);
                      x.push(element.v);
                      y.push(time);
                  });
                  getChart(x, y, data.id);
              }
          }*/
      } catch(e) {
          console.log("no data request"); // error in the above string (in this case, yes)!
      }
  }
}
