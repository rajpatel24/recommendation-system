// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
var ctx = document.getElementById("myBarChart");
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Samsung Galaxy S6 Edge G925P 32GB White Pearl - Sprint (Certified Refurbished)', 'Samsung Galaxy J3 Emerge J327P SILVER Android Cell Phone - SPRINT', 'Total Wireless\xa0Samsung Galaxy\xa0S8+ 4G\xa0LTE Prepaid Smartphone', 'Samsung Galaxy S8 SM-G950UZSAVZW - Verizon - Coral Blue (Renewed) …', 'Samsung Galaxy Note 5 SM-N920T 64GB White - T-Mobile (Certified Refurbished)'],
    datasets: [{
      label: "Revenue",
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [5, 5, 4, 5, 4, 3],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'month'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 6
        }
      }],
      yAxes: [{
        ticks: {
          min: 1,
          max: 5,
          maxTicksLimit: 5
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
