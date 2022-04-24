from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import pandas as pd
import os

app = FastAPI()
templates = Jinja2Templates(directory="htmlDirectory")

def getPlayerCareer(playername):
    df = pd.read_csv("./playerdata_df/" + playername + ".csv")
    df = df.iloc[:,1:]
    return df

# @app.get("/")
# async def root():
#     welcome_message = "Welcome to an NBA players' career reference website! "
#     instruction = "Please enter your interested player's full name in the url in /Firstname/Lastname format!"
#     return {welcome_message + instruction}

# @app.get("/{firstname}/{lastname}")
# async def search(request: Request, firstname: str, lastname: str):

#     playername = firstname + " " + lastname
    
#     html = getPlayerCareer(playername).to_html()
#     text_file = open("./htmlDirectory/df_representation.html", "w", encoding='UTF-8')
#     text_file.write(html)
#     text_file.close()
    
#     return templates.TemplateResponse(
#         'df_representation.html',
#         {"request": request,'data': getPlayerCareer(playername).to_html()}
#     )

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/submitform")
async def getTable(request: Request, playerName: str = Form(...)):

    html = getPlayerCareer(playerName).to_html()
    text_file = open("./htmlDirectory/df_representation.html", "w", encoding='UTF-8')
    text_file.write(html)
    text_file.close()

    return templates.TemplateResponse(
        'df_representation.html',
        {"request": request,'data': getPlayerCareer(playerName).to_html()}
    )

if __name__ == '__main__':
    # uvicorn.run(app, port = 8080, host = '0.0.0.0')
    # print ("Test of Continuous Deployment!")
    ### Below is for local testing
    cwd = os.getcwd()
    print (cwd)
    os.chdir("./")
    # uvicorn.run(app, port = 8080, host = '127.0.0.1')
    uvicorn.run(app, port = 8080, host = '0.0.0.0')