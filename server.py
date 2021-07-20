from flask import Flask, render_template_string

app = Flask(__name__)


@app.route("/")
def index():
    temp = "20°"
    hot = float(temp[:-1]) > 37.5
    classs = "hot" if hot else "cold"
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Temp</title>
            <script async defer src="https://buttons.github.io/buttons.js"></script>
        </head>
        
        <body>
            <header>
                <nav>
                    <h5>Température du rasperry</h5>
                    <img src="https://upload.wikimedia.org/wikipedia/fr/thumb/3/3b/Raspberry_Pi_logo.svg/1200px-Raspberry_Pi_logo.svg.png"
                         alt="rasperry">
                    <a class="github-button" href="https://github.com/ahmedlahrizi/rasp_temp"
                       data-icon="octicon-star" data-size="large" data-show-count="true"
                       aria-label="Star ahmedlahrizi/rasp_temp on GitHub">Star</a>
                </nav>
            </header>
            <div class="info">
                <h1>La temperature du rasperry est de:
                    <span class={{ classs }}>
                    {{ temp }}°
               </span>
                </h1>
            </div>
        
            {% if hot %}
                <img src="https://emoji.gg/assets/emoji/hot.png" alt="hot">
            {% else %}
                <img src="https://emoji.gg/assets/emoji/7655_freezing.png" alt="cold">
            {% endif %}
            <p>Merci de ne pas envoyer trop de requêtes au serveur (il va cramer)</p>
        
            <footer>
                <p>Ahmed LAHRIZI</p>
            </footer>
        </body>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Work+Sans:wght@500&display=swap');
            
            * {
                box-sizing: border-box;
                font-family: "Roboto", "Lucida Grande", "DejaVu Sans", "Bitstream Vera Sans", Verdana, Arial, sans-serif;
                margin: 0;
                padding: 0;
            }
            
            html {
                background-color: #26293d;
            }
            
            header {
                background-color: #1E1E2D;
                width: 100%;
            }
            
            nav {
                width: min(70rem, 100%);
                margin: auto;
                font-size: 3rem;
                display: flex;
                align-items: center;
                gap: 3rem;
                justify-content: start;
                height: 7rem;
            }
            
            header *:last-child {
                margin-left: auto;
            }
            
            nav > img {
                width: 4rem;
                height: 4rem;
            }
            
            nav > h5 {
                color: #FFF;
            }
            
            body * {
                color: #FFFFFFB2;
            }
            
            body {
                display: flex;
                flex-flow: column nowrap;
                gap: 3rem;
            }
            
            .info {
                font-weight: 100;
                color: #FFF;
                align-self: center;
                margin-top: 2rem;
            }
            
            body > img {
                width: 10rem;
                align-self: end;
                margin-right: 3rem;
            }
            
            .cold {
                color: #90c5ff;
            }
            
            .hot {
                color: #de3f6a;
            }
            
            footer * {
                color: #5dbbba;
                font-family: 'Work Sans', sans-serif;
                font-weight: bold;
                font-size: 2rem;
                margin-left: 2rem;
            }
            
            body > p {
                font-size: 2rem;
                color: #FFFFFF;
                align-self: center;
            }
            
            @media all and (max-width: 70.6875rem ) {
                :root {
                    font-size: .8rem;
                }
            }
            
            @media all and (max-width: 50rem ) {
                :root {
                    font-size: .7rem;
                }
            }
            
            @media all and (max-width: 41.875rem ) {
                :root {
                    font-size: .4rem;
                }
                nav *:first-child {
                    margin-left: 5px;
                }
            }
    </style>
    </html>
    """,
                                  temp=temp,
                                  hot=hot,
                                  classs=classs)
