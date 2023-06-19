// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Area Chart Example
var ctx = document.getElementById("myAreaChart");
var key_list = document.getElementById("keyList");
var value_list = document.getElementById("valueList");

var key_list = ["Samsung Galaxy Note 3, Black 32GB (Verizon Wireless)","Nokia Lumia 900 Black Factory Unlocked","Samsung Galaxy A20 US Version Factory Unlocked Cell Phone with 32GB Memory, 6.4\" Screen, [SM-A205UZKAXAA], 12 Month Samsung US Warranty, GSM & CDMA Compatible, Black","Samsung Galaxy Note 8 N950 Factory Unlocked Phone 64GB Midnight Black (Renewed)","Samsung Galaxy A10 32GB (A105M) 6.2\" HD+ Infinity-V 4G LTE Factory Unlocked GSM Smartphone - Black","Samsung Galaxy Note 9 Factory Unlocked Phone with 6.4\" Screen and 128GB (U.S. Warranty), Ocean Blue","Motorola G6 – 32 GB – Unlocked (AT&T/Sprint/T-Mobile/Verizon) – Deep Indigo - (U.S. Warranty) - PAAE0011US","Samsung Galaxy Note 5, Black  64GB (Verizon Wireless)","Samsung Galaxy Note 5 SM-N920V Gold 32GB (Verizon Wireless)","Samsung Galaxy S8+ 64GB Factory Unlocked Smartphone - 6.2\" Screen - US Version (Midnight Black) - US Warranty [SM-G955UZKAXAA]","Samsung Galaxy S7 Edge G935FD 32GB Unlocked GSM 4G LTE","Moto G - Verizon Prepaid Phone (Verizon Prepaid Only)","Samsung Galaxy A50 A505G 64GB Duos GSM Unlocked Phone w/Triple 25MP Camera - Blue"]
var value_list =[983, 929, 915, 891, 874, 873, 836, 799, 799, 793, 783, 773, 706]


var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: key_list,
    datasets: [{
      label: "Sessions",
      lineTension: 0.3,
      backgroundColor: "rgba(2,117,216,0.2)",
      borderColor: "rgba(2,117,216,1)",
      pointRadius: 5,
      pointBackgroundColor: "rgba(2,117,216,1)",
      pointBorderColor: "rgba(255,255,255,0.8)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(2,117,216,1)",
      pointHitRadius: 50,
      pointBorderWidth: 2,
      data: value_list,
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          min: 100,
          max: 1000,
          maxTicksLimit: 5
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
