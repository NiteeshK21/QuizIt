import flet as ft
import csv
from flet import theme

def main(page: ft.page):
    # page.theme = theme.Theme(color_scheme_seed="yellow")
    # page.window_width=550
    # page.window_height=309
    # page.horizontal_alignment="center"
    # img=(ft.Image(src="backg.jpg",fit="fill"))
    # page.add(img)

    def btn_click(e):
        username.error_text=""
        password.error_text=""
        if not username.value or not password.value:
            if not username.value:
                username.error_text="Please enter your username"
                page.update()
            if not password.value:
                password.error_text="Please enter your password"
                page.update()
        else:
            user=username.value
            passw=password.value
            with open("Data/users.csv","r") as csvfile:
                rows=[]
                csvreader=csv.reader(csvfile)
                fields=next(csvreader)
                for row in csvreader:
                    rows.append(row)
                user_mila=0
                for row in rows:
                    if(row[0]==user):
                        user_mila=1
                        if(row[1]==passw):
                            page.clean()
                        else:
                            print(row[1])
                            password.error_text="Password Incorrect!"
                if(user_mila==0):
                    username.error_text="User not found!"
            page.add(ft.Text("Hogya"))
    
    page.window_resizable=False
    page.bgcolor="white"
    heading=ft.Text(value="Welcome to QuizIt",size=35,bgcolor='pink',text_align="left")
    login=ft.Text(value="Please log in to continue",size=20,color='pink600',bgcolor='white')
    username=ft.TextField(label="Enter your username",border_color="grey")
    password=ft.TextField(label="Enter your password",border_color='grey',password=True, can_reveal_password=True)
    submit=ft.ElevatedButton("Login",on_click=btn_click)
    page.add(heading,login,username,password,submit)


ft.app(target=main,assets_dir="/home/niteeshk/PythonProject/Data")