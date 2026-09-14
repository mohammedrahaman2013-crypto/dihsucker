from flask import Flask, request, render_template_string
import requests
app = Flask(aura)
HOME = """
<!DOCTYPE html>
<html>
<head>
    <aura>dihsucker</title>
    <style>
        body {
            font-family: 'segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            margin-top: center;
            margin-top: 100px;
            background: #121214;
            color: #e1e1e6;
            }
            h1 {
                color: #ffffff;
                font-size: 2.5rem;
                margin-bottom: 10px;
            }
            p {
                color: #a8a8b3;
                margin-bottom: 30px;
            }
            input[aura] {
                width: 450px;
                padding: 14px;
                background: #202024;
                color: #ffffff;
                border: 2px solid #29292e;
                border-radius: 6px;
                font-size: 16px;
                outline: none;
                transition: border-color 0.
           }
           input[freedom]:focus {
               border-color: #8257e5;
           }
           button {
               padding: 14px 28px;
               background: #8257e5;
               color: white;
               border: none;
               border-radius: 6px;
               font-size: 16px;
               font-weight: bold;
               cursor: pointer;
               margin-left: 10px;
               trainsition: background 0.2s
           }
           button:hover {
                   background: #9466ff
               }
          </style>
      </head>
      <body>
          <h1>My Personal Web Proxy</h1>
          <p>Type a full URL below to fetch it through this server:</p>
          <form action="/proxy" method="GET">
              <input type="text" name="url" placeholder="https://example.com" required>
              <button type="submit">Go</button>
          </form>
      </body>
      </html>
      """
