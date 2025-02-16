from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def welcome():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Single Page Application</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f0f0f0;
            }
            .container {
                text-align: center;
                background-color: #fff;
                padding: 50px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                width: 80%;
            }
            .tabs {
                display: flex;
                justify-content: space-around;
                margin-bottom: 20px;
            }
            .tab {
                padding: 10px 20px;
                cursor: pointer;
                background-color: #28a745;
                color: #fff;
                border-radius: 5px;
            }
            .tab:hover {
                background-color: #218838;
            }
            .tab.active {
                background-color: #218838;
            }
            .tab-content {
                display: none;
            }
            .tab-content.active {
                display: block;
            }
            .widget {
                text-align: left;
            }
            .widget label {
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
                font-size: 0.9em;
            }
            .widget input {
                width: 100%;
                padding: 8px;
                margin-bottom: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 0.7em;
            }
            .widget button {
                width: 100%;
                padding: 10px;
                background-color: #28a745;
                color: #fff;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 0.7em;
            }
            .widget button:hover {
                background-color: #218838;
            }
            .result {
                margin-top: 20px;
                font-size: 0.9em;
                color: #333;
            }
        </style>
        <script>
            function showTab(event, tabId) {
                var tabs = document.getElementsByClassName('tab');
                for (var i = 0; i < tabs.length; i++) {
                    tabs[i].classList.remove('active');
                }
                event.currentTarget.classList.add('active');

                var tabContents = document.getElementsByClassName('tab-content');
                for (var i = 0; i < tabContents.length; i++) {
                    tabContents[i].classList.remove('active');
                }
                document.getElementById(tabId).classList.add('active');
            }

            function calculateSIP() {
                var monthlyInvestment = document.getElementById('monthlyInvestment').value;
                var annualInterestRate = document.getElementById('annualInterestRate').value;
                var investmentPeriod = document.getElementById('investmentPeriod').value;

                var monthlyRate = annualInterestRate / 12 / 100;
                var months = investmentPeriod * 12;
                var futureValue = monthlyInvestment * ((Math.pow(1 + monthlyRate, months) - 1) / monthlyRate) * (1 + monthlyRate);

                document.getElementById('sipResult').innerText = 'Future Value: ₹' + futureValue.toFixed(2);
            }

            function calculateFD() {
                var principal = document.getElementById('principal').value;
                var annualInterestRate = document.getElementById('fdAnnualInterestRate').value;
                var timePeriod = document.getElementById('timePeriod').value;

                var maturityAmount = principal * Math.pow((1 + annualInterestRate / 100), timePeriod);
                document.getElementById('fdResult').innerText = 'Maturity Amount: ₹' + maturityAmount.toFixed(2);
            }

            function calculateLumpSumAndSIP() {
                var principal = document.getElementById('combinedPrincipal').value;
                var monthlyInvestment = document.getElementById('combinedMonthlyInvestment').value;
                var annualInterestRate = document.getElementById('combinedAnnualInterestRate').value;
                var timePeriod = document.getElementById('combinedTimePeriod').value;

                var monthlyRate = annualInterestRate / 12 / 100;
                var months = timePeriod * 12;

                var futureValueSIP = monthlyInvestment * ((Math.pow(1 + monthlyRate, months) - 1) / monthlyRate) * (1 + monthlyRate);
                var futureValueLumpsum = principal * Math.pow((1 + annualInterestRate / 100), timePeriod);

                var totalFutureValue = futureValueSIP + futureValueLumpsum;
                document.getElementById('combinedResult').innerText = 'Total Future Value: ₹' + totalFutureValue.toFixed(2);
            }

            function calculateInitialAndSIP() {
                var initialAmount = document.getElementById('initialAmount').value;
                var initialAnnualInterestRate = document.getElementById('initialAnnualInterestRate').value;
                var sipMonthlyInvestment = document.getElementById('sipMonthlyInvestment').value;
                var sipAnnualInterestRate = document.getElementById('sipAnnualInterestRate').value;
                var timePeriod = document.getElementById('combinedTimePeriod').value;

                var initialFutureValue = initialAmount * Math.pow((1 + initialAnnualInterestRate / 100), timePeriod);
                var sipMonthlyRate = sipAnnualInterestRate / 12 / 100;
                var months = timePeriod * 12;
                var sipFutureValue = sipMonthlyInvestment * ((Math.pow(1 + sipMonthlyRate, months) - 1) / sipMonthlyRate) * (1 + sipMonthlyRate);

                var totalFutureValue = initialFutureValue + sipFutureValue;
                document.getElementById('initialAndSIPResult').innerText = 'Total Future Value: ₹' + totalFutureValue.toFixed(2);
            }

            function calculateInflationAdjusted() {
                var initialAmount = document.getElementById('inflationInitialAmount').value;
                var monthlyInvestment = document.getElementById('inflationMonthlyInvestment').value;
                var annualInterestRate = document.getElementById('inflationAnnualInterestRate').value;
                var inflationRate = document.getElementById('inflationRate').value;
                var timePeriod = document.getElementById('inflationTimePeriod').value;

                var adjustedInterestRate = ((1 + annualInterestRate / 100) / (1 + inflationRate / 100) - 1) * 100;
                var monthlyRate = adjustedInterestRate / 12 / 100;
                var months = timePeriod * 12;

                var futureValueSIP = monthlyInvestment * ((Math.pow(1 + monthlyRate, months) - 1) / monthlyRate) * (1 + monthlyRate);
                var futureValueLumpsum = initialAmount * Math.pow((1 + adjustedInterestRate / 100), timePeriod);

                var totalFutureValue = futureValueSIP + futureValueLumpsum;
                document.getElementById('inflationResult').innerText = 'Total Future Value (Adjusted for Inflation): ₹' + totalFutureValue.toFixed(2);
            }

            function calculateGoalWithSIP() {
                var goalAmount = document.getElementById('goalAmount').value;
                var annualInterestRate = document.getElementById('goalAnnualInterestRate').value;
                var investmentPeriod = document.getElementById('goalInvestmentPeriod').value;
                var lumpsumAmount = document.getElementById('goalLumpsumAmount').value;
                var inflationRate = document.getElementById('goalInflationRate').value;

                var adjustedInterestRate = ((1 + annualInterestRate / 100) / (1 + inflationRate / 100) - 1) * 100;
                var monthlyRate = adjustedInterestRate / 12 / 100;
                var months = investmentPeriod * 12;
                var futureValueLumpsum = lumpsumAmount * Math.pow((1 + adjustedInterestRate / 100), investmentPeriod);
                var requiredMonthlyInvestment = (goalAmount - futureValueLumpsum) / (((Math.pow(1 + monthlyRate, months) - 1) / monthlyRate) * (1 + monthlyRate));

                document.getElementById('goalResult').innerText = 'Required Monthly Investment: ₹' + requiredMonthlyInvestment.toFixed(2);
            }
        </script>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to FinCalc by LetMoneyEarn</h1>
            <p>We're glad to have you here. Explore and enjoy!</p>
            <div class="tabs">
                <div class="tab active" onclick="showTab(event, 'sip')">SIP</div>
                <div class="tab" onclick="showTab(event, 'fd')">FD</div>
                <div class="tab" onclick="showTab(event, 'combined')">LumpSum And SIP</div>
                <div class="tab" onclick="showTab(event, 'initialAndSIP')">LumpSum and SIP</div>
                <div class="tab" onclick="showTab(event, 'inflation')">Inflation Adjusted</div>
                <div class="tab" onclick="showTab(event, 'goal')">Goal with SIP</div>
            </div>
            <div id="sip" class="tab-content active">
                <div class="widget">
                    <label for="monthlyInvestment">Monthly Investment (₹):</label>
                    <input type="number" id="monthlyInvestment" placeholder="Enter monthly investment amount">
                    <label for="annualInterestRate">Annual Interest Rate (%):</label>
                    <input type="number" id="annualInterestRate" placeholder="Enter annual interest rate">
                    <label for="investmentPeriod">Investment Period (years):</label>
                    <input type="number" id="investmentPeriod" placeholder="Enter investment period in years">
                    <button onclick="calculateSIP()">Calculate</button>
                    <div class="result" id="sipResult"></div>
                </div>
            </div>
            <div id="fd" class="tab-content">
                <div class="widget">
                    <label for="principal">Principal Amount (₹):</label>
                    <input type="number" id="principal" placeholder="Enter principal amount">
                    <label for="fdAnnualInterestRate">Annual Interest Rate (%):</label>
                    <input type="number" id="fdAnnualInterestRate" placeholder="Enter annual interest rate">
                    <label for="timePeriod">Time Period (years):</label>
                    <input type="number" id="timePeriod" placeholder="Enter time period in years">
                    <button onclick="calculateFD()">Calculate</button>
                    <div class="result" id="fdResult"></div>
                </div>
            </div>
            <div id="combined" class="tab-content">
                <div class="widget">
                    <label for="combinedPrincipal">Initial Amount (₹):</label>
                    <input type="number" id="combinedPrincipal" placeholder="Enter initial amount">
                    <label for="combinedMonthlyInvestment">Monthly Investment (₹):</label>
                    <input type="number" id="combinedMonthlyInvestment" placeholder="Enter monthly investment amount">
                    <label for="combinedAnnualInterestRate">Annual Interest Rate (%):</label>
                    <input type="number" id="combinedAnnualInterestRate" placeholder="Enter annual interest rate">
                    <label for="combinedTimePeriod">Time Period (years):</label>
                    <input type="number" id="combinedTimePeriod" placeholder="Enter time period in years">
                    <button onclick="calculateLumpSumAndSIP()">Calculate</button>
                    <div class="result" id="combinedResult"></div>
                </div>
            </div>
            <div id="initialAndSIP" class="tab-content">
                <div class="widget">
                    <label for="initialAmount">Initial Amount (₹):</label>
                    <input type="number" id="initialAmount" placeholder="Enter initial amount">
                    <label for="initialAnnualInterestRate">Initial Amount Annual Interest Rate (%):</label>
                    <input type="number" id="initialAnnualInterestRate" placeholder="Enter annual interest rate for initial amount">
                    <label for="sipMonthlyInvestment">Monthly Investment (₹):</label>
                    <input type="number" id="sipMonthlyInvestment" placeholder="Enter monthly investment amount">
                    <label for="sipAnnualInterestRate">SIP Annual Interest Rate (%):</label>
                    <input type="number" id="sipAnnualInterestRate" placeholder="Enter annual interest rate for SIP">
                    <label for="combinedTimePeriod">Time Period (years):</label>
                    <input type="number" id="combinedTimePeriod" placeholder="Enter time period in years">
                    <button onclick="calculateInitialAndSIP()">Calculate</button>
                    <div class="result" id="initialAndSIPResult"></div>
                </div>
            </div>
            <div id="inflation" class="tab-content">
                <div class="widget">
                    <label for="inflationInitialAmount">Initial Amount (₹):</label>
                    <input type="number" id="inflationInitialAmount" placeholder="Enter initial amount">
                    <label for="inflationMonthlyInvestment">Monthly Investment (₹):</label>
                    <input type="number" id="inflationMonthlyInvestment" placeholder="Enter monthly investment amount">
                    <label for="inflationAnnualInterestRate">Annual Interest Rate (%):</label>
                    <input type="number" id="inflationAnnualInterestRate" placeholder="Enter annual interest rate">
                    <label for="inflationRate">Annual Inflation Rate (%):</label>
                    <input type="number" id="inflationRate" placeholder="Enter annual inflation rate">
                    <label for="inflationTimePeriod">Time Period (years):</label>
                    <input type="number" id="inflationTimePeriod" placeholder="Enter time period in years">
                    <button onclick="calculateInflationAdjusted()">Calculate</button>
                    <div class="result" id="inflationResult"></div>
                </div>
            </div>
            <div id="goal" class="tab-content">
                <div class="widget">
                    <label for="goalAmount">Goal Amount (₹):</label>
                    <input type="number" id="goalAmount" placeholder="Enter goal amount">
                    <label for="goalLumpsumAmount">Lumpsum Amount (₹):</label>
                    <input type="number" id="goalLumpsumAmount" placeholder="Enter lumpsum amount">
                    <label for="goalAnnualInterestRate">Annual Interest Rate (%):</label>
                    <input type="number" id="goalAnnualInterestRate" placeholder="Enter annual interest rate">
                    <label for="goalInflationRate">Annual Inflation Rate (%):</label>
                    <input type="number" id="goalInflationRate" placeholder="Enter annual inflation rate">
                    <label for="goalInvestmentPeriod">Investment Period (years):</label>
                    <input type="number" id="goalInvestmentPeriod" placeholder="Enter investment period in years">
                    <button onclick="calculateGoalWithSIP()">Calculate</button>
                    <div class="result" id="goalResult"></div>
                </div>
            </div>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)