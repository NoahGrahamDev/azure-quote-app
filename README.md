# 🌤️ Quote of the Day – Azure Flask App

A simple Flask web app deployed to **Azure App Service** that displays a new inspirational quote every time you load the page. Quotes are pulled live from the [ZenQuotes.io API](https://zenquotes.io).

## 🚀 Live Demo

👉 [View Live App](https://noahg-quote-app-b0d9bdd7fuhvg4gq.centralus-01.azurewebsites.net/)



---

## 🧰 Built With

- **Python + Flask** – lightweight web app framework
- **ZenQuotes API** – delivers random quotes
- **Azure App Service** – cloud hosting with scaling support
- **Gunicorn** – production WSGI server (auto-configured in Azure)
- **GitHub Actions** – automated deployment pipeline
- **Application Insights** – live monitoring, performance tracking, and alerting

---

## 📁 Project Structure

```bash
.
├── main.py               # Main Flask app
├── requirements.txt      # Python dependencies
└── .github/workflows     # GitHub Actions deployment workflow
