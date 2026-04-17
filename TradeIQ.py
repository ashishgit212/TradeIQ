<!DOCTYPE html>
<html>
<head>
  <title>TradePilot AI</title>
</head>
<body style="font-family: Arial; text-align:center; margin-top:100px;">
  <h1>📈 TradePilot AI</h1>
  <p>Simple Options Profit Calculator</p>

  <input id="premium" placeholder="Enter Premium"><br><br>
  <input id="lot" placeholder="Lot Size"><br><br>

  <button onclick="calc()">Calculate</button>

  <h2 id="result"></h2>

  <script>
    function calc() {
      let p = document.getElementById("premium").value;
      let l = document.getElementById("lot").value;
      let profit = p * l;
      document.getElementById("result").innerText = "Profit: ₹" + profit;
    }
  </script>
</body>
</html>